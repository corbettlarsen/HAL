
unsigned char ButtonState = 16;
      
void setup() {
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(9, OUTPUT);      
  // initialize the pushbutton pin as an input:
  
  pinMode(11, INPUT_PULLUP);

}

void loop(){ 
  
  buttonState = digitalRead(11);
  Serial.println(buttonState);
  
  delay(1);
}
