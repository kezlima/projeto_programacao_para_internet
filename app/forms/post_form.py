from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField

class PostForm(FlaskForm):
    body = StringField('Escreva a sua mensagem')
    submit = SubmitField('Enviar')