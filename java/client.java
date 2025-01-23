import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import weather.WeatherServiceGrpc;
import weather.WeatherRequest;
import weather.WeatherResponse;

public class WeatherClient {
    public static void main(String[] args) {
        // Criando o canal de comunicação com o servidor gRPC
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()  // Usando comunicação sem criptografia para desenvolvimento
                .build();

        // Criando o stub (cliente) para o serviço WeatherService
        WeatherServiceGrpc.WeatherServiceBlockingStub stub = WeatherServiceGrpc.newBlockingStub(channel);

        // Criando a requisição
        WeatherRequest request = WeatherRequest.newBuilder()
                .setLocation("Natal, RN")
                .build();

        // Chamando o método GetWeather e recebendo a resposta
        WeatherResponse response = stub.getWeather(request);

        // Exibindo a resposta
        System.out.println("Clima em Natal, RN:");
        System.out.println(" - Temperatura: " + response.getTemperature() + "°C");
        System.out.println(" - Umidade: " + response.getHumidity() + "%");
        System.out.println(" - Precipitação: " + response.getPrecipitation() + "mm");

        // Fechando o canal
        channel.shutdown();
    }
}
