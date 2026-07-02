import machine
import time

# --- CONFIGURATION ZONE ---
LED_PIN = 1
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# This variable simulates our incoming data stream
heart_rate = eval(input(print("Enter your heart rate: ")))  

print("Medical Monitoring Simulator Active...")

try:
    while True:
        # Every cycle, we simulate the heart rate increasing 
        # (This acts like a shifting data variable)
        heart_rate += 5
        print(f"Current Heart Rate: {heart_rate} BPM")
        
        # ========================================================
        # YOUR PROGRAMMING CHALLENGE:
        # Write the conditional state logic below.
        # ========================================================
        
        # STATE 1: Normal (Heart rate is less than or equal to 100)
        # ACTION: Blink the LED slowly (Turn ON, sleep 0.4, Turn OFF, sleep 0.4)
        if heart_rate <= 100:
            led.value(1)
            time.sleep(0.4)
            led.value(0)
            time.sleep(0.4)
            
        # STATE 2: Warning (Heart rate is between 101 and 140)
        # ACTION: Blink the LED rapidly (Turn ON, sleep 0.1, Turn OFF, sleep 0.1)
        elif heart_rate > 100 and heart_rate <= 140:
            led.value(1)
            time.sleep(0.1)
            led.value(0)
            time.sleep(0.1)
            
        # STATE 3: Critical Alarm (Heart rate is greater than 140)
        # ACTION: Turn the LED solid ON, print a danger message, and break the loop
        else:
            led.value(1)
            print("Emergency!!!")
            break
            
except KeyboardInterrupt:
    led.off()
    print("\nSimulation terminated safely.")

