import grpc
import asyncio
import requests
from grpc import aio
from google.protobuf.json_format import MessageToJson
from google.protobuf.struct_pb2 import Struct
from concurrent import futures

#fetch da API
def fetch_weather_data():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=-5.795&longitude=-35.2094&current_weather=true&timezone=America%2FSao_Paulo"
    )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "não foi possível acessar aos dados da API"}

#serviço
class WeatherService:
    async def GetWeather(self, request, context):
        weather_data = fetch_weather_data()
        response_struct = Struct()
        response_struct.update(weather_data)
        return response_struct


#servidor
async def server() -> None:
    server = grpc.aio.server()
    wheater_service = WeatherService()

    #registrando o serviço
    server.add_generic_rpc_handlers(
        [
            aio.unary_unary_rpc_method_handler(
                weather_service.GetWeather,
                request_deserializer=None,
                response_serializer=MessageToJson,
            )
        ]
    )
    
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()

if __name__== '__main__':
    asyncio.run(server())