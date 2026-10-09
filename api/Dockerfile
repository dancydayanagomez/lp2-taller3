FROM python:3.11-slim

WORKDIR /app

# Copiamos primero solo requirements.txt para aprovechar el cache de Docker:
# si el código cambia pero las dependencias no, esta capa no se reconstruye.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Comando para levantar el servidor uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]