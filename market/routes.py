from flask import render_template, redirect, url_for, flash
from market import app
from market.models import Item, User
from market.forms import RegisterForm

from market import db


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/market/')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register/', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.email_address.data,
            password_hash=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user: {err_msg}','danger')
    return render_template('register.html', form=form)
