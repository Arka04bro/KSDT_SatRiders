const int mqPin = A0;     
const float R0 = 10.0;   
const float RL = 10.0;   
void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(mqPin);
  float V = sensorValue * (5.0 / 1023.0);
  float RS = (5.0 - V) / V * RL;
  float ratio = RS / R0;
  float ppm = 116.6020682 * pow(ratio, -2.769034857);
  Serial.print("PPM: ");
  Serial.println(ppm);
  delay(1000);
}
