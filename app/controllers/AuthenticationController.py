from flask import render_template, flash
from flask_login import login_user, logout_user
from app.models.usuario import Usuario



class AuthenticationController:
    
    def login(form):
        flash(f"O usuario {form.username.data} fez o login, lembrar={form.remember_me.data}")
        usuario_logado = {
            'nome': form.username.data
        }

        username=form.username.data.strip()
        user=Usuario.query.filter_by(username=username).first()


        return render_template("index.html", usuario = usuario_logado, usuario_logado = True)
    


    def logout():
        return logout_user()