# Twilio-WeatherApi

Aplicacion sencilla, que consulta el tiempo con Weather API y envia un sms al celular con ayuda de Twilio con el reporte del clima para el dia actual.

1. crea un entorno virtual con python: python -m venv venv
2. instala los paquetes necesarios: pip install -r requirements.txt
3. crea un archivo .env con la siguiente estructura
   
  TWILIO_ACCOUNT_SID ='zzz'
  TWILIO_AUTH_TOKEN ='zzz'
  PHONE_NUMBER ='+1 231 266 0452 (aqui va el numero que utilices en Twilio)'
  API_KEY_WAPI = 'zzz'
