import time
import machine
import neopixel

student_register ={}

student_register[202302826] = "Joven"
student_register[202302827] = "John Rey"
student_register[202302828] = "Anjun"
student_register[202302829] = "RJ"

led = machine.Pin(1, machine.Pin.OUT)

RGB_PIN = 38
np = neopixel.NeoPixel(machine.Pin(RGB_PIN), 1)

try: 

    while True:

        search_id = int(input("Enter your student number: "))

        if search_id == 0:
           led.value(1)
           time.sleep(2)
           led.value(0)
           time.sleep(1)
           led.value(1)
           time.sleep(2)
           print("The system is going off, Thank you!")
           led.value(0)
           break   

        elif search_id == 1234: 
           print("--- STUDENT REGISTER ---")
           for std_id, name in student_register.items(): 
                print("ID: ", std_id, "Name: ", name)
                np[0] = (255, 0, 0)
                np.write()
                time.sleep(1)
                np[0] = (0, 0, 0)
                np.write()
            

        elif search_id in student_register:
            student_name = student_register[search_id]
            print("The name of student under", search_id, "is", student_name)
            
            np[0] = (255, 0, 0)
            np.write()
            time.sleep(0.1)

            np[0] = (255, 255, 0)
            np.write()
            time.sleep(0.1)
            
            np[0] = (255, 255, 0)
            np.write()
            time.sleep(0.1)

            np[0] = (0, 255, 0)
            np.write()
            time.sleep(0.1)
            
            np[0] = (0, 0, 255)
            np.write()
            time.sleep(0.1)
            
            np[0] = (255, 0, 255)
            np.write()
            time.sleep(0.1)
            
            np[0] = (255, 0, 255)
            np.write()
            time.sleep(0.1)
            
            led.value(1)  # Turn ON
            time.sleep(0.1)
            led.value(0)  # Turn OFF
            time.sleep(0.1)
        else:
            print("Student number", search_id, "is not registered in the system")
            np[0] = (255, 0, 0)
            np.write()
            time.sleep(0.5)

            np[0] = (0, 0, 0)
            np.write()
            time.sleep(0.5)
            
            np[0] = (255, 0, 0)
            np.write()
            time.sleep(0.5)

            np[0] = (0, 0, 0)
            np.write()
            time.sleep(0.5)
            
            np[0] = (255, 0, 0)
            np.write()
            time.sleep(0.5)
            
            np[0] = (0, 0, 0)
            np.write()
            time.sleep(0.5)
            
            np[0] = (0, 0, 0)
            np.write()
            time.sleep(0.5)
            
            led.value(1)  # Turn ON
            time.sleep(0.1)
            led.value(0)  # Turn OFF
            time.sleep(0.1)
        print("-" * 50)
        time.sleep(2)

except KeyboardInterrupt:
    led.value(0)