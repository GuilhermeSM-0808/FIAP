void setup() {
pinMode (13, INPUT);
pinMode (10, OUTPUT);
pinMode (9, OUTPUT);
pinMode (8, OUTPUT);
}

int c = 0;

void loop(){
  if (digitalRead(13)==1) {
  (c = 1);
  }
  digitalWrite (8, HIGH);
  delay(5000);
  digitalWrite(8, LOW);
  digitalWrite (9, HIGH);
  delay(1500);
  digitalWrite(9, LOW);
  digitalWrite (10, HIGH);
  delay(3500);
  if (c > 0) {
    delay(3500);
    c = 0;
  }
  digitalWrite(10, LOW);
}
