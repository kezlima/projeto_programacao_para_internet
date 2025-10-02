from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class UsuarioForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Por favor, preencha o nome de usuário.")])
    email = EmailField('Email', validators=[DataRequired(message="Por favor, preencha o email."), Email(message="Email inválido")])
    password_hash = PasswordField('Senha', validators=[DataRequired(),Length(min=6)])
    password2 = PasswordField('Confirmar Senha',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Salvar')