from app.models import Usuario
from app import db
import sqlalchemy as sa
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user

class Usuario_teste:
    def salvar(form):
        try:
            usuario=Usuario()
            form.populate_obj(usuario)
            usuario.password_hash = generate_password_hash(form.password_hash.data)
            db.session.add(usuario)
            db.session.commit()
            print('salvou')
            return True

        except Exception as e:
            db.session.rollback()
            return False
        
    def lista_usuarios():
        query=sa.select(Usuario)
        usuarios=db.session.scalars(query)
        return usuarios
    
    def checar_unicidade(campo, tipo):
        if tipo == 'username':
            if Usuario.query.filter_by(username=campo).first():
             return False
            
        if tipo == 'email':
          if Usuario.query.filter_by(email=campo).first():
           return False
          
        return True
    
    def logout():
       return logout_user()