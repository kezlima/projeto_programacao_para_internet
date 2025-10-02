from app import db
import sqlalchemy as sa
from app.models import Post, Usuario

class PostController:
    def criar(form):
        try:
            post= Post()
            form.populate_obj(post) 
            usuario=Usuario.query.get(3)
            post.author = usuario
            db.session.add(post)
            db.session.commit()
            print('salvo no banco')
            return True
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
