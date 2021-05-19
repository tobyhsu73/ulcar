
union data{  //定義共用結構體
  float Yaw;
  byte Yaw_byte[4];
};
data UNION_YAW;  //幫結構體命名

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial2.begin(9600);
  delay(500);
  while (Serial2.available()){
    Serial2.read();
  }
  Serial.print("開始");
}

void loop() {

  while (Serial2.available()){  //清緩存
    Serial2.read();
  }
  while (Serial2.read() != 'Y');  //讀到起始頭才跳出迴圈
  for(byte n=0;n<4;n++){
    while (!Serial2.available());  //等待資料送入才跳出迴圈
    UNION_YAW.Yaw_byte[n] = Serial2.read();
  }
  Serial.println(UNION_YAW.Yaw);

  
  delay(100);
}
