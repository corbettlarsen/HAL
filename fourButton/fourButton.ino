

unsigned char previousButtonState = 16;
      
void setup() {
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(9, OUTPUT);      
  // initialize the pushbutton pin as an input:
  pinMode(7,INPUT_PULLUP);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);  
  digitalWrite(9, HIGH); 
}

void loop(){ 
  
  unsigned char buttonState = 0;
  if(digitalRead(7)){
    buttonState ^= 0b10000;
  }  
  if(digitalRead(10)){
    buttonState ^= 0b01000;
  }
   if(digitalRead(11)){
    buttonState ^= 0b00100;
  }
   if(digitalRead(12)){
    buttonState ^= 0b00010;
  }
   if(digitalRead(13)){
    buttonState ^= 0b00001;
  }
  
  Serial.println(buttonState);
  
  previousButtonState = buttonState;
  delay(1);
}
