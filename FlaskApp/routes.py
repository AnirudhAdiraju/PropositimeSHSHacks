from flask import render_template, flash, redirect, request
from app import app
from app.loginform import LoginForm, SignupForm, GoalForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Spandan'}
    return render_template('main.html', title='Home', user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    sign = SignupForm()
    if sign.validate_on_submit():
        flash('Signup requested for user {}, password {}'.format(
            sign.username.data, sign.password.data))
        return redirect('/index')
    return render_template('signup.html', title='Sign Up', form=sign)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/setgoal', methods=['GET','POST'])
def goal():
    goal = GoalForm()
    if goal.validate_on_submit():
        flash("New Goal set")
        return redirect('/index')
    return render_template('goal.html', title='Goals!', form=goal)
