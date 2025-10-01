from app.models.professor import ProfessorModel
from app import db


class Professor():
    def salvar(form):
        try:
            professor=ProfessorModel()
            form.populate_obj(professor)
            db.session.add(professor)
            db.session.commit()
        except Exception as e:
            print('Erro')