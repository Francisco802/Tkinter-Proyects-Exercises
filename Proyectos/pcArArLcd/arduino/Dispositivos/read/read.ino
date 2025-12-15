#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>

#define rxPin 3
#define txPin 2

LiquidCrystal_I2C lcd(0x27,16,2);
SoftwareSerial auxSerial(rxPin, txPin);

String inputString = "";
bool stringComplete = false;

unsigned long tiempoOne=0;

int led = 5;
int pot1= A0;
int pot2= A1;

void setupLcd();
void aux_serial();

void setup() {
  setupLcd();
  Serial.begin(9600);
  auxSerial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() {
  if (stringComplete) {
    inputString.trim();

    processCommand();

    inputString = "";
    stringComplete = false;
  }

  aux_serial();
}

void processCommand() {

  lcd.setCursor(0,0);
  lcd.print(inputString);
  delay(1500);
  lcd.clear();
  
  if(inputString == "#on"){
    digitalWrite(led,HIGH);
  }
  if(inputString == "#off"){
    digitalWrite(led,LOW);
  }

}


//
//  Funcion para leer datos.
//
void aux_serial() {
  while (auxSerial.available()) {
    char inChar = (char)auxSerial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}

//
//  LCD setup
//

void setupLcd(){
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Setup: ok");
  delay(1500);
  lcd.clear();
}