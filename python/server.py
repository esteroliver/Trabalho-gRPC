import grpc
import requests

infos = requests.get('https://api.open-meteo.com/v1/forecast?latitude=-5.795&longitude=-35.2094&current=temperature_2m,apparent_temperature,precipitation&timezone=America%2FSao_Paulo')
print(infos.json())