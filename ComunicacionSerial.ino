//Para los comandos
String inputString = "";
bool stringComplete = false;
int valor =0;

void setup()
{
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(3,OUTPUT);
}

void loop()
{
  //Leer desde python
  if (stringComplete)
  {
    inputString.trim();
    //Serial.println(inputString);

    //Procesar las opciones
    processCommand();

    //resetear String
    inputString = "";
    stringComplete = false;
  }
}

void processCommand() {
  if (inputString.indexOf("$ONR20") != -1) {
      digitalWrite(3,HIGH);
    }
  
  if (inputString.indexOf("$OFFR20") != -1) {
      digitalWrite(3,LOW);
    }

  if(inputString.indexOf("$SLD1") != -1){
    String Svalor = inputString.substring(5);
    valor = Svalor.toInt();
    valor = map(valor, 0, 100, 0, 255);
    analogWrite(3,valor);
  }
  
}

void serialEvent() {
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
