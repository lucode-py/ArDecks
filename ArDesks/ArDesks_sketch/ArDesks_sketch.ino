//YWROBOT
//Compatible with the Arduino IDE 1.0
//Library version:1.1
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <DHT.h>;

#define DHT11_PIN 2
#define DHTTYPE DHT11
DHT dht(DHT11_PIN, DHTTYPE);

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display

int temp;

void setup()
{

  lcd.init();                      // initialize the lcd 
  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();
  affichResult();

  Serial.begin(9600);
  dht.begin();
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);

}


void affichResult(){
    lcd.setCursor(0,0);
    lcd.print("Tempe:      ");
    lcd.setCursor(7,0);
    temp = dht.readTemperature();
    //Serial.println(temp);
    lcd.print(temp);

}

void loop()
{
  int valBut1 = digitalRead(8);
  //Serial.println(valBut1);
  int valBut2 = digitalRead(9);
  //Serial.println(valBut2);



  if (valBut1 == LOW) {
    Serial.println("S1");
    delay(100);
  }else if (valBut2 == LOW) {
    Serial.println("S2");
    delay(100);
  
  }
  affichResult();
}
