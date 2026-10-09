"""
Rutas del frontend.

Aquí NO hay consultas ORM. Todo pasa por funciones de api_client,
que hacen peticiones HTTP al servicio 'api'. Esta vista Flask solo
se encarga de pedir datos y renderizar HTML.
"""

from flask import Blueprint, abort, render_template, request
from . import api_client

main = Blueprint("routes", __name__)


@main.route("/")
def index():
    categoria_id = request.args.get("categoria", type=int)

    # 1. Obtener productos filtrados (si hay categoria_id)
    productos = api_client.obtener_productos(categoria_id)

    # 2. Obtener todas las categorías
    categorias = api_client.obtener_categorias()

    # 3. Renderizar el catálogo
    return render_template(
        "index.html",
        productos=productos,
        categorias=categorias,
        categoria_id=categoria_id,
    )


@main.route("/producto/<sku>")
def detalle(sku):
    # 4. Obtener producto por SKU
    producto = api_client.obtener_producto(sku)

    # 5. Si no existe, abortar con 404
    if producto is None:
        abort(404)

    # 6. Renderizar detalle
    return render_template("detalle.html", producto=producto)


@main.route("/categorias")
def categorias():
    # 7. Obtener todas las categorías
    categorias = api_client.obtener_categorias()

    # 8. Renderizar listado de categorías
    return render_template("categorias.html", categorias=categorias)
