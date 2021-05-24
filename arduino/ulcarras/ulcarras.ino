#include <OneWire.h>

#include <LiquidCrystal_I2C.h> 
#include <Wire.h> 

#define TRIGGER_PIN2 9
#define PWM_OUTPUT_PIN2 8

#define TRIGGER_PIN 11
#define PWM_OUTPUT_PIN 10
LiquidCrystal_I2C lcd(0x27,16,2);
int f1;
int f2;
byte hdr2, data_h2, data_l2, chksum2;
unsigned int distance2;
byte hdr, data_h, data_l, chksum;
unsigned int distance1;
long duration;
long duration2;
float distance;
float distance3;
int m1=LOW;
int m2=LOW;
int m3=HIGH;
int rforward = 23;
int rleft = 25;
int rleft2 = 22;
int rlefttop = 24;
int rfastrace =26;
int rslowrace = 27;
int rleft2i;
int rforwardi;
int rlefttopi;
int rlefti;
int rfastracei;
int rslowracei;
int num;
int m = 0;


void setup() {


Serial.begin(9600);
  lcd.init(); //初始化LCD 
  lcd.backlight(); //開啟背光

pinMode(24,INPUT);
pinMode(25,INPUT);
pinMode(26,INPUT);
pinMode(27,INPUT);
pinMode(28,INPUT);
pinMode(29,INPUT);


pinMode(53,OUTPUT);
pinMode(51,OUTPUT);
pinMode(49,OUTPUT);
pinMode(47,OUTPUT);
pinMode(45,OUTPUT);
pinMode(43,OUTPUT);

pinMode(40,OUTPUT);
pinMode(38,OUTPUT);
pinMode(36,OUTPUT);
pinMode(34,OUTPUT);
pinMode(32,OUTPUT);
pinMode(30,OUTPUT);

pinMode(52,OUTPUT);
pinMode(50,OUTPUT);
pinMode(48,OUTPUT);
pinMode(46,OUTPUT);
pinMode(44,OUTPUT);
pinMode(42,OUTPUT);

pinMode(41,OUTPUT);
pinMode(39,OUTPUT);
pinMode(37,OUTPUT);
pinMode(35,OUTPUT);
pinMode(33,OUTPUT);
pinMode(31,OUTPUT);
while (Serial2.available()){
    Serial2.read();
  }
}
void forward(){
digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,HIGH);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,HIGH);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,LOW);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,LOW);
  }
void back(){
 digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,LOW);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,LOW);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,HIGH);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,HIGH);
  }
void left(){
digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,LOW);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,LOW);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,LOW);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,LOW);
}
void right(){
 digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,HIGH);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,HIGH);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,HIGH);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,HIGH);}
void right2(){
digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,LOW);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,HIGH);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,LOW);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,HIGH);}
void left2(){
   digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,HIGH);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,LOW);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,HIGH);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,LOW);}
void righttop(){
   digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,HIGH);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,LOW);
digitalWrite(32,LOW);
digitalWrite(30,LOW);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,LOW);
digitalWrite(44,LOW);
digitalWrite(42,LOW);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,LOW);}
void rightdown(){
     digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,LOW);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,LOW);
digitalWrite(32,LOW);
digitalWrite(30,LOW);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,LOW);
digitalWrite(44,LOW);
digitalWrite(42,LOW);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,HIGH);}
void lefttop(){
     digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,LOW);
digitalWrite(45,LOW);
digitalWrite(43,HIGH);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,HIGH);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,LOW);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,LOW);
digitalWrite(33,LOW);
digitalWrite(31,HIGH);}
void leftdown(){
 digitalWrite(53,m1);
digitalWrite(51,m2);
digitalWrite(49,m3);
digitalWrite(47,LOW);
digitalWrite(45,LOW);
digitalWrite(43,HIGH);
digitalWrite(40,m1);
digitalWrite(38,m2);
digitalWrite(36,m3);
digitalWrite(34,HIGH);
digitalWrite(32,HIGH);
digitalWrite(30,LOW);
digitalWrite(52,m1);
digitalWrite(50,m2);
digitalWrite(48,m3);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,HIGH);
digitalWrite(41,m1);
digitalWrite(39,m2);
digitalWrite(37,m3);
digitalWrite(35,LOW);
digitalWrite(33,LOW);
digitalWrite(31,HIGH);}
void stop1(){
  digitalWrite(53,m1);
  digitalWrite(51,m2);
  digitalWrite(49,m3);
  digitalWrite(47,LOW);
  digitalWrite(45,LOW);
  digitalWrite(43,LOW);
  digitalWrite(40,m1);
  digitalWrite(38,m2);
  digitalWrite(36,m3);
  digitalWrite(34,LOW);
  digitalWrite(32,LOW);
  digitalWrite(30,LOW);
  digitalWrite(52,m1);
  digitalWrite(50,m2);
  digitalWrite(48,m3);
  digitalWrite(46,LOW);
  digitalWrite(44,LOW);
  digitalWrite(42,HIGH);
  digitalWrite(41,m1);
  digitalWrite(39,m2);
  digitalWrite(37,m3);
  digitalWrite(35,LOW);
  digitalWrite(33,LOW);
  digitalWrite(31,HIGH);
  }
void readpaluse(){
Serial.flush();
rleft2i=pulseIn(rleft2,HIGH,60000);
rforwardi=pulseIn(rforward,HIGH,60000);
rlefttopi=pulseIn(rlefttop,HIGH,60000);
rlefti=pulseIn(rleft,HIGH,60000);
rfastracei=pulseIn(rfastrace,HIGH,60000);
rslowracei=pulseIn(rslowrace,HIGH,60000);
}
void controlrace(){
if (rfastracei <=1350 and rslowracei <=1350){
  m=0;
  m1=LOW;
  m2=LOW;
  m3=LOW;
  }
else if(rfastracei <=1350 and rslowracei >=1650){
  m=1;
m1=HIGH;
m2=LOW;
m3=LOW;
}
else if(1450<= rfastracei <=1550 and rslowracei <=1350){
  m=2;
  m1=LOW;
  m2=HIGH;
  m3=LOW;}
else if(1450<= rfastracei <=1550 and rslowracei >=1650){
  m=3;
  m1=LOW;
  m2=LOW;
  m3=HIGH;}
else if(rfastracei >=1650 and rslowracei <=1350){
  m=4;
  m1=HIGH;
  m2=LOW;
  m3=HIGH;}
else if(rfastracei >=1650 and rslowracei >=1650){
  m=5;
  m1=LOW;
  m2=HIGH;
  m3=HIGH;}
}

void loop() {
if(Serial.available()){
  lcd.clear();
f1=Serial.read();
if(f1=='s'){
  f2=Serial.read();
  if (f2=='l'){
      lcd.setCursor(0, 0);
      lcd.print("left");
    }
    else if(f2=='r'){
      lcd.setCursor(0, 0);
      lcd.print("right");}}
else if(f1=='f'){
  lcd.setCursor(0, 0);
   lcd.print("foword");} 
else if(f1=='m'){
  f2=Serial.read();
  if(f2=='r'){
   lcd.setCursor(0, 0);
   lcd.print("right2"); }
   else if(f2=='f'){
    lcd.setCursor(0, 0);
   lcd.print("right2");}
   else if(f2=='l'){
    lcd.setCursor(0, 0);
    lcd.print("left2");}}
else{
      lcd.setCursor(0, 0);
    lcd.print("stoppppp");}
  
controlrace();

delay(10);
}

}
