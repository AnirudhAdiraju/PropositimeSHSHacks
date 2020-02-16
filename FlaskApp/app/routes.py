from flask import render_template, flash, redirect, request, current_app
from app import app
from app.loginform import LoginForm, SignupForm, GoalForm
from app import models
from app.models import User
from app.models import everyone, everyusername

guylogged = False
currentUser = ""

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    sign = SignupForm()
    if sign.validate_on_submit():
        if (sign.password.data == sign.confirmPassword.data):
            User(sign.username.data, sign.password.data, sign.email.data)
        return redirect('/index')
    return render_template('signup.html', title='Sign Up', form=sign)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        if (form.password.data == everyone[everyusername.index(form.username.data)].getPassword()):
            everyone[everyusername.index(form.username.data)].login()
            guylogged = True
            currentUser = everyone[everyusername.index(form.username.data)].getUsername()
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/setgoal', methods=['GET','POST'])
def goal():
    goal = GoalForm()
    if not guylogged:
        return redirect('/login')
    else:
        if goal.validate_on_submit():
            everyone[everyusername.index(currentUser)].addGoal(goal.goal.data, goal.notifyTime.data,
                                               goal.notifyUnits.data, goal.goalLength.data,
                                               goal.goalUnits.data, goal.final.data,
                                               goal.finalUnits.data)




            flash("New Goal set")
            return redirect('/index')
    return render_template('goal.html', title='Goals!', form=goal)
