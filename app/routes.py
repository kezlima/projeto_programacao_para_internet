from app import app
from flask import render_template, flash
from app.forms.login_form import LoginForm
from app.forms.usuario_form import UsuarioForm
from app.forms.post_form import PostForm
from app.controllers.AuthenticationController import AuthenticationController
from app.controllers.usuarioController import UsuarioController
from app.controllers.postController import PostController
from app.forms.professor_form import ProfessorForm
from app.controllers.professorController import Professor

@app.route("/")
def home():
    return render_template("index.html", usuario = None, usuario_logado = False)


@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route('/post', methods = ['GET', 'POST'])
def post():
    formulario = PostForm()
    PostController.criar(formulario)
    return render_template('post.html', formulario = formulario)

@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        return AuthenticationController.login(formulario)
    return render_template('login.html', title='Login', form = formulario)


@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():
        sucesso = UsuarioController.salvar(formulario)
        if sucesso:
            flash("Usuario cadastrado com sucesso!", category="success")
            return render_template("index.html")
        else:
            flash("Erro ao cadastrar novo usuário.", category="error")
            return render_template("cadastro.html", form = formulario)
    return render_template('cadastro.html', titulo='Cadastro de Usuario', form = formulario)


@app.route('/listar', methods=['GET'])
def listar():
    lista_usuarios = UsuarioController.listar_usuarios()
    return render_template("listar.html", usuarios = lista_usuarios)


@app.route('/listar_filtro', methods=['GET'])
def listar_com_filtro():
    username = 'leosilva'
    usuario = UsuarioController.buscar_por_username(username)
    print(usuario.id, usuario.username, usuario.email)    
    return render_template("index.html")


@app.route('/atualizar/<int:id>', methods=['GET'])
def atualizar(id):
    form = UsuarioForm()
    form.username = 'atualizei_de_novo'
    UsuarioController.atualizar_usuario(id, form)
    return render_template("index.html")


@app.route('/remover/<int:id>', methods=['GET'])
def remover(id):
    UsuarioController.remover_usuario(id)
    return render_template("index.html")


###############################   EXERCICIOS DE REVISAO #############################


@app.route('/cadastrar_professor', methods=['GET', 'POST'])
def cadastrar_professor():
    form=ProfessorForm()
    if form.validate_on_submit():
        sucesso=Professor.salvar(form)
        if sucesso:
            print('Formulário enviado para o controller')
        
        else:
            print('Erro ao enviar formulário ')

    return render_template('cadastro_professor.html', form=form)