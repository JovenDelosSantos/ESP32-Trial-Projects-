#define DELAY_TIME 1000 // 1 second delay

void setup() {
  // No explicit pinMode is needed for the built-in RGB macro, 
  // but we initialize it implicitly by writing to it.
}

void loop() {
  // Turn the RGB LED Red
  neopixelWrite(RGB_BUILTIN, 64, 0, 0); // Red, Green, Blue (0-255 brightness)
  delay(DELAY_TIME);

  // Turn the RGB LED Off
  neopixelWrite(RGB_BUILTIN, 0, 0, 0);
  delay(DELAY_TIME);
}