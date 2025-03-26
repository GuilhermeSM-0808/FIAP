// https://wokwi.com/projects/426505731150547969

int VRL = 13; // Vehicle Red Light
int VYL = 12; // Vehicle Yellow Light
int VGL = 11; // Vehicle Green Light
int PGL = 10; // Pedestrian Green Light
int PRL = 9; // Pedestrian Red Light
int B = 2; // Button
bool x = false;
int t;

void setup() {
  pinMode(VRL, OUTPUT);
  pinMode(VYL, OUTPUT);
  pinMode(VGL, OUTPUT);
  pinMode(B, INPUT);
  pinMode(PRL, OUTPUT);
  pinMode(PGL, OUTPUT);
}
 
void loop() {
  //Traffic Light Cycle
  // Close Pedestrian Traffic Light
  digitalWrite(PRL, 1);
  digitalWrite(PGL, 0);
  // Vehicle Green Light
  digitalWrite(VRL, 0);
  digitalWrite(VYL, 0);
  digitalWrite(VGL, 1);
  for (t = 0; t < 1499; t++) {
    delay(1);
    // Check if button is being pressed
    if ( digitalRead(B) == 1 && x == false) {
      x = true; 
    }
  }
  // Vehicle Yellow Light
  digitalWrite(VRL, 0);
  digitalWrite(VYL, 1);
  digitalWrite(VGL, 0);
  for (t = 0; t < 499; t++) {
    delay(1);
    // Check if button is being pressed
    if ( digitalRead(B) == 1 && x == false) {
      x = true; 
    }
  }
  // Vehicle Red Light
  // If button was NOT pressed then proceed as normal
  if (x == false) {
    digitalWrite(VRL, 1);
    digitalWrite(VYL, 0);
    digitalWrite(VGL, 0);
  // Check if button is being pressed
    for (t = 0; t < 1999; t++) {
      delay(1);
      // Check if button is being pressed
      if ( digitalRead(B) == 1 && x == false) {
        x = true; 
      }
    }
  }
  // If button WAS pressed, then extend Red light delay for vehicles and open green crossing light for pedestrians 
  else {
    //Vehicle Red Light
    digitalWrite(VRL, 1);
    digitalWrite(VYL, 0);
    digitalWrite(VGL, 0);
    //Pedestrian Green Light
    digitalWrite(PRL, 0); 
    digitalWrite(PGL, 1);
    delay(6000);
    x = false;
  }
}