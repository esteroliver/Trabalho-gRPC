import grpc
import asyncio
import requests
from grpc import aio
from google.protobuf.json_format import MessageToJson
from google.protobuf.struct_pb2 import Struct
from concurrent import futures

#dados da api retornam sobre o tempo em Natal/RN
def fetch_weather_data():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=-5.795&longitude=-35.2094&current_weather=true&timezone=America%2FSao_Paulo"
    )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "não foi possível acessar aos dados da API"}

class WeatherService:
    async def GetWeather(self, request, context):
        weather_data = fetch_weather_data()
        response_struct = Struct()
        response_struct.update(weather_data)
        return response_struct


async def server() -> None:
    server = grpc.aio.server()
    server.add_insecure_port("[::]:50051")
    print("Server running on port 50051...")
    await server.start()
    await server.wait_for_termination()

if __name__== '__main__':
    asyncio.run(server())