from flask import Flask

app = Flask(__name__)

# Importa las rutas después de inicializar la aplicación para evitar problemas de importación circular
from app import routes
