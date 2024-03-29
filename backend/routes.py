from flask import render_template, request, redirect, session
from app import app
from app.models import connect_db

# Función para conectar a la base de datos SQLite
def connect_db():
    return sqlite3.connect('db/usuarios.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['logged_in'] = True
        session['username'] = username
        session['role'] = user[3]  # El rol del usuario se almacena en la cuarta columna de la tabla usuarios
        return redirect('/dashboard')
    else:
        return 'Credenciales incorrectas. <a href="/">Volver</a>'

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        if session['role'] == 'administrador':
            return render_template('admin_dashboard.html')
        elif session['role'] == 'agente':
            return render_template('agent_dashboard.html')
        elif session['role'] == 'tienda':
            return render_template('store_dashboard.html')
    return redirect('/')
