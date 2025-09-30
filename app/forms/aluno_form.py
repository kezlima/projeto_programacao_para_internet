from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AlunoForm(FlaskForm):
    nome = StringField('Nome:', validators=[DataRequired()])
    turma = StringField('Turma:', validators=[DataRequired()])
    submit=SubmitField('Salvar')