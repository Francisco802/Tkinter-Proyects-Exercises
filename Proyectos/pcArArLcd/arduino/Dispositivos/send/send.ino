#include <SoftwareSerial.h>
#define rxPin 3
#define txPin 2

SoftwareSerial auxSerial(rxPin, txPin);

String inputString = "";
bool stringComplete = false;

unsigned long tiempoOne=0;

int led = 5;
int pot1= A0;
int pot2= A1;

void setup() {
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


}

void processCommand() {

  auxSerial.println(inputString);
  
  if(inputString == "#on"){
    digitalWrite(led,HIGH);
  }
  if(inputString == "#off"){
    digitalWrite(led,LOW);
  }

}

//
//  Funcion para enviar datos. Sensores
//
void serialSend(){

  if(millis() - tiempoOne > 200){
    tiempoOne= millis();

    int valor1 = analogRead(pot1);
    int valor2 = analogRead(pot2);

    valor1 = map(valor1,0,1024,0,100);
    valor2 = map(valor2,0,1024,0,100);

    Serial.println(
      (String)valor1+","+
      (String)valor2
    );
  }

}

//
//  Funcion para leer datos.
//
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}