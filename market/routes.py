from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user,logout_user,login_required,current_user

from market import app
from market.models import Item, User
from market.forms import RegisterForm, LoginForm,PurchaseForm,SellItemForm

from market import db


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/market/',methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        purchase_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchase_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"You have purchased: {p_item_object.name}",category="success")
            else:
                flash("You have not enough funds to make purchase",category="danger")

        # sell item
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"You have sold: {s_item_object.name}", category="success")
            else:
                flash("You do not have this product", category="danger")

        return redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        my_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items,purchase_form=purchase_form,selling_form=selling_form,my_items=my_items)


@app.route('/register/', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.email_address.data,
            password=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as: {user_to_create.username} ',category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data
        ).first()
        if attempted_user and \
                attempted_user.check_password_correction(
                    attempted_password=form.password.data
                ):
            login_user(attempted_user)
            flash(f"You are logged in as: {attempted_user.username}",category='success')
        else:
            flash("username or password is incorrect!!!",category='danger')
        return redirect(url_for('market_page'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("you are now logged out",category='info')
    return redirect(url_for('home_page'))


#5:27