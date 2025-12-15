#include <SoftwareSerial.h>
#define rxPin 3
#define txPin 2

SoftwareSerial auxSerial(rxPin, txPin);

String inputString = "";
bool stringComplete = false;

String inputString2 = "";
bool stringComplete2 = false;

//
//  Variables de la trama
//
char *adrss = NULL;
String DT[4];

int led = 4;
bool Bandera = false;

String ownAddss="101";
String Destino="";
String txt="";

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

  if (stringComplete2) {
    inputString2.trim();

    processCommand();

    inputString2 = "";
    stringComplete2 = false;
  }


 while (auxSerial.available()) {
    char inChar2 = (char)auxSerial.read();
    if (inChar2 == '\n') {
      stringComplete2 = true;
    } else {
      inputString2 += inChar2;
    }
  }
}

void processCommand() {
  
  // Recibe texto pcToARduino
  if(inputString.indexOf("TX") != -1){

    //
    //  TK, ownAddss, destino, texto,
    //
    //
    txt = inputString.substring(2);
    auxSerial.print("TK,"+ ownAddss + Destino + txt + "\n");
  }

  // Seleccion de destino
  if(inputString=="DE"){
    inputString = inputString.substring(2);
    if(inputString=="101"){
      Destino="101";
    }

    if(inputString=="102"){
      Destino="102";
    }
   
  }

  // Inicializa proceso
  if(inputString=="ST"){
    Bandera = false;
    auxSerial.write("BL00\n");
  }
  
  if(inputString=="BD00"){
      Bandera = true;
    }

  if(inputString2=="BL00"){
    digitalWrite(led,HIGH);
    delay(500);
    digitalWrite(led,LOW);

    if(Bandera != true){
      auxSerial.write("BL00\n");
    }
  }

  if(inputString2.indexOf("TK") != -1){
    String inputString2_Copy = inputString2;
    inputString = inputString.substring(3);
    separador();

    String Origen=DT[0];      // Quien o manda
    String Destino=DT[1];     // Quien recibe
    String Informacion=DT[2]; // Texto

    digitalWrite(led,HIGH);
    delay(5000);
    digitalWrite(led,LOW);

    if(true){
      Serial.print(Informacion);
      auxSerial.print(inputString2_Copy + "\n");
    }      
    
    if(Origen==ownAddss){
      Bandera = false;
      auxSerial.write("BL00\n");
    }    

  }



}

void separador(){
    int longitud = inputString2.length()+1;

    char trama[longitud];
    inputString2.toCharArray(trama, longitud);

    adrss = strtok(trama, ",");
    int i = 0;
    while (adrss != NULL) {
      //Serial.println(adrss);
      DT[i] = adrss;
      adrss = strtok(NULL, ",");
      //Serial.println(DT[i]);
      i++;
    }
}


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