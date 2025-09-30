from app.models import Post
from app import db


class Postagem:
    def salvar(form):

        try:
            postagem=Post()
            form.populate_obj(postagem)
            db.session.add(postagem)
            db.session.commit()
            print('Deu certo')

        except Exception as e:
            db.session.rollback()
            print('deu erro')