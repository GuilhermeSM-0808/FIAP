int VGL = 13; // Vehicle Green Led
int VYL = 12; // Vehicle Yellow Led
int VRL = 11; // Vehicle Red Led

int PGL = 9; // Pedestrian Green Led
int PRL = 8; // Pedestrian Red Led

int Button = 2; // Button Input

void setup() {

  pinMode(VGL,OUTPUT);
  pinMode(VYL,OUTPUT);
  pinMode(VRL,OUTPUT);
  pinMode(PGL,OUTPUT);
  pinMode(PRL,OUTPUT);
  pinMode(Button,INPUT);
}

void loop() {
  if ( digitalRead(2) == 1){
    digitalWrite(VRL,1);
    digitalWrite(VYL,0);
    digitlaWrite(VGL,0);
    digitalWrite(PRL,0);
    digitalWrite(PGL,1);
    delay(6000);
  }
  else {
    //Vermelho pedestre
    digitalWrite(PRL,1);
    digitalWrite(PGL,0);
    

  }
}
