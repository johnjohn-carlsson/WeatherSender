import requests
from twilio.rest import Client

# Weather API configuration (Weather service)
api_key = '[INSERT API KEY HERE]'
city = '[INSERT CITY HERE]'
weather_api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'

# Twilio configuration (SMS service)
account_sid = '[INSERT SID HERE]'
auth_token = '[INSERT TOKEN HERE]'
sender = '[INSERT NUMBER HERE]'
recipient = '[INSERT NUMBER HERE]'
client = Client(account_sid, auth_token)

# Fetch weather data, convert temp to 1 decimal Celcius.
response = requests.get(weather_api_url)
data = response.json()
temperature = round(int(data['main']['temp']) - 273.15)
conditions = data['weather'][0]['description']

# Format the message
message = f"Tjenare mannen! Här kommer dagens väderrapport för {city}:\n" \
          f"Temperature: {temperature}°C\n" \
          f"Condition: {conditions}\n" \
          f"Ha en bra dag!"

# Send the message via Twilio
message = client.messages.create(
  from_=sender,
  body=message,
  to=recipient
)

# Check if program was run through
print("Weather report sent successfully!")