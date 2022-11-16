

#include "DHT.h"// Library for dht22
#define DHTPIN 15     // what pin we're connected to
#define DHTTYPE DHT22   // define type of sensor DHT 22
float h, t;


DHT dht (DHTPIN, DHTTYPE);
 
void setup(){
  Serial.begin(115200);                                             
  dht.begin();
  delay(500);                                                    
}
 
void loop(){
 
     h = dht.readHumidity();
     t = dht.readTemperature();
    
    //Send Humidity status to Python Code
    Serial.print("Current humidity = ");
    Serial.print(h);
    Serial.print("%  ");

    //Send Temperature status to Python Code
    Serial.print("temperature = ");
    Serial.print(t); 
    Serial.println("C  ");
    
    delay(1000);                                                  
}
