"""Configuración del frontend Flask."""

import os


class Config:
    # 1. Clave secreta para sesiones y cookies
    SECRET_KEY = os.environ.get("SECRET_KEY", "cambia-esta-clave")

    # 2. URL de la API (servicio FastAPI)
    #    - En Docker Compose: "http://api:8000"
    #    - En desarrollo local: "http://localhost:8000"
    API_URL = os.environ.get("API_URL", "http://localhost:8000")

