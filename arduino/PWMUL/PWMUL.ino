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

#define TRIGGER_PIN 34
#define PWM_OUTPUT_PIN 36
#define TRIGGER_PIN1 44
#define PWM_OUTPUT_PIN1 45
#define TRIGGER_PIN2 40
#define PWM_OUTPUT_PIN2 38
#define TRIGGER_PIN3 37
#define PWM_OUTPUT_PIN3 35
#define TRIGGER_PIN4 41
#define PWM_OUTPUT_PIN4 39
#define TRIGGER_PIN5 43
#define PWM_OUTPUT_PIN5 42
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

int rforward = 23;
int rleft = 25;
int rleft2 = 22;
int rlefttop = 24;
int rfastrace =26;
int rslowrace = 27;
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
pinMode(22,INPUT);
pinMode(23,INPUT);
pinMode(24,INPUT);
pinMode(25,INPUT);
pinMode(26,INPUT);
pinMode(27,INPUT);  
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
  Serial.print(distance5);
  
  delay(5);
int rleft2i=pulseIn(rleft2,HIGH,60000);
int rforwardi=pulseIn(rforward,HIGH,60000);
int rlefttopi=pulseIn(rlefttop,HIGH,60000);
int rlefti=pulseIn(rleft,HIGH,60000);
int rfastracei=pulseIn(rfastrace,HIGH,60000);
int rslowracei=pulseIn(rslowrace,HIGH,60000);
if(rslowracei <=1350){
  Serial.print('h');

  if(rfastracei <=1350){
    Serial.print('s');
    }
  else if(1450<= rfastracei and rfastracei<=1550){
    Serial.print('m');}
  else if(rfastracei >=1650){
    Serial.print('f');}


    
  if(rlefti<=1250 and rforwardi<=1250){
    Serial.println("lf");}
  else if(rlefti >= 1750 and rforwardi<=1250){
    Serial.println("rf");}
  else if(rlefti <=1250 and rforwardi >=1750){
    Serial.println("lb");}
  else if(rlefti>= 1750 and rforwardi >=1750){
    Serial.println("rb");}
  else if(rlefttopi <=1200 and rleft2i<=1350){
    Serial.println("ld");}
  else if(rlefttopi <=1200 and rleft2i>=1650){
    Serial.println("rd");}
  else if(rlefttopi>=1700 and rleft2i<=1350){
    Serial.println("lt");}
  else if(rlefttopi>=1700 and rleft2i>=1650){
    Serial.println("rt");} 
  else if(rforwardi<=1250){
    Serial.println("ff");}
  else if(rforwardi>=1650){
    Serial.println("bb");}
  else if(rlefti<=1350){
    Serial.println("ll");}
  else if(rlefti>=1650){
    Serial.println("rr");}
  else if(rleft2i<=1350){
    Serial.println("lt");}
  else if(rleft2i>=1650){
    Serial.println("rt");}
  else{
    Serial.println("st");}
   }

else if(rslowracei>=1650){
  Serial.println('u');}
}
