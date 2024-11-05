from app import alquimias
from flask import render_template,request, redirect, url_for,flash
from app import app

@app.route('/')
def index():
    user = None
    username = request.args.get('username')
    if username: user = {'username': username}
    return render_template(
        'index.html',
        title = 'Página Inicial',
        user = user

    )


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        if alquimias.validate_user_password(username,password):
            flash('Login bem sucedido!')
            return redirect(url_for(f"index", username=username))
        else:
            flash('Usuário ou senha inválidos')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    username = request.form ['username'].lower()
    if alquimias.user_exist(username):
        flash('Usuário já existe!')
        return redirect(url_for('login'))
    else:
        username = username
        password = request.form['password'].lower()
        remember = True if request.form.get('remember') == 'on' else False
        alquimias.create_user(username, password, remember)
        return redirect(url_for(f'index', username=username))
