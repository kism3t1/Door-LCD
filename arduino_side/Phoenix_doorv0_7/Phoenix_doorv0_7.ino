#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
char msg = ' ';

void setup(){
  lcd.begin(16, 2);  //Setup LCD's number of columns and rows
  Serial.begin(9600);  //Start the serial connection
  lcd.blink();
  lcd.clear();
    //Scroll booting message onto screen then stop
  int x = 20;
  while (x > 0){
    lcd.setCursor(20, 0);
    lcd.scrollDisplayLeft();
    lcd.print("Booting up...");
    lcd.setCursor(20, 1); //Set to second line
    lcd.print("Arduino Powered.");
    delay(550);
    x--;
  }
}

void loop(){
  if (Serial.available()){
    delay(100);
    while (Serial.available()){
    msg = Serial.read();  //Read serial value and set it as input
    Serial.println(msg);  //Print serial value
    if (msg == 'o') { 
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(">    Sorry     <");
      lcd.setCursor(0, 1); //Set to second line
      lcd.print(">Out Of Office!<");
  } else if (msg == 'i') {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("> ICT Support  <");
      lcd.setCursor(0, 1); //Set to second line
      lcd.print("> Department!  <");
  } else if (msg == 'y') {    
      lcd.clear();
        //Flash "Come In" for 10 Seconds
      int x = 10;
      while (x > 0){
        lcd.clear();
        delay(300);
        lcd.setCursor(0, 0);
        lcd.print(">  COME IN!!   <");
        delay(700);  //Then default to In message
        x--;
      }
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("> ICT Support  <");
      lcd.setCursor(0, 1); //Set to second line
      lcd.print("> Department!  <");
  } else if (msg == 'm') {    
    lcd.clear();              
    lcd.setCursor(0, 0);
    lcd.print("> Sorry We Are <");
    lcd.setCursor(0, 1); //Set to second line
    lcd.print("> In A Meeting!<");
  } else if (msg == 'f') {    
    lcd.clear();              
    lcd.setCursor(0, 0);
    lcd.print("      0 0      ");
    lcd.setCursor(0, 1); //Set to second line
    lcd.print("---o00o-o00o---");
  } else {

  }
}
    }
  
}

