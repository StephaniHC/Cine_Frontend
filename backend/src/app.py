import sys
import os
directorio_principal = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directorio_principal)

from flask import Flask
from controllers.pelicula_controller import pelicula_bp
from controllers.genero_controller import genero_bp
from controllers.clasificacion_controller import clasificacion_bp
from database.db_singleton import Database  
from config.config import DB_CONFIG


app = Flask(__name__) 
app.config['DB_HOST'] = DB_CONFIG['DB_HOST']
app.config['DB_USER'] = DB_CONFIG['DB_USER']
app.config['DB_PASSWORD'] = DB_CONFIG['DB_PASSWORD']
app.config['DB_NAME'] = DB_CONFIG['DB_NAME']
db = Database(app) 

# Llama a init_app para inicializar la base de datos
Database().init_app(app)

# Registra los blueprints
app.register_blueprint(pelicula_bp, url_prefix='/pelicula')
app.register_blueprint(genero_bp, url_prefix='/genero')
app.register_blueprint(clasificacion_bp, url_prefix='/clasificacion')

if __name__ == '__main__':
    app.run(debug=True, port=5000)