#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include "printf.h"


RF24 radio(9,10);


void setup(void){
  while(!Serial);
  Serial.begin(9600);

  radio.begin();

  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  const uint64_t pipe = 0xE8E8F0F0E1LL;
  radio.openReadingPipe(1,pipe);

  radio.enableDynamicPayloads();
  radio.powerUp(); 
}

void loop(void){
   radio.startListening();
   Serial.println("Starting loop.Radio on.");
   char recievedMessage[32] = {0};
   if(radio.available()){
    radio.read(recievedMessage , sizeof(recievedMessage));
    Serial.println(recievedMessage);
    Serial.println("Turning off th Radio.");
    radio.stopListening(); 
    String stringMessage(recievedMessage);

    if(stringMessage == "0"){
      
    }
    
    if(stringMessage == "1"){
      
    }
    
    if(stringMessage == "2"){
      
    }
    
    if(stringMessage == "3"){
      
    }
    
   }
   delay(200);
}

