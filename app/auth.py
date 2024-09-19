from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('base.html')

@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'

@auth.route('/sign-up')
def sign_up():
    return '<h1>Sign up</h1>'