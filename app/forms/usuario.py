from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo
from app.controllers.usuario import Usuario_teste

class UsuarioForm(FlaskForm):
    username = StringField('Usuário:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired()])
    #password_hash=PasswordField('Senha:',validators=[DataRequired()])
    password_hash= PasswordField('Senha', validators=[DataRequired(),Length(min=6)])
    password2 = PasswordField('Confirmar Senha',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Salvar')
        

def validate_username(self, username):
  if not Usuario_teste.checar_unicidade(username.data.strip(), 'username'):
   raise ValidationError('Nome de usuário já cadastrado.')

def validate_email(self, email):
  if not Usuario_teste.checar_unicidade(email.data.strip().lower(), 'email'):
   raise ValidationError('Email já cadastrado.')