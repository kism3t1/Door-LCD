#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int LED = 13; //Pin LED is attached to
int warnLED = 8;
//int input; //Setup input integer
char msg = ' ';
//int temppin = 0;
//int RED_LED = 6;
//int GREEN_LED = 7;
//int BLUE_LED = 9;

//char myStrings[32] = {' '};

void setup(){
  lcd.begin(16, 2);  //Setup LCD's number of columns and rows
  Serial.begin(9600);  //Start the serial connection
  //pinMode(LED, OUTPUT);   //Setup LED as an output
  lcd.blink();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Booted up");
  lcd.setCursor(0, 1); //Set to second line
  lcd.print("Arduino Powered.");
}

void loop(){
  if (Serial.available()){
    delay(100);
    while (Serial.available()){
    msg = Serial.read();  //Read serial value and set it as input
    Serial.println(msg);  //Print serial value
    if (msg == 'o') {
      digitalWrite(LED, HIGH); 
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Out Of Office");
  } else if (msg == 'i') {
      digitalWrite(LED, LOW);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("ICT Support");
      lcd.setCursor(0, 1); //Set to second line
      lcd.print("Department!");
  } else if (msg == 'p') {    //When raspi is booted it sends 'B'
    lcd.clear();              //over serial and LCD displays....
    lcd.setCursor(0, 0);
    lcd.print("We are all");
    lcd.setCursor(0, 1); //Set to second line
    lcd.print("Down the Pub!");
  } else {

  }
}
    }
  
}

