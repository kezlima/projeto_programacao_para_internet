
from app import app
from flask import Flask,  render_template
from app.forms.login_form import LoginForm
from app.controllers.AuthenticationController import AuthenticationController
from app.controllers.inserir import AuthenticationController
from app.forms.postagem import PostForm
from app import db
from app.models import Usuario
from app.controllers.postagem import Postagem
from flask import redirect
from app.models import Post
from app.forms.usuario import UsuarioForm
from app.controllers.usuario import Usuario_teste
from flask import url_for
from flask import flash



@app.route("/inserir_com_relacionamento", methods=['GET'])
def inserir_com_relacionamento():
    # Supondo que existe um usuario com id igual a 1
    usuario = Usuario.query.get(1)
    novo_post = Post(body="Post de exemplo", author=usuario)
    db.session.add(novo_post)
    db.session.commit()
    return redirect("/")

@app.route('/postagem', methods=['GET','POST'])
def postagem():
    form=PostForm()

    if form.validate_on_submit():

        postagem=Postagem.salvar(form)
        return 'Deu certo'

    return render_template('postagem.html', form=form)



@app.route('/')
def inicio(): 
    return render_template('index.html', usuario=None, usuario_logado=False)

@app.route('/sobre')
def sobre():
    return render_template('formulario.html')

@app.route('/endereco')
def pagina():
    return render_template('endereco.html')

@app.route('/sobre_mim')
def pagina2():
    return render_template('sobreMim.html')

@app.route('/pagina_derivada')
def pagina_derivada():
    return render_template('base2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    formulario =LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationController.login(formulario):
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos.", "error")
            return render_template('login.html', tittle="Login", form=formulario)

@app.route('/instituicao')
def bd():
    usuario = Usuario(username='bianca', email='biancalima@.com')
    db.session.add(usuario)
    db.session.commit()
    return render_template('index.html', usuario=None, usuario_logado=False)


@app.route('/lista_usuario', methods=['GET', 'POST'])
def lista_usuario():
    pass


@app.route('/inserir',  methods=['GET', 'POST'])
def inserir():

    form =UsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario_teste.salvar(form)
        print('enviou para o controler')
        if usuario:
            print('Deu certo na rota')
            return redirect(url_for('login'))
        else:
            print('Erro ao salvar no controller')
    else:
        print('Formulário inválido')

    return render_template('inserir.html', title="Cadastro", form=form)