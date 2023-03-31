from market import db, bcrypt, login_manager
from flask_login import UserMixin


# so that our system knows our identity in every page session
# it should be able to load user using login manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), default=1000)
    items = db.relationship('Item', backref='owning_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]}, {str(self.budget)[-3:]}'
        else:
            return self.budget

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_pass):
        self.password_hash = bcrypt.generate_password_hash(plain_text_pass).decode('utf-8')

    def __repr__(self):
        return self.username

    def check_password_correction(self, attempted_password):
        # it returns either true or false
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=30), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return self.name

# ended at 2:10
