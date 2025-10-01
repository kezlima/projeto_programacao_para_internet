from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class ProfessorForm(FlaskForm):
    nome=StringField('Digite seu nome:', validators=[DataRequired(message='Campo é obrigatório')])
    materia=StringField('Digite sua matéria:', validators=[DataRequired(message='Campo é obrigatório')])
    email=StringField('Digite seu email:', validators=[DataRequired(message='Campo é obrigatório')])
    senha=StringField('Digite sua senha:', validators=[DataRequired(message='Campo é obrigatório')])
    submit=SubmitField('Salvar')