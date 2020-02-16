from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


times = [0000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400]

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign up!')

units = ["seconds", "minutes", "hours", "days", "weeks", "years", "decades"]



class GoalForm(FlaskForm):
    goal = StringField('Set Goal:', validators=[DataRequired()])
    notifyTime = StringField('Time to be notified for goal updates:', validators=[DataRequired()])
    notifyUnits = SelectField('Units', choices=list(enumerate(units)))
    goalLength = StringField('Time for goal', validators=[DataRequired()])
    goalUnits = SelectField('Units', choices=list(enumerate(units)))
    submit = SubmitField('Set your goal!')
