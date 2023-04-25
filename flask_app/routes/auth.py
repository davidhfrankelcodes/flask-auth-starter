from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_app.forms import LoginForm, SignupForm
from flask_app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_app import login_manager, db
import os
from dotenv import load_dotenv

load_dotenv()

SIGNUP_DISABLED = int(
    os.environ.get("FLASK_SIGNUP_DISABLED"))

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            return redirect(
                url_for('homepage.homepage'))

        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(
                username=username).first()

            if user and user.check_password(password):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(
                    next_page or url_for(
                        'homepage.homepage'))
            else:
                flash('Invalid username or password.')

    return render_template(
        'auth/login.html',
        form=form,
        signup_disabled=SIGNUP_DISABLED,)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # The implementation will be provided in the next step.
    form = SignupForm()
    if form.validate_on_submit() and not SIGNUP_DISABLED:
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered. You can now log in.')
        return redirect(url_for('auth.login'))
    return render_template(
        'auth/signup.html', 
        form=form, 
        signup_disabled=SIGNUP_DISABLED,)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
