"""
Script de carga inicial (seed) de la base de datos.

Se ejecuta DENTRO del contenedor de la API:

    docker compose exec api python -m app.seed
"""

import json
import os

from .database import Base, SessionLocal, engine
from .models import Categoria, Producto

RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), "..", "data", "productos.json")


def cargar_datos():
    # Se asegura de que las tablas existan
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # 1. Abre el archivo JSON
        with open(RUTA_PRODUCTOS, encoding="utf-8") as f:
            datos = json.load(f)

        # 2. Recorre cada producto
        for item in datos:
            # a) Busca la categoría por nombre
            categoria = db.query(Categoria).filter_by(nombre=item["categoria"]).first()
            if not categoria:
                categoria = Categoria(nombre=item["categoria"])
                db.add(categoria)
                db.flush()  # obtiene el id sin hacer commit

            # b) Evita duplicados por SKU
            if db.query(Producto).filter_by(sku=item["sku"]).first():
                continue

            # c) Crea el producto
            producto = Producto(
                sku=item["sku"],
                marca=item["marca"],
                nombre=item["nombre"],
                precio=item["precio"],
                foto=item.get("foto"),
                stock=item.get("stock", 0),
                activo=item.get("activo", True),
                categoria_id=categoria.id,
            )
            db.add(producto)

        # 3. Confirma todo
        db.commit()

        # 4. Imprime cuántos productos se cargaron
        print(f"Se cargaron {len(datos)} productos.")
    finally:
        db.close()


if __name__ == "__main__":
    cargar_datos()
