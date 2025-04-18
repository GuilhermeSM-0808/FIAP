
// https://wokwi.com/projects/426987903610370049


//Setup
int pin;

void setup() {
  for (pin = 13; pin >= 3; pin--) {
    pinMode(pin, OUTPUT);
  }
pinMode(2, INPUT); // Distance Echo
pinMode(A0, INPUT); // Potentiometer Input
}

//Loop
//Starting variables
  bool direction = false; // false is decreasing
  int x = 13; // starting led
  int d = 100; // delay between leds
  float cl = 2; // chase length

void loop() {
  // measure distance to determine chase length
    digitalWrite(3, 1);
    delayMicroseconds(10);
    digitalWrite(3, 0);

    int duration = pulseIn(2, 1);
    cl = round(( 1 + ((duration / 58) * 0.025 )));
    delay(d);
    
  // alterar delay baseado no A0
    d = ((analogRead(A0) / 5) +25 );
  //Turn on one led and turn another one off before or after depending on direction and which one based on the chase length 
    if (direction == false){
      if (x == 5){
        direction = true;
      }
      digitalWrite(x,1);
      delay(d);
      x--;
      digitalWrite(x,1);
      digitalWrite((x+cl),0);
    }
    else {
        if (x == 12){
        direction = false;
      }
      digitalWrite(x,1);
      delay(d);
      x++;
      digitalWrite(x,1);
      digitalWrite((x-cl),0);    
    }
}