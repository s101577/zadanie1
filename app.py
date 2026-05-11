import os
import datetime
import logging
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

NAME = "Szymon Jagusiak"
PORT = 8080
START_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


logging.basicConfig(level=logging.INFO)
print(f"--- LOG STARTOWY ---", flush=True)
print(f"Data uruchomienia: {START_DATE}", flush=True)
print(f"Autor: {NAME}", flush=True)
print(f"Port TCP: {PORT}", flush=True)
print(f"--------------------", flush=True)
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def weather_page(city: str = "Warszawa"):

    temp = "18°C" 
    return f"""
    <html>
        <head><title>Pogoda - {NAME}</title></head>
        <body>
            <h1>Pogoda dla: {city}</h1>
            <p>Temperatura: {temp}</p>
            <p>Status: Słonecznie</p>
            <hr>
            <form action="/">
                <select name="city">
                  <option value="Warszawa">Warszawa</option>
                  <option value="Kraków">Kraków</option>
                  <option value="Gdańsk">Gdańsk</option>
                </select>
                <input type="submit" value="Sprawdź">
            </form>
            <footer>Autor: {NAME}</footer>
        </body>
    </html>
    """