#include "LedControl.h"

LedControl lc=LedControl(12,11,10,2);  // Pins: DIN,CLK,CS, # of Display connected

unsigned long delayTime=200;  // Delay between Frames

int incomingByte = 0;   // for incoming serial data
int blueLed=6;
int greenLed=5;
int redLed=4;

byte invader1a[] =
{
   B00011000,  // First frame of invader #1
   B00111100,
   B01111110,
   B11011011,
   B11111111,
   B00100100,
   B01011010,
   B10100101
};

byte invader1b[] =
{
  B00011000, // Second frame of invader #1
  B00111100,
  B01111110,
  B11011011,
  B11111111,
  B00100100,
  B01011010,
  B01000010
};

byte off[] =
{
  B00000000, // Second frame of invader #1
  B00000000,
  B00000000,
  B00000000,
  B00000000,
  B00000000,
  B00000000,
  B00000000
};


void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        pinMode(greenLed, OUTPUT);
        pinMode(redLed, OUTPUT);
        pinMode(blueLed,OUTPUT);
        digitalWrite(redLed, HIGH);
        digitalWrite(greenLed, HIGH);

        lc.shutdown(0,false);
        lc.shutdown(1,false);
        lc.setIntensity(0,5);  // Set intensity levels
        lc.setIntensity(0,8);
        lc.clearDisplay(0);  // Clear Displays
        lc.clearDisplay(1);
        
}

void sinvader1a()
{
  for (int i = 0; i < 8; i++)  
  {
    lc.setColumn(0,i,invader1a[i]);
  }
}

void sinvader1b()
{
  for (int i = 0; i < 8; i++)
  {
    lc.setColumn(0,i,invader1b[i]);
  }
}

void executeMatrix(byte ledArray[])
{
    for (int i = 0; i < 8; i++)
  {
    lc.setColumn(0,i,ledArray[i]);
  }
}
void loop() {
  
        if (Serial.available() > 0) {
      
        digitalWrite(blueLed, LOW);
        digitalWrite(redLed, HIGH);
        digitalWrite(greenLed, HIGH);

      
        incomingByte = Serial.read();
      
        Serial.print(incomingByte);
               if(incomingByte == 97){
                    digitalWrite(blueLed, HIGH);
                    digitalWrite(redLed, LOW);
                    digitalWrite(greenLed, HIGH);                    
                    executeMatrix(invader1a);
                    delay(delayTime);
                    executeMatrix(invader1b);
                    delay(delayTime);
                    delay(500);
                }else {
                    digitalWrite(blueLed, HIGH);
                    digitalWrite(redLed, HIGH);
                    digitalWrite(greenLed, LOW);
                    executeMatrix(off);
                    delay(500);
                  }
        }

        
}




