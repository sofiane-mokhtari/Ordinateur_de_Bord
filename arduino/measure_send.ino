TRIGGER_PIN = 3;
ECHO_PIN = 2;

void setup() {
   
  Serial.begin(9600);
  pinMode(TRIGGER_PIN, OUTPUT);
  digitalWrite(TRIGGER_PIN, LOW);
  pinMode(ECHO_PIN, INPUT);
}
 
void loop() {
  
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  long measure = pulseIn(ECHO_PIN, HIGH);
  float distance_mm = measure / 2.0 * 340.0 / 1000;
  Serial.println(distance_mm / 10.0, 2);
  delay(500);
}
