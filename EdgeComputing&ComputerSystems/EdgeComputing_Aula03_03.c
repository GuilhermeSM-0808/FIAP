void setup() {
  // put your setup code here, to run once:
pinMode(13,OUTPUT);
pinMode(12,OUTPUT);
pinMode(11,OUTPUT);
pinMode(10,OUTPUT);
pinMode(9,OUTPUT);
pinMode(8,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (analogRead(A0) < 677){
    digitalWrite(13,1);
    digitalWrite(12,0);
    digitalWrite(11,0);
    digitalWrite(10,0);
    digitalWrite(9,0);
    digitalWrite(8,0);
  }
  if (677 < analogRead(A0) < 1355){
    digitalWrite(13,0);
    digitalWrite(12,1);
    digitalWrite(11,0);
    digitalWrite(10,0);
    digitalWrite(9,0);
    digitalWrite(8,0);
  }
  if (1355 < analogRead(A0) < 2032){
    digitalWrite(13,0);
    digitalWrite(12,0);
    digitalWrite(11,1);
    digitalWrite(10,0);
    digitalWrite(9,0);
    digitalWrite(8,0);
  }
    if (2032 < analogRead(A0) < 2710){
    digitalWrite(13,0);
    digitalWrite(12,0);
    digitalWrite(11,0);
    digitalWrite(10,1);
    digitalWrite(9,0);
    digitalWrite(8,0);
  }
    if (2710 < analogRead(A0) < 3387){
    digitalWrite(13,0);
    digitalWrite(12,0);
    digitalWrite(11,0);
    digitalWrite(10,0);
    digitalWrite(9,1);
    digitalWrite(8,0);
  }
      if (3387 < analogRead(A0)){
    digitalWrite(13,0);
    digitalWrite(12,0);
    digitalWrite(11,0);
    digitalWrite(10,0);
    digitalWrite(9,0);
    digitalWrite(8,1);
  }
}
