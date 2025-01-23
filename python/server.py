import grpc
import asyncio
import requests
from concurrent import futures
from weather_service_pb2 import WeatherResponse
from weather_service_pb2_grpc import WeatherServiceServicer, add_WeatherServiceServicer_to_server

#serviço
class WeatherService(WeatherServiceServicer):
    def GetWeather(self, request, context):
        print(f"Recebida uma requisição para: {request.location}")
        response = requests.get(
            'https://api.open-meteo.com/v1/forecast?latitude=-5.795&longitude=-35.2094&current=temperature_2m,apparent_temperature,precipitation&timezone=America%2FSao_Paulo'
        )
        weather_data = response.json()
        temperature = weather_data["current"]["temperature_2m"]
        return temperature

#servidor
async def server() -> None:
    server = grpc.aio.server()
    add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()

if __name__== '__main__':
    asyncio.run(server())