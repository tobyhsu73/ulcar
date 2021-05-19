

byte hdr, data_h, data_l, chksum;
unsigned int distance;

void setup()
{ Serial.begin(9600);
  Serial1.begin(9600);


}

void loop()
{  Serial.flush();
   Serial1.flush();
 
    hdr = (byte) Serial1.read();
    if (hdr == 255)
    {
      data_h = (byte) Serial1.read();
      data_l = (byte) Serial1.read();
      chksum = (byte) Serial1.read();

      if (chksum == ((hdr + data_h + data_l)&0x00FF))
      {
        distance = data_h * 256 + data_l;

        Serial.print(distance, DEC);
        Serial.println(" mm");
      
    }
  }
delay(100);
}
