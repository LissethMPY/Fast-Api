from fastapi import FastAPI

# Crea una instancia de FastAPI
app = FastAPI()

# Define una ruta para el punto de entrada de la aplicación
@app.get("/")
async def read_root():
    return {"fast api de Lisseth": "¡Hola Mundo!"}
