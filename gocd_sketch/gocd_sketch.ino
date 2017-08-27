int incomingByte = 0;   // for incoming serial data
int blueLed=6;
int greenLed=5;
int redLed=4;
void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        pinMode(greenLed, OUTPUT);
        pinMode(redLed, OUTPUT);
        pinMode(blueLed,OUTPUT);
        digitalWrite(redLed, HIGH);
        digitalWrite(greenLed, HIGH);
        
}

void loop() {
  
        if (Serial.available() > 0) {
        digitalWrite(blueLed, HIGH);
        digitalWrite(redLed, LOW);
        digitalWrite(greenLed, HIGH);
        
        delay(500);
        
        digitalWrite(blueLed, HIGH);
        digitalWrite(redLed, HIGH);
        digitalWrite(greenLed, LOW);

        delay(500);

        digitalWrite(blueLed, LOW);
        digitalWrite(redLed, HIGH);
        digitalWrite(greenLed, HIGH);

        delay(500);

        incomingByte = Serial.read();

               if(incomingByte = 97){
                    digitalWrite(blueLed, HIGH);
                    digitalWrite(redLed, LOW);
                    digitalWrite(greenLed, HIGH);
                    delay(6000);
                }else {
                    digitalWrite(blueLed, LOW);
                    digitalWrite(redLed, HIGH);
                    digitalWrite(greenLed, HIGH);
                    delay(6000);
                  }
        }

        
}
