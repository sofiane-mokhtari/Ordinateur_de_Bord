

void setup() {
   
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  digitalWrite(3, LOW);
  pinMode(2, INPUT);
}
 
void loop() {
  
  digitalWrite(3, HIGH);
  delayMicroseconds(10);
  digitalWrite(3, LOW);
  int i = 0;
  long measure = pulseIn(2, HIGH);
  int distance_mm = measure / 2 * 340 / 1000;
  int d = round(distance_mm / 10);
  if (d < 10)
  {
    if (i != 0)
      Serial.println('0');
      i = 0;
  }
  else if (d < 20)
  {
    if (i != 1)
      Serial.println('1');
      i = 1;
  }
  else if (d < 30)
  {
    if (i != 2)
      Serial.println('2');
    i = 2;
  }
  else if (d < 40)
  {
    if (i != 3)
     Serial.println('3');
    i = 3;
  }
  else if (d < 50)
  {
    if (i != 4)
      Serial.println('4');
      i = 4;
  }
  else
  {
    if (i != 5)
      Serial.println('5');
      i = 5;
  }
}
