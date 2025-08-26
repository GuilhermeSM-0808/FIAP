/*
------------------ FIAP --------------------
SPRINT 3 - TECH MAHINDRA
EDGE COMPUTING & COMPUTER SYSTEMS
Participantes:
Prof. Paulo Marcotti PF2150
Arthur Cotrick Pagani RM554510
Diogo Leles Franciulli RM558487
Felipe Sousa de Oliveira RM559085
Ryan Brito Pereira Ramos RM554497
--------------------------------------------
 
Canal ThingSpeak para Processamento dos Dados
https://thingspeak.com/channels/2642712
 
Este projeto desenvolvido como parte da entrega
para a Sprint 3 do Challenge da Tech Mahindra na
FIAP demonstra uma aplicação de Internet das Coisas
(IoT) usando o microcontrolador ESP32 para monitorar
dados ambientais e a velocidade de um carro de Fórmula
E, além de um sistema de alerta de proximidade.
Utilizando um Sensor DHT22, um Potenciômetro (utilizado
para simular um velocímetro) e um Sensor Ultrassônico
de Distância HC-SR04 (em conjunto de um Buzzer e um LED),
o sistema mede continuamente a temperatura e umidade do
ambiente onde se encontra o veículo, bem como sua velocidade
atual, enviando esses dados para a nuvem via Wi-Fi, onde são
armazenados e analisados em tempo real através do software
ThingSpeak. Localmente, ele emite avisos ao piloto quando
seu veículo se encontra muito próximo em relação ao veículo
da frente (1 metro ou menos de distância).
*/
 
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
 
#define DHTPIN 18 // Pino GPIO15 do ESP32 para o DHT22
#define DHTTYPE DHT11 // Tipo de sensor DHT (DHT11)
DHT dht(DHTPIN, DHTTYPE);
 
#define LUX_PIN 34 // Pino do ESP32 para o Potenciômetro
 
 
// Credenciais
const char* ssid = "FIAP-IOT"; // Rede Wi-Fi
const char* password = "F!@p25.IOT"; // Senha da rede Wi-Fi
const char* apiKey = "WBD6WF9Z8RSREZ99"; // Write API Key
const char* server = "http://api.thingspeak.com"; // Servidor ThingSpeak
 
void setup() {
  Serial.begin(115200);
  dht.begin();
 
  // Configuração dos pinos
  pinMode(LUX_PIN, INPUT);
 
  // Inicialização e loop de verificação da rede Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Conectando ao WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" conectado!");
}
 
void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    // Leitura dos sensores
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    int lux = analogRead(LUX_PIN); // Leitura do valor do Potenciômetro
    Serial.println("Valor lux: "+ String(lux));
    int valor_lux = map(lux, 0, 4065, 0, 100);
 
    if (isnan(h) || isnan(t)) {
      Serial.println("Falha ao ler o sensor DHT11!");
      return;
    }
 
   
 
    // Envio de dados para o ThingSpeak
    HTTPClient http;
    String url = String(server) + "/update?api_key=" + apiKey + "&field1=" + String(valor_lux) + "&field2=" + String(t) + "&field3=" + String(h);
    http.begin(url);
 
    int httpCode = http.GET();
    if (httpCode > 0) {
      String payload = http.getString(); // Resposta da requisição HTTP
      Serial.println("Dados enviados ao ThingSpeak.");
      Serial.print("Código HTTP: ");
      Serial.println(httpCode);
      Serial.println("Resposta: ");
      Serial.println(payload);
    } else {
      Serial.print("Erro ao enviar dados. Código HTTP: ");
      Serial.println(httpCode);
    }
   
    http.end();
  } else {
    Serial.println("WiFi não conectado. Tentando reconectar...");
  }
 
  // Espera 15 segundos para enviar a requisição novamente
  delay(5000);
}