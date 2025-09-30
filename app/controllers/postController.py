from app import db
import sqlalchemy as sa
from app.models import Post

class PostController:
    def criar(formulario):
        try:
            form = Usuario()
            form.populate_obj(usuario)
            
            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
