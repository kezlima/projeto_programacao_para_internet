from flask import flash, render_template

class AuthenticationController:

    def login(form):
        
        flash(f"O usuario {form.usuario.data} fez o login, e o email é {form.email.data}")
        usuario_logado = { 
            'nome' : form.usuario.data
        }
        return render_template('index.html', usuario=usuario_logado, usuario_logado=True)