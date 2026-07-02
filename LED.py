import machine 
import time 

led = machine.Pin(4, machine.Pin.Out)

print("S.O.S system is currently operating")
while True:
    for i in range (3):
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)

    time.sleep(10) 

    for i in range (3): 
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)

    time.sleep(5)

    for i in range (3):
        led.value(1) 
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)

    


