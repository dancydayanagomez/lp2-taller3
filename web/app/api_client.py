"""
Cliente HTTP hacia el servicio 'api'.

Este módulo concentra TODAS las llamadas de red hacia la API, para que
routes.py no tenga que preocuparse por URLs, timeouts o códigos de estado.
"""

import requests
from flask import current_app

TIMEOUT = 5  # segundos máximo de espera por respuesta de la API


def obtener_productos(categoria_id=None):
    """Retorna la lista de productos (dicts) desde la API."""
    url = f"{current_app.config['API_URL']}/productos/"
    parametros = {"categoria_id": categoria_id} if categoria_id is not None else {}
    try:
        respuesta = requests.get(url, params=parametros, timeout=TIMEOUT)
        if respuesta.status_code == 200:
            return respuesta.json()
        return []
    except requests.RequestException:
        return []


def obtener_producto(sku):
    """Retorna un producto (dict) por su SKU, o None si no existe."""
    url = f"{current_app.config['API_URL']}/productos/{sku}"
    try:
        respuesta = requests.get(url, timeout=TIMEOUT)
        if respuesta.status_code == 200:
            return respuesta.json()
        return None
    except requests.RequestException:
        return None


def obtener_categorias():
    """Retorna la lista de categorías (dicts) desde la API."""
    url = f"{current_app.config['API_URL']}/categorias/"
    try:
        respuesta = requests.get(url, timeout=TIMEOUT)
        if respuesta.status_code == 200:
            return respuesta.json()
        return []
    except requests.RequestException:
        return []
