#include<ESP8266WiFi.h>
#include<ModbusIP_ESP8266.h>

//  Registro modbus
const int ledCoil=0;
const int ledIsts=0;
const int dataIReg=0;
const int dataHReg=0;

//  Pin led
const int ledPin=2;

//  Wifi conexion
void wifiCon();

//  Modbus
ModbusIP mb;

void setup() {
  Serial.begin(9600);
  wifiCon();

  mb.server();

  pinMode(ledPin,OUTPUT); 
  //digitalWrite(ledPin,LOW);

  //Segundo parametro valor inicial
  mb.addCoil(ledCoil);      //Coil
  mb.addIsts(ledIsts);      //Discrete input

  mb.addHreg(dataHReg);    //Holding register
  mb.addIreg(dataIReg);   //Input register

}

void loop() {
  mb.task();
  int b = analogRead(A0);
  bool a = mb.Coil(ledCoil);
  Serial.println(a);


// Modifica imagen
  if(b>1000){
    mb.Ists(ledIsts,1);
    // recibe valor del led
    digitalWrite(ledPin,mb.Coil(ledCoil));
  }
  if(b<50){
    mb.Ists(ledIsts,0);
    // Recibe valores de scale
  analogWrite(ledPin,mb.Hreg(dataHReg));
  }
  
// modifica progressbar
  mb.Ireg(dataIReg,b);

  delay(10);
}

void wifiCon(){
  const char* ssid="INFINITUM208C";
  const char* password="Tr9Xt1Aa1g";

  WiFi.begin(ssid,password);

  while(WiFi.status()!=WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  //  Modo servidor
  Serial.println("");
  Serial.println("Wifi conectado");
  Serial.println("Direccion IP: ");
  Serial.println(WiFi.localIP());     //192.168.1.78
}

