"""
Punto de entrada del frontend.

Ejecutar con:
    python run.py
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Ejecuta la app escuchando en 0.0.0.0 para que sea accesible desde fuera del contenedor
    app.run(host="0.0.0.0", port=5000, debug=True)

