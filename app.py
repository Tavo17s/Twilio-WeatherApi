import os
import requests
import pandas as pd
from dotenv import load_dotenv

from twilio.rest import Client

load_dotenv()
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
phone_number = os.environ.get('PHONE_NUMBER')
api_key = os.environ.get('API_KEY_WAPI')

city = 'SANTA MARTA'
url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no'
response = requests.get(url).json()


def get_forecast(response, i):

    fecha = response['forecast']['forecastday'][0]['hour'][1]['time'].split()[
        0]
    hora = int(response['forecast']['forecastday'][0]
               ['hour'][i]['time'].split()[1].split(':')[0])
    condicion = response['forecast']['forecastday'][0]['hour'][0]['condition']['text']
    temperatura = response['forecast']['forecastday'][0]['hour'][0]['temp_c']
    rain_prob = response['forecast']['forecastday'][0]['hour'][0]['will_it_rain']
    chance_rain = response['forecast']['forecastday'][0]['hour'][0]['chance_of_rain']

    return fecha, hora, condicion, temperatura, rain_prob, chance_rain


datos = []
for i in range(len(response['forecast']['forecastday'][0]['hour'])):
    datos.append(get_forecast(response, i))

col = ['fecha', 'hora', 'condicion', 'temperatura', 'rain_prob', 'chance_rain']
df = pd.DataFrame(datos, columns=col)

forecast_df = df[['hora', 'condicion', 'chance_rain']]
forecast_df.set_index('hora', inplace=True)

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=phone_number,
    body='\nHola! \n\n\n El pronostico de lluvia hoy ' +
    df['fecha'][0] + ' en ' + city + ' es : \n\n\n ' + str(forecast_df),
    to='+573016491031'
)
