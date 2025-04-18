
// https://wokwi.com/projects/427074113905735681


//I/O setup
int VRL1 = 13; // Vehicle Red Light 1
int VYL1 = 12; // Vehicle Yellow Light 1
int VGL1 = 11; // Vehicle Green Light 1
int VRL2 = 8; // Vehicle Red Light 2
int VYL2 = 7; // Vehicle Yellow Light 2
int VGL2 = 6; // Vehicle Green Light 2
int PGL = 10; // Pedestrian Green Light
int PRL = 9; // Pedestrian Red Light
int B = 2; // Button 
int pin; // Setup variable

void setup() {
  for (pin = 13; pin >= 6; pin--) {
    pinMode(pin, OUTPUT);
  }
pinMode(B, INPUT);
}
//Constants
// Button press bool
bool x = false;
// t int for timer delay
int t;
// Delay length in ms
  int d = 10;
  // Delays (multiplied by delay length)
    //main delay
    int m1 = 400; // Main road delay time
    int m2 = 250; // Side road delay time
    //switch delay
    int s = 80;
// Pedestrian crossing amount in ms
  int p = 6000;
  int e = 1000;


void loop() {
//Traffic Light Cycle
digitalWrite(PRL, 1);
digitalWrite(PGL, 0);
// MAIN
  // Vehicle Green Light 1
  digitalWrite(VRL1, 0);
  digitalWrite(VYL1, 0);
  digitalWrite(VGL1, 1);
  // Vehicle Red Light 2
  digitalWrite(VRL2, 1);
  digitalWrite(VYL2, 0);
  digitalWrite(VGL2, 0);
  for (t = 0; t < m1; t++) {
    delay(d);
    // Check if button is being pressed
    if ( digitalRead(B) == 1 && x == false) {
      x = true; 
    }
  }
// SWITCHING
  // Vehicle Yellow Light 1
  digitalWrite(VRL1, 0);
  digitalWrite(VYL1, 1);
  digitalWrite(VGL1, 0);
  // Vehicle Red Light 2
  digitalWrite(VRL2, 1);
  digitalWrite(VYL2, 0);
  digitalWrite(VGL2, 0);
  for (t = 0; t < s; t++) {
    delay(d);
    // Check if button is being pressed
    if ( digitalRead(B) == 1 && x == false) {
      x = true; 
    }
  }
// If button WAS pressed, then add extra Red light delay for vehicles and open green crossing light for pedestrians 
  if (x == true) {
    //Vehicle Red Light 1
    digitalWrite(VRL1, 1);
    digitalWrite(VYL1, 0);
    digitalWrite(VGL1, 0);
    //Vehicle Red Light 2
    digitalWrite(VRL2, 1);
    digitalWrite(VYL2, 0);
    digitalWrite(VGL2, 0);
    //Pedestrian Green Light
    digitalWrite(PRL, 0); 
    digitalWrite(PGL, 1);
    delay(p);
    // Close Pedestrian Traffic Light
    digitalWrite(PRL, 1);
    digitalWrite(PGL, 0);
    delay(e);
    x = false;
  }
  else {
    //Vehicle Red Light 1
    digitalWrite(VRL1, 1);
    digitalWrite(VYL1, 0);
    digitalWrite(VGL1, 0);
    //Vehicle Red Light 2
    digitalWrite(VRL2, 1);
    digitalWrite(VYL2, 0);
    digitalWrite(VGL2, 0);
      for (t = 0; t < s; t++) {
      delay(d);
      // Check if button is being pressed
      if ( digitalRead(B) == 1 && x == false) {
        x = true; 
      }
    }
  }
// MAIN
  // Vehicle Red Light 1
  digitalWrite(VRL1, 1);
  digitalWrite(VYL1, 0);
  digitalWrite(VGL1, 0);
  // Vehicle Green Light 2
  digitalWrite(VRL2, 0);
  digitalWrite(VYL2, 0);
  digitalWrite(VGL2, 1);
  // Check if button is being pressed
  for (t = 0; t < m2; t++) {
    delay(d);
    // Check if button is being pressed
    if ( digitalRead(B) == 1 && x == false) {
      x = true; 
    }
  }
// SWITCHING  
  // Vehicle Red Light 1
  digitalWrite(VRL1, 1);
  digitalWrite(VYL1, 0);
  digitalWrite(VGL1, 0);
  // Vehicle Yellow Light 2
  digitalWrite(VRL2, 0);
  digitalWrite(VYL2, 1);
  digitalWrite(VGL2, 0);
  for (t = 1; t < s; t++) {
    delay(d);
    // Check if button is being pressed
    if ( digitalRead(B) == 1 && x == false) {
      x = true; 
    }
  }
// If button WAS pressed, then add extra Red light delay for vehicles and open green crossing light for pedestrians 
  if (x == true) {
    //Vehicle Red Light 1
    digitalWrite(VRL1, 1);
    digitalWrite(VYL1, 0);
    digitalWrite(VGL1, 0);
    //Vehicle Red Light 2
    digitalWrite(VRL2, 1);
    digitalWrite(VYL2, 0);
    digitalWrite(VGL2, 0);
    //Pedestrian Green Light
    digitalWrite(PRL, 0); 
    digitalWrite(PGL, 1);
    delay(p);
        // Close Pedestrian Traffic Light
    digitalWrite(PRL, 1);
    digitalWrite(PGL, 0);
    delay(e);
    x = false;
  }
  else {
    //Vehicle Red Light 1
    digitalWrite(VRL1, 1);
    digitalWrite(VYL1, 0);
    digitalWrite(VGL1, 0);
    //Vehicle Red Light 2
    digitalWrite(VRL2, 1);
    digitalWrite(VYL2, 0);
    digitalWrite(VGL2, 0);
      for (t = 0; t < s; t++) {
      delay(d);
      // Check if button is being pressed
      if ( digitalRead(B) == 1 && x == false) {
        x = true; 
      }
    }
  }
}