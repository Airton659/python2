from datetime import datetime
from app import alquimias
from flask import render_template,request, redirect, url_for,flash
from app import app
from app.alquimias import create_post,get_timeline
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)



@app.route('/')
def index():
    user = current_user if current_user.is_authenticated else None
    posts = get_timeline() if user else []
    return render_template(
        'index.html',
        title='Página Inicial',
        user=user,
        posts=posts
    )
    # if current_user.is_authenticated:
    #     user = current_user
    # return render_template(
    #     'index.html',
    #     title = 'Página Inicial',
    #     user = user

    # )


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        user = alquimias.validate_user_password(username,password)
        if user:
            user.last_login = datetime.now()
            flash('Login bem sucedido!')
            login_user(user,remember = user.remember)
            return redirect(url_for(f"index"))
        else:
            flash('Usuário ou senha inválidos')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form ['username'].lower()
        if alquimias.user_exist(username):
            flash('Usuário já existe!')
            return redirect(url_for('login'))
        else:
            username = username
            password = request.form['password'].lower()
            profile_picture = request.form.get('profile')
            bio = request.form.get('bio')
            remember = True if request.form.get('remember') == 'on' else False
            user = alquimias.create_user(username, password, profile_picture, bio, remember)
            login_user(user,remember = remember)
            return redirect(url_for(f'index'))
    return render_template('cadastro.html')
    
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(f'index'))


@app.route('/post', methods = ['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        if not body.strip():
            flash('O post não pode estar vazio!')
            return redirect(url_for('post'))
        create_post(body, current_user)
        flash('Post publicado com sucesso!')
        return redirect(url_for('index'))
    return render_template('post.html')