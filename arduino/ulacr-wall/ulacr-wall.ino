#include <LiquidCrystal_I2C.h> 
#include <Wire.h> 
#define TRIGGER_PIN2 9
#define PWM_OUTPUT_PIN2 8

#define TRIGGER_PIN 11
#define PWM_OUTPUT_PIN 10
LiquidCrystal_I2C lcd(0x27,16,2); 
byte hdr2, data_h2, data_l2, chksum2;
unsigned int distance2;
byte hdr, data_h, data_l, chksum;
unsigned int distance1;
long duration;
long duration2;
float distance;
float distance3;
int imunum=0;
int m1=HIGH;
int m2=HIGH;
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
float imu=0;
float oldimu=0;
int point =0;
union data{  //定義共用結構體
  float Yaw;
  byte Yaw_byte[4];
};
data UNION_YAW;

void setup() {
lcd.init(); //初始化LCD 
lcd.backlight(); //開啟背光
lcd.print("Hello, World!"); //顯示Hello, World!
Serial3.begin(9600);
Serial2.begin(9600);
Serial.begin(9600);
Serial1.begin(9600);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(PWM_OUTPUT_PIN, INPUT);
    pinMode(TRIGGER_PIN2, OUTPUT);
  pinMode(PWM_OUTPUT_PIN2, INPUT);
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
void controlmove(){
if(rlefti<=1250 and rforwardi<=1250){//左前
digitalWrite(53,HIGH);
digitalWrite(51,HIGH);
digitalWrite(49,HIGH);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,HIGH);
digitalWrite(40,HIGH);
digitalWrite(38,HIGH);
digitalWrite(36,HIGH);
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
else if(rlefti >= 1750 and rforwardi<=1250){
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
digitalWrite(52,HIGH);
digitalWrite(50,HIGH);
digitalWrite(48,HIGH);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,LOW);
digitalWrite(41,HIGH);
digitalWrite(39,HIGH);
digitalWrite(37,HIGH);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,LOW);
  }
else if(rlefti <=1250 and rforwardi >=1750){

 digitalWrite(53,HIGH);
digitalWrite(51,HIGH);
digitalWrite(49,HIGH);
digitalWrite(47,HIGH);
digitalWrite(45,HIGH);
digitalWrite(43,LOW);
digitalWrite(40,HIGH);
digitalWrite(38,HIGH);
digitalWrite(36,HIGH);
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
else if(rlefti>= 1750 and rforwardi >=1750){
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
digitalWrite(52,HIGH);
digitalWrite(50,HIGH);
digitalWrite(48,HIGH);
digitalWrite(46,HIGH);
digitalWrite(44,HIGH);
digitalWrite(42,HIGH);
digitalWrite(41,HIGH);
digitalWrite(39,HIGH);
digitalWrite(37,HIGH);
digitalWrite(35,HIGH);
digitalWrite(33,HIGH);
digitalWrite(31,HIGH);
 }
else if(rlefttopi <=1200 and rleft2i<=1350){
  leftdown();}
else if(rlefttopi <=1200 and rleft2i>=1650){
  rightdown();}
else if(rlefttopi>=1700 and rleft2i<=1350){
  lefttop();}
else if(rlefttopi>=1700 and rleft2i>=1650){
  righttop();}
else if(rforwardi<=1250){
  forward();}
else if(rforwardi>=1650){
  back();}
else if(rlefti<=1350){
  left();}
else if(rlefti>=1650){
  right();}
else if(rleft2i<=1350){
  left2();}
else if(rleft2i>=1650){
  right2();}
else{
  stop1();
  }
}
void readimu(){
  while (Serial2.available()){  //清緩存
    Serial2.read();
  }
  while (Serial2.read() != 'Y');  //讀到起始頭才跳出迴圈
  for(byte n=0;n<4;n++){
    while (!Serial2.available());  //等待資料送入才跳出迴圈
    UNION_YAW.Yaw_byte[n] = Serial2.read();
  }
  
  
  if (point==0){
    lcd.setCursor(0, 0);
    lcd.print(UNION_YAW.Yaw);
    
    imu=UNION_YAW.Yaw-oldimu;
  if(imu<0.02){
    imunum=imunum+1;
    if(imunum>100){
      point=1;
      }
    }
  else{
    imunum=0;
    }
   oldimu= UNION_YAW.Yaw;
    }
   else{
   UNION_YAW.Yaw=UNION_YAW.Yaw-oldimu;
   UNION_YAW.Yaw=UNION_YAW.Yaw+360;
   Serial.print(oldimu);
   Serial.print(UNION_YAW.Yaw);
   lcd.setCursor(0, 0);
    lcd.print(UNION_YAW.Yaw);
    }
   

   
  

  

  }
void readpwmul2(){
   digitalWrite(TRIGGER_PIN2, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN2, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN2, LOW);

  pinMode(PWM_OUTPUT_PIN2, INPUT);
  duration2 = pulseIn(PWM_OUTPUT_PIN2, HIGH);

  distance3 = duration2;
  distance3 = distance3 / 58;
  Serial.print("  ");
  Serial.print(distance3);
  Serial.print(" cm2 ");

  }
void readpwmul(){
   digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(100);
  digitalWrite(TRIGGER_PIN, LOW);

  pinMode(PWM_OUTPUT_PIN, INPUT);
  duration = pulseIn(PWM_OUTPUT_PIN, HIGH);

  distance = duration;
  distance = distance / 58;
  Serial.print("  ");
  Serial.print(distance);
  Serial.print(" cm ");

  }
void readuaul1(){
  Serial1.write("xxxxx");
  while (Serial1.available()){
hdr = (byte) Serial1.read();
    if (hdr == 255)
    {
      data_h = (byte) Serial1.read();
      data_l = (byte) Serial1.read();
      chksum = (byte) Serial1.read();

      if (chksum == ((hdr + data_h + data_l)&0x00FF))
      {
        distance1 = data_h * 256 + data_l;

        Serial.print(distance1, DEC);
        Serial.println(" mm ");  
  }
    }}}
void readuaul2(){
  Serial3.write("xxxxx");
     while (Serial3.available()){
     
 
    hdr2 = (byte) Serial3.read();
    if (hdr2 == 255)
    {
      data_h2 = (byte) Serial3.read();
      data_l2 = (byte) Serial3.read();
      chksum2 = (byte) Serial3.read();

      if (chksum2 == ((hdr2 + data_h2 + data_l2)&0x00FF))
      {
        distance2 = data_h2 * 256 + data_l2;

        Serial.print(distance2, DEC);
        Serial.print(" mmmmm");
      
    }
  }

  }}





  
void loop() {
readimu();
readpwmul();
readpwmul2();
readuaul2();
readuaul1();
//readpaluse();  
//controlrace();
//controlmove();
if(point==0){
  stop1();
  lcd.setCursor(0, 1);
  lcd.print("stop");
  }
else if(UNION_YAW.Yaw>363){
  right();
  lcd.setCursor(0, 1);
  lcd.print("right");}
else if(UNION_YAW.Yaw<=357){
  left();
  lcd.setCursor(0, 1);
  lcd.print("left");}
else if(distance1<=300 and distance1 != 0 and distance2<250  and distance2 != 0){
  while(true){  readimu();
readpwmul();
readpwmul2();
readuaul2();
readuaul1();
right2();
lcd.setCursor(0, 1);
  lcd.print("left2");
if(distance2>=250){
break;}}


  }
else if(distance1<=300 and distance1 !=0){
  right2();
  lcd.setCursor(0, 1);
  lcd.print("left2");}
else if(distance<27 and distance != 0){
  left2();
  lcd.setCursor(0, 1);
  lcd.print("right2");
  }
else if(distance2<250 and distance2 != 0){
  left2();
  lcd.setCursor(0, 1);
  lcd.print("right2");}
else if(distance3<27 and distance3 != 0){
  right2();
  lcd.setCursor(0, 1);
  lcd.print("left2");}
else{
  forward();
  lcd.setCursor(0, 1);
  lcd.print("forward");}
delay(10);


}
