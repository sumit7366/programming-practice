from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class QuestionForm(FlaskForm):
    topic = SelectField('Topic', choices=[], validators=[DataRequired()])
    question = TextAreaField('Question', validators=[DataRequired(), Length(min=10)])
    answer = TextAreaField('Answer', validators=[DataRequired(), Length(min=10)])
    difficulty = SelectField('Difficulty', 
                           choices=[('Basic', 'Basic'), ('Medium', 'Medium'), ('Advanced', 'Advanced')],
                           validators=[DataRequired()])
    submit = SubmitField('Add Question')

# Add this new form for topics
class TopicForm(FlaskForm):
    name = StringField('Topic Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Length(max=500)])
    submit = SubmitField('Add Topic')