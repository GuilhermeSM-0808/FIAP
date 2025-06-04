#include <Wire.h>
#include <HardwareI2C.h>
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

// Usando ESP32

//Global
  //DHT
    #define DHTPIN 25
    #define DHTTYPE DHT11

    DHT dht(DHTPIN, DHTTYPE);

  //LCD
    #define col 16 // Serve para definir o numero de colunas do display utilizado
    #define lin  2 // Serve para definir o numero de linhas do display utilizado
    #define ende  0x27 // Serve para definir o endereço do display.

    LiquidCrystal_I2C lcd(ende,col,lin); // Chamada da funcação LiquidCrystal para ser usada com o I2C

  // Variables
    long OnTime = millis(); // Tempo que o dispositivo  esteve ligado
    long LastTime = 0;
    long Time = 0;
    float us1; // umidade do solo sensor 01
    float us2; // umidade do solo sensor 02
    float us_percent1;
    float us_percent2;
    float us_media;
    int display = 0;

void setup() {
  // Serial
    Serial.begin(9600);
    Serial.print("Starting...");

  //Pins setup
    pinMode(4, INPUT);
    pinMode(21, INPUT);
    pinMode(22, INPUT);
    pinMode(25, INPUT);
    pinMode(33, INPUT);

  //DHT
  dht.begin();

  //LCD
    lcd.clear();
    lcd.init();                    
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.print("Initiating...");
}

void loop() {

  //Tempo
    delay(1000);
    OnTime = millis();
    Time = OnTime - LastTime;
    //Serial.println(OnTime);
    Serial.print("Tempo: ");
    Serial.println(Time);
    //Serial.println(LastTime);

    if (Time / 5000 >= 1){
      lcd.clear();
      display++;
      if (display == 2){
        display = 0;
      }
      LastTime = OnTime;
    }

  //Humdity
    us1 = analogRead(4);
    us_percent1 = ((1 - (us1 / 4095))*100);
    us2 = analogRead(33);
    us_percent2 = ((1 - (us2 / 4095))*100);
    us_media = (us_percent1 + us_percent2) / 2;
    // Serial.println(us_percent1);
    // Serial.println(us_percent2);
    Serial.print("Umidade do solo: ");
    Serial.print(us_media);
    Serial.println("%");
    if (display == 0) {
      lcd.setCursor(0,0);
      lcd.print("Umidade do Solo: ");
      lcd.setCursor(0,1);
      lcd.print(us_media);
      lcd.print("%");
    }

  //DHT
    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    float h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();

      // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t)) {
      Serial.println(F("Failed to read from DHT sensor!"));
      return;
    }

    Serial.print(F("Umidade do Ar: "));
    Serial.print(h);
    Serial.println(F("%"));
    Serial.print(F("Temperatura: "));
    Serial.print(t);
    Serial.println(F("°C "));

    if (display == 1){
      lcd.setCursor(0,0);
      lcd.print("Temp: ");
      lcd.print(t);
      lcd.println("*C ");
    }

}
