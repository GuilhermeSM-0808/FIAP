#include <Wire.h> // Biblioteca utilizada para fazer a comunicação com o I2C
#include <LiquidCrystal_I2C.h> // Biblioteca utilizada para fazer a comunicação com o display 20x4 
#include <DHT.h>


// CONFIG LCD I2C
  #define col 16 // Serve para definir o numero de colunas do display utilizado
  #define lin  2 // Serve para definir o numero de linhas do display utilizado
  #define ende  0x27 // Serve para definir o endereço do display.

  LiquidCrystal_I2C lcd(ende,col,lin); // Chamada da funcação LiquidCrystal para ser usada com o I2C

//CONFIG DHT
  //Pino conectado ao pino de dados do sensor
    #define DHTPIN 5
  //Utilize a linha de acordo com o modelo do sensor
    #define DHTTYPE DHT11   // Sensor DHT11
    //#define DHTTYPE DHT22   // Sensor DHT 22  (AM2302)
  //Definicoes do sensor : pino, tipo
  DHT dht(DHTPIN, DHTTYPE);

//Light Sensor Set up
    int Sensor_Luz = 4;
  // These constants should match the photoresistor's "gamma" and "rl10" attributes
    const float GAMMA = 0.7;
    const float RL10 = 50;

  // Convert the analog value into lux value:
    int analogValue = analogRead(A3);
    float voltage = analogValue / 1024. * 5;
    float resistance = 2000 * voltage / (1 - voltage / 5);
    float lux = pow(RL10 * 1e3 * pow(10, GAMMA) / resistance, (1 / GAMMA));

//Constantes - Setup
  int Button = 2;
  int Buzzer = 3;
  int LedR = 8;
  int LedY = 6;
  int LedG = 7;

//Variables
  long OnTime = millis();
  long LastTime = 0;
  long Time = 0;
  int Display = 0;
  bool TempOk = true;
  bool UmiOk = true;
  bool LuzOk = true;
  int instance = 0;

//Listas
  float list_t[5];
  float list_u[5];
  float list_lux[5];

void setup() {

  Serial.begin(9600);
  //Iniclaiza o sensor DHT
    dht.begin();
  // Iniciar tela LCD
    lcd.init(); // Serve para iniciar a comunicação com o display já conectado
    lcd.backlight(); // Serve para ligar a luz do display
    lcd.clear(); // Serve para limpar a tela do display

    lcd.println("Aguardando dados...");

  //Set up I/O
  pinMode(Buzzer, OUTPUT);
  pinMode(LedR, OUTPUT);
  pinMode(LedY, OUTPUT);
  pinMode(LedG, OUTPUT);
  pinMode(Sensor_Luz, INPUT);
  pinMode(Button, INPUT);
  pinMode(A3, INPUT);

  //Listas, valores inciais
  for(int i=0; i<5; i++){
    list_t[i]= 13.5;
    list_u[i]= 60.0;
    list_lux[i]= 1;
  }
}

void loop() {

  //Tempo
    delay(100);
    OnTime = millis();
    Time = OnTime - LastTime;
    //Serial.println(OnTime);
    Serial.println(Time);
    //Serial.println(LastTime);

  //Leitura de sensores
    //Leitura sensor de luz
      analogValue = analogRead(A3);
      voltage = analogValue / 1024. * 5;
      resistance = 2000 * voltage / (1 - voltage / 5);
      lux = pow(RL10 * 1e3 * pow(10, GAMMA) / resistance, (1 / GAMMA));

    //Leitura do sensor de umidade
      float u = dht.readHumidity();
    //Leitura do sensor de temperatura (Celsius)
      float t = dht.readTemperature();
  
  //Media dos Valores
    instance ++;
    if (instance == 10){
      list_u[0] = u;
      list_t[0] = t;
      list_lux[0] = lux;
    }
    else if (instance == 20){
      list_u[1] = u;
      list_t[1] = t;
      list_lux[1] = lux;
    }
    else if (instance == 30){
      list_u[2] = u;
      list_t[2] = t;
      list_lux[2] = lux;
    }
    else if (instance == 40){
      list_u[3] = u;
      list_t[3] = t;
      list_lux[3] = lux;
    }
    else if (instance == 50){
      list_u[4] = u;
      list_t[4] = t;
      list_lux[4] = lux;

      instance = 0;
    }

    u = ((list_u[0] + list_u[1] + list_u[2] + list_u[3] + list_u[4]) / 5);
    t = ((list_t[0] + list_t[1] + list_t[2] + list_t[3] + list_t[4]) / 5);
    lux = ((list_lux[0] + list_lux[1] + list_lux[2] + list_lux[3] + list_lux[4]) / 5);
  
  //Falhha ao Verificar Valores
    //Verifica se os sensores estao respondendo
    if (isnan(u) || isnan(t))
      {
        lcd.setCursor(0,0);
        lcd.println("Falha ao ler dados do sensor DHT !!!");
        return;
      }
    else if(isnan(lux))
      {
        lcd.setCursor(0,0);
        lcd.println("Falha ao ler dados do sensor de Luz !!!");
        return;
      }
    //Verificar se os valores estao dentro dos padroes
      if ( 10.0 <= t && t <= 15.0 ){
        TempOk = true;
      }
      else{
        TempOk = false;
      }
      if ( 50.0 <= u && u <= 70.0){
        UmiOk = true;
      }
      else{
        UmiOk = false;
      }
      if ( lux <= 10.5){
        LuzOk = true;
      }
      else{
        LuzOk = false;
      }


  //Mostrar no Display
    if (Time / 5000 >= 1){
      lcd.clear();
      Display ++;
      LastTime = OnTime;
    if (Display >= 3){
      Display = 0;
    }
    }
    //Botao pressionado mudar para prox display
    if (digitalRead(Button) == 1){
      lcd.clear();
      Display ++;
      LastTime = OnTime;
    }
    // Se todas a medidas estiverem dentro do parametro, mostrar cada medida de 5 em 5 segundos
    if (TempOk == true && UmiOk == true && LuzOk == true){
      //Mostra a temperatura no display
      if (Display == 0){
          lcd.setCursor(0,0);
          lcd.print("Temperatura: OK"); 
          lcd.setCursor(0,1);
          lcd.print("Temp: "); 
          lcd.print(t);
          lcd.print(" *C  ");
        }
      //Mostra a umidade no display
      else if (Display == 1){
        lcd.setCursor(0,0);
        lcd.print("Umidade: OK"); 
        lcd.setCursor(0,1);
        lcd.print("Umidade: "); 
        lcd.print(u);
        lcd.println(" %");
      }
      //Mostrar a luminosidade
      else if (Display == 2){
        if (lux > 1){
          lcd.setCursor(0,0);
          lcd.print("Ambiente a meia"); 
          lcd.setCursor(0,1);
          lcd.print("Luz...."); 
        }
        else{
          Display = 0;
        }
      }
    }
    // Se uma das medidas nao estiver dentro dos parametros, pular as medidas que estao dentro do parametro, mostrar apenas as foras e mudar entre elas a cada 5 segundos
    else {
      //Mostar a temperatura
      if (Display == 0){
        if (TempOk == true){
          Display ++;
        }
        else{
          if (t > 15){
            lcd.setCursor(0,0);
            lcd.print("Temp: ALTA!!!!!!"); 
          }
          else{
            lcd.setCursor(0,0);
            lcd.print("Temp: BAIXA!!!!"); 
          }
          lcd.setCursor(0,1);
          lcd.print("Temp: "); 
          lcd.print(t);
          lcd.print(" *C  ");
        }
      }
      //Mostrar a umidade no display
      else if (Display == 1){
        if (UmiOk == true){
            Display ++;
          }
        else{
          if (u > 70){
            lcd.setCursor(0,0);
            lcd.print("Umi: ALTA!!!!!!"); 
          }
          else{
            lcd.setCursor(0,0);
            lcd.print("Umi: BAIXA!!!!!"); 
          }
          lcd.setCursor(0,1);
          lcd.print("Umidade: "); 
          lcd.print(u);
          lcd.println(" %");
        }
      }
      //Mostrar a luminosidade
      else if (Display == 2){
          if (LuzOk == true){
            Display = 0;
          }
        else{
          lcd.setCursor(0,0);
          lcd.print("Ambiente muito"); 
          lcd.setCursor(0,1);
          lcd.print("CLARO!!"); 
        }
      }
    } 
  //Ligar LEDs certos dependo da situacao
    if (TempOk == true && (UmiOk == false || LuzOk == false)){
      digitalWrite(LedR, 1);
      digitalWrite(LedY, 0);
      digitalWrite(LedG, 0);
    }
    else if (TempOk == false && (UmiOk == false || LuzOk == false)){
      digitalWrite(LedR, 1);
      digitalWrite(LedY, 1);
      digitalWrite(LedG, 0);
    }
    else if (TempOk == false && UmiOk == true && LuzOk == true){
      digitalWrite(LedR, 0);
      digitalWrite(LedY, 1);
      digitalWrite(LedG, 0);
    }
    else if (TempOk == true && UmiOk == true && LuzOk == true){
      if (lux > 1){
      digitalWrite(LedR, 0);
      digitalWrite(LedY, 1);
      digitalWrite(LedG, 0);
      }
      else{
      digitalWrite(LedR, 0);
      digitalWrite(LedY, 0);
      digitalWrite(LedG, 1);
      }
    }
  //Buzzer ligado se algo estiver fora do padrao
    if (TempOk == false || UmiOk == false || LuzOk == false){
      if (instance % 2 == 0){
        digitalWrite(Buzzer, HIGH);
      }
      else{
        digitalWrite(Buzzer, LOW);
      }
    }
    else{
      digitalWrite(Buzzer, LOW);
    }
}  
