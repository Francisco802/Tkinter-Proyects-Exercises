#include <SoftwareSerial.h>
#define rxPin 3
#define txPin 2

#define E0 10
#define E1 11

SoftwareSerial mySerial(rxPin, txPin);

//  Para los comandos
String inputString = "";
bool stringComplete = false;

//  Variables
int s0, s1;
int J[5];
int cks = 0;
byte data[8];

//  Funciones
void joints();
void opcion();
void processCommand();


void setup()
{
  Serial.begin(9600);
  mySerial.begin(2400);

  pinMode(E0,OUTPUT);
  pinMode(E1,OUTPUT);

  for(int i=0;i<5;i++){
    J[i]=128;
  }
  joints(128, J[1], J[2], J[3], J[4], 0, 0);

  delay(1000);
  Serial.println("Listo...");
}

void loop()
{
  if (stringComplete)
  {
    inputString.trim();

    //Procesar las opciones
    processCommand();

    inputString = "";
    stringComplete = false;
  }
}

void processCommand() {
  opcion();

  int h = -1;
  if (inputString.indexOf("J0") != -1) h = 0;
  if (inputString.indexOf("J1") != -1) h = 1;
  if (inputString.indexOf("J2") != -1) h = 2;
  if (inputString.indexOf("J3") != -1) h = 3;
  if (inputString.indexOf("J4") != -1) h = 4;

  if (h != -1) {
    String valueStr = inputString.substring(2);
    J[h] = valueStr.toInt();
  }

  joints(47, J[1], J[2], J[3], J[4], 0, 0);
  
}

void serialEvent() {
  //Lectura de datos serial
  while (Serial.available())
  {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    }
    else {
      inputString += inChar;
    }
  }
}

void joints(int D1, int D2, int D3, int D4, int D5, int s0, int s1) {
  //Funcion comunicacion con el robot
  if (s0 == 0 && s1 == 0) {D4 = 128; D5 = 128;}
  if (s0 == 0 && s1 == 1) {D5 = 128;}

  cks = (260 + D1 + D2 + D3 + D4 + D5) % 255;
  data[0]=255;
  data[1]=5;
  data[2]=D1;
  data[3]=D2;
  data[4]=D3;
  data[5]=D4;
  data[6]=D5;
  data[7]=cks;
  
  mySerial.write(data,8);
}

void opcion(){
  //Seleccion de extremidad que se movera
    if (inputString.indexOf("$O") != -1) {
      String CMD = inputString.substring(2);
      if(CMD=="BD"){s0=0; s1=0;}
      if(CMD=="PI"){s0=0; s1=1;}
      if(CMD=="BI"){s0=1; s1=0;}
      if(CMD=="PD"){s0=1; s1=1;}  
    } 
    digitalWrite(E0,s0);
    digitalWrite(E1,s1);
}

