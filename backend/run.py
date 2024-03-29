from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
import hashlib

app = Flask(__name__)

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta a la base de datos
db_path = os.path.join(current_dir, 'backend', 'Usuarios.db')

# Conexión a la base de datos
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Crear la tabla de usuarios si no existe
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                rol TEXT NOT NULL
            )''')
conn.commit()

# Ruta para el formulario de registro del administrador principal
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Verificar si el usuario ya está registrado
        c.execute("SELECT * FROM usuarios WHERE username=?", (username,))
        usuario_existente = c.fetchone()

        if usuario_existente:
            return "El nombre de usuario ya está en uso. Por favor, elige otro."

        # Cifrar la contraseña antes de guardarla en la base de datos
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Insertar el nuevo usuario en la base de datos como administrador
        c.execute("INSERT INTO usuarios (username, password, rol) VALUES (?, ?, ?)",
                    (username, hashed_password, 'administrador'))
        conn.commit()

        return redirect(url_for('inicio'))  # Redireccionar a la página de inicio después del registro

    return render_template('registro.html')

# Ruta para mostrar los usuarios registrados
@app.route('/usuarios')
def mostrar_usuarios():
    # Consultar todos los usuarios en la base de datos
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)

