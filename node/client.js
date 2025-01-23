const gRPC = require('@grpc/grpc-js');
const protoPack = require('@grpc/proto-loader');
const scanner = require("readline");
const data = scanner.createInterface({input: process.stdin, output: process.stdout});
const proto = protoPack.loadSync('weather_service.proto');
const weatherProto = gRPC.loadPackageDefinition(proto).weather;

const client = new weatherProto.WeatherService('localhost:50051', gRPC.credentials.createInsecure());

data.question("Digite a latitude: ", (latitude) => {
    data.question("Digite a longitude: ", (longitude) => {
        const request = {latitude: latitude, longitude: longitude};
        client.getWeather(request, (err, response) => {
            if(err) {
                console.error(err);
                return;
            }
            console.log(response.message);
        });
        data.close();
    });
});

// Carregar o arquivo .proto