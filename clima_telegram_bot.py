# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 14:14:38 2022

@author: Precision
"""
 
import requests
import json
import emoji
from datetime import datetime

def fecha_hora():
    date = datetime.now()
    fecha = date.date()
    hora = date.time().strftime("%H:%M:%S")
    emojis =emoji.emojize(':mega:', language='alias')
    return f'{emojis} Fecha del reporte {fecha}\n {emojis}Hora del reporte {hora} \n'
    
#Lectura de credenciales para ingresar a telegram
def credenciales():
    datos = []
    with open('credenciales.txt') as file:
        lineas = file.readlines()
        for linea in lineas :
            datos.append(linea.strip('\n'))            
    return datos
datos= credenciales()

#Acceso API Telegram
TELEGRAM_BOT_TOKEN = datos[0]
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
chat_id = datos[1]  #Para grupo de telegram

#Request página open weather
pagina = https://api.openweathermap.org/data/2.5/onecall?lat={latitud}&lon={longitud}&exclude=hourly,daily&appid={API KEY}&units=metric
page = requests.get(str(pagina))
json_data = json.loads(page.text)

#Guardar datos en archivo
# file = open('datos.txt', 'w')
# file.write(str(json_data))
# file.close()

#Envío de la frase en bot de telegram
message = (format('{}El reporte actual del clima{} \n {} {} La temperatura actual es {} ºC \n {}El indíce de radiación UV es {}\n {}La humedad es de {} % \n '
                  .format(emoji.emojize(':earth_americas:', language='alias'), emoji.emojize(':cyclone:', language='alias'),
                          fecha_hora(),
                          emoji.emojize(':thermometer:', language='alias'),json_data['current']['temp'],
                          emoji.emojize(':sun:', language='alias'), json_data['current']['uvi'], 
                          emoji.emojize(':cloud:', language='alias'),json_data['current']['humidity'], )))
params = {"chat_id": chat_id, "parse_mode": "Markdown", "text": message}
requests.get(TELEGRAM_API_URL, params=params)

print(message)


