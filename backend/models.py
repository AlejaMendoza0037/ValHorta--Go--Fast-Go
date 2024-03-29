import sqlite3

# Función para conectar a la base de datos SQLite
def connect_db():
    return sqlite3.connect('db/usuarios.db')
