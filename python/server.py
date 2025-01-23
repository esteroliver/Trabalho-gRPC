import grpc
import asyncio
import requests
import weather_service_pb2
import weather_service_pb2_grpc

#serviço
class WeatherService(weather_service_pb2_grpc.WeatherServiceServicer):
    def GetWeather(self, request, context):
        print(f"Recebida uma requisição para: {request.latitude} - {request.longitude}")
        response = requests.get(
            f'https://api.open-meteo.com/v1/forecast?latitude={request.latitude}&longitude={request.longitude}&current=temperature_2m,apparent_temperature,precipitation&timezone=America%2FSao_Paulo'
        )
        weather_data = response.json()
        temperatura, graus = weather_data["current"]["temperature_2m"], weather_data["current_units"]["temperature_2m"]
        sensacao_termica = weather_data["current"]["apparent_temperature"]
        precipitacao = weather_data["current"]["precipitation"]
        mensagem = f"""\nTemperatura atual: é {temperatura} {graus}.
A sensação térmica é de {sensacao_termica} {graus}.
{f"Está chovendo {precipitacao} mm." if precipitacao > 0 else "Não está chovendo."}\n"""
        return weather_service_pb2.WeatherResponse(message=mensagem)

#servidor
async def server() -> None:
    server = grpc.aio.server()
    weather_service_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port("localhost:50051")
    print("Servidor rodando na porta 50051")
    await server.start()
    await server.wait_for_termination()

if __name__== '__main__':
    asyncio.run(server())