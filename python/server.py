import grpc
import asyncio
import requests
from concurrent import futures
from weather_service_pb2 import WeatherResponse
from weather_service_pb2_grpc import WeatherServiceServicer, add_WeatherServiceServicer_to_server

#fetch da API
# def fetch_weather_data():
#     response = requests.get(
#         "https://api.open-meteo.com/v1/forecast?latitude=-5.795&longitude=-35.2094&current_weather=true&timezone=America%2FSao_Paulo"
#     )
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": "não foi possível acessar aos dados da API"}

#serviço
class WeatherService(WeatherServiceServicer):
    # Implementação do método GetWeather
    def GetWeather(self, request, context):
        print(f"Recebida uma requisição para: {request.location}")

        # Dados simulados de previsão do tempo
        response = WeatherResponse(
            temperature=28.5,
            humidity=75.0,
            precipitation=0.0
        )
        return response

#servidor
async def server() -> None:
    server = grpc.aio.server()
    add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()

if __name__== '__main__':
    asyncio.run(server())