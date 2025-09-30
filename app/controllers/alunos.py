from app import db
from app.models.alunos import Aluno
import sqlalchemy as sa


class Alunos:
    def salvar_aluno(form):
        try:

            aluno=Aluno()
            form.populate_obj(aluno)
            db.session.add(aluno)
            db.session.commit()
            print('Aluno salvo')

        except Exception as e:
            print('Deu erro')

    def lista_alunos():
        query=sa.select(Aluno)  
        usuarios=db.session.scalars(query)  
        return usuarios   
