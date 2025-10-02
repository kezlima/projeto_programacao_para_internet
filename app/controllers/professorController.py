from app.models.professor import ProfessorModel
from app import db


class Professor():
    def salvar(form):
        try:
            professor=ProfessorModel()
            form.populate_obj(professor)
            db.session.add(professor)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            print('Erro')
            return False