from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    body = StringField('Digite a mensagem:', validators=[DataRequired()])
    submit=SubmitField('Enviar')
   