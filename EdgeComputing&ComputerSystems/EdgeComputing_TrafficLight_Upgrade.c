int VRL = 13; // Vehicle Red Light
int VYL = 12; // Vehicle Yellow Light
int VGL = 11; // Vehicle Green Light
int PGL = 10; // Pedestrian Green Light
int PRL = 9; // Pedestrian Red Light
int B = 2; // Button
bool x = false;

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
  delay(1500);
  // Check if button is being pressed
  if ( digitalRead(B) == 1) {
    x = true; 
  }
  // Vehicle Yellow Light
  digitalWrite(VRL, 0);
  digitalWrite(VYL, 1);
  digitalWrite(VGL, 0);
  delay(500);
  // Check if button is being pressed
  if ( digitalRead(B) == 1) { 
    x = true; 
  }
  // Vehicle Red Light
  // If button was NOT pressed then proceed as normal
  if (x == false) {
    digitalWrite(VRL, 1);
    digitalWrite(VYL, 0);
    digitalWrite(VGL, 0);
    delay(2000);
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
  // Check if button is being pressed
  if ( digitalRead(B) == 1) {
    x = true; 
  }
}