#include <LiquidCrystal.h>

LiquidCrystal lcd(6, 7, 8, 9, 10, 11);  
int sensorPin = 0;

void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("Temperature");
}

void loop()
{
  int reading = analogRead(sensorPin);
  float getVoltage = reading * 5.0;
  getVoltage /= 1024.0;
  float tmpC = (getVoltage - 0.5) * 100; 
  
  Serial.print(tmpC);
  
  lcd.setCursor(0, 1); 
  lcd.print(tmpC);
  lcd.print(" Degrees");
  
  delay(10000);
}
