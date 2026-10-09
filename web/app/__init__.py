"""
Application factory del frontend.

CAMBIO CLAVE respecto al Taller 2: este servicio ya NO se conecta a
ninguna base de datos. Su única fuente de datos es la API (servicio
'api'), a través de peticiones HTTP.
"""

from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    # 1. Carga la configuración
    app.config.from_object(config_class)

    # 2. Importa y registra el blueprint 'main'
    from .routes import main
    app.register_blueprint(main)

    return app

