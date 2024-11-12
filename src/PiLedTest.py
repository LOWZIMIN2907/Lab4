import hal.hal_input_switch as SWITCH
import hal.hal_led as LED
import time

# Function to turn LED on or off based on input
def control_LED(state):
    if state:
        LED.set_output(24, 1)
    else:
        LED.set_output(24, 0) 

# Function to make the LED blink at a specified frequency for a given duration
def blink_LED(frequency, duration):
    end_time = time.time() + duration 
    while time.time() < end_time:
        LED.set_output(24, 1) 
        time.sleep(1 / (2 * frequency))  
        LED.set_output(24, 0) 
        time.sleep(1 / (2 * frequency)) 
    LED.set_output(24, 0) 


def main():
    SWITCH.init()  
    LED.init()  
    on_off = False 

    while True:
        # Check the position of the switch
        switch_position = SWITCH.read_slide_switch()

        if switch_position == 1:  # If the switch is in the right position
            blink_LED(10, 5)  
            control_LED(False) 
            time.sleep(0.2)  # Small delay to prevent fast toggling
        else: 
            control_LED(False)
            time.sleep(0.1)

# Run the program
if __name__ == "__main__":
    main()