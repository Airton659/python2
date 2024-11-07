from app import alquimias
from flask import render_template,request, redirect, url_for,flash
from app import app
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)

@app.route('/')
@login_required
def index():
    user = None
    if current_user.is_authenticated:
        user= current_user
    return render_template(
        'index.html',
        title = 'Página Inicial',
        user = user
    )


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        user = alquimias.validate_user_password(username,password)
        if user:        
            flash('Login bem sucedido!')
            login_user(user, remember=user.remember)
            return redirect(url_for(f"index"))
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
        user = alquimias.create_user(username,password, remember)
        login_user(user, remember=remember)
        return redirect(url_for(f'index'))
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(f'index'))
