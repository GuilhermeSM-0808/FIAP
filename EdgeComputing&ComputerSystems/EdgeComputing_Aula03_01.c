//Arduino UNO 

int LedPort = 10;

void setup() {
  // put your setup code here, to run once:
pinMode(LedPort,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
for (int x = 0; x < 3; x++){
  digitalWrite(LedPort,HIGH);
  delay(500);
  digitalWrite(LedPort,LOW);
  delay(500);
}
for (int y = 0; y < 2; y++){
  digitalWrite(LedPort, HIGH);
  delay(1500);
  digitalWrite(LedPort, LOW);
  delay(500);
}
}
