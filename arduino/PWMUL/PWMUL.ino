/**
 * 
 * Author: Ritesh Talreja, Made in China, Warehouse: Shenzhen, Guangdong.
 * 
 * Components: Arduino UNO, DYPA02YYWM  v1.0
 * 
 * Arduino UNO +5V    --> DYPA02YYUM Pin 1 Red
 * Arduino UNO GND    --> DYPA02YYUM Pin 2 Black
 * Arduino UNO Pin 11 --> DYPA02YYUM Pin 3
 * Arduino UNO Pin 10 --> DYPA02YYUM Pin 4
 * 
 */

#define TRIGGER_PIN 22
#define PWM_OUTPUT_PIN 24
#define TRIGGER_PIN1 30
#define PWM_OUTPUT_PIN1 32
#define TRIGGER_PIN2 28
#define PWM_OUTPUT_PIN2 26
#define TRIGGER_PIN3 25
#define PWM_OUTPUT_PIN3 23
#define TRIGGER_PIN4 29
#define PWM_OUTPUT_PIN4 27
#define TRIGGER_PIN5 31
#define PWM_OUTPUT_PIN5 33
long duration;
int distance;
long duration1;
int distance1;
long duration2;
long duration3;
int distance2;
int distance3;
int distance4;
long duration4;
int distance5;
long duration5;
void setup()
{
  Serial.begin(57600);
  while (!Serial);
  pinMode(TRIGGER_PIN1, OUTPUT);
  pinMode(PWM_OUTPUT_PIN1, INPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(PWM_OUTPUT_PIN, INPUT);
  pinMode(TRIGGER_PIN2, OUTPUT);
  pinMode(PWM_OUTPUT_PIN2, INPUT);
  pinMode(TRIGGER_PIN3, OUTPUT);
  pinMode(PWM_OUTPUT_PIN3, INPUT);
  pinMode(TRIGGER_PIN4, OUTPUT);
  pinMode(PWM_OUTPUT_PIN4, INPUT);
  pinMode(TRIGGER_PIN5, OUTPUT);
  pinMode(PWM_OUTPUT_PIN5, INPUT);  
}

void loop()
{
  // The sensor is triggered by a falling edge of a HIGH pulse that 
  // is more than 60 microseconds in duration.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN, LOW);
   pinMode(PWM_OUTPUT_PIN, INPUT);
  duration = pulseIn(PWM_OUTPUT_PIN, HIGH);
  distance = duration;
  distance = distance / 58;
  Serial.print("lf");
    if(distance<0){
    distance=0;
    } 
  if (distance<10){
    Serial.print("00");}
  else if(distance<100){
    Serial.print(0);}
  Serial.print(distance);
  delay(5);
  
  digitalWrite(TRIGGER_PIN1, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN1, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN1, LOW);
   pinMode(PWM_OUTPUT_PIN1, INPUT);
  duration1 = pulseIn(PWM_OUTPUT_PIN1, HIGH);
  distance1 = duration1;
  distance1 = distance1 / 58;
  Serial.print("mf");
    if(distance1<0){
    distance1=0;
    }
   if (distance1<10){
    Serial.print("00");}
  else if(distance1<100){
    Serial.print(0);}  
  Serial.print(distance1);
  
  delay(5);

   digitalWrite(TRIGGER_PIN2, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN2, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN2, LOW);
   pinMode(PWM_OUTPUT_PIN2, INPUT);
  duration2 = pulseIn(PWM_OUTPUT_PIN2, HIGH);
  distance2 = duration2;
  distance2 = distance2 / 58; 
  Serial.print("rf");
  if(distance2<0){
    distance2=0;
    }
  else if (distance2<10){
    Serial.print("00");}
  else if(distance2<100){
    Serial.print(0);} 
  Serial.print(distance2);
  
  delay(5); 

  digitalWrite(TRIGGER_PIN3, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN3, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN3, LOW);
  pinMode(PWM_OUTPUT_PIN3, INPUT);
  duration3 = pulseIn(PWM_OUTPUT_PIN3, HIGH);
  distance3 = duration3;
  distance3 = distance3 / 58; 
  Serial.print("ll");
  if(distance3<0){
    distance3=0;
    }
  else if (distance3<10){
    Serial.print("00");}
  else if(distance3<100){
    Serial.print(0);} 
  Serial.print(distance3);
  
  delay(5);

  digitalWrite(TRIGGER_PIN4, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN4, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN4, LOW);
  pinMode(PWM_OUTPUT_PIN4, INPUT);
  duration4 = pulseIn(PWM_OUTPUT_PIN4, HIGH);
  distance4 = duration4;
  distance4 = distance4 / 58; 
  Serial.print("rr");
  if(distance4<0){
    distance4=0;
    }
  else if (distance4<10){
    Serial.print("00");}
  else if(distance4<100){
    Serial.print(0);} 
  Serial.print(distance4);
  
  delay(5);

  digitalWrite(TRIGGER_PIN5, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN5, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN5, LOW);
  pinMode(PWM_OUTPUT_PIN5, INPUT);
  duration5 = pulseIn(PWM_OUTPUT_PIN5, HIGH);
  distance5 = duration5;
  distance5 = distance5 / 58; 
  Serial.print("bb");
  if(distance5<0){
    distance5=0;
    }
  else if (distance5<10){
    Serial.print("00");}
  else if(distance5<100){
    Serial.print(0);} 
  Serial.println(distance5);
  
  delay(5);
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  // If no object detected, fixed pulse width of 35ms is sent
  // by the sensor.

 
  // Convert the pulse width duration into a distance

  

}
