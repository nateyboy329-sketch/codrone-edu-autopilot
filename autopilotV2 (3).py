#code made by Natheniel Robinson, available for educational and personal use. please credit me.
from codrone_edu.drone import *
import random
import time
#start the drone
drone = Drone()
drone.pair()
drone.controller_clear_screen()
color = drone.get_colors()
def emergency():
    x = drone.get_accel_x()
    if x > 15:
        drone.emergency_stop()

    if x < -15:
        drone.emergency_stop()
    y = drone.get_accel_y()
    if y > 15:
        drone.emergency_stop()

    if y < -15:
        drone.emergency_stop()
def turn():
    distances = [0, 0, 0]
    for i in range(3):
        drone.turn_right(90)
        distances[i] = drone.get_front_range()

    drone.turn_right(90)
    if distances[0] == max(distances):
            drone.turn_right(90)
            print("turning right")
    elif distances[1] == max(distances):
        drone.turn_right(180)
        print("turning around")
    else:
        drone.turn_left(90)
        print("turning left")
            
            
def safety_feature():
    drone.set_drone_LED(255, 0, 0, 800)
    print("safety feature; put on red pad or surface to bypass.")
    drone.controller_buzzer(700, 4000)
    drone.drone_buzzer_sequence("error")
def startup():
    drone.controller_buzzer(600, 200)
    drone.controller_buzzer(900, 1000)
    drone.drone_buzzer_sequence("success")
    drone.takeoff()
#ditances when detecting wall

if 'red' in color:      
    startup()


   
    image = drone.controller_create_canvas() 
    time.sleep(1)
    #write either error or succsess to controller
    if drone.get_bottom_range() > 2:
        drone.controller_draw_string(0, 40, "takeoff succsessful", image)
    else:
        drone.controller_draw_string(0, 40, "error 404, takeoff failed", image)
        drone.emergency_stop()
    drone.controller_draw_canvas(image) 
   

    #main loop
    while True:
        brn = drone.get_bottom_range()      
        temp = drone.get_drone_temperature()
        print(temp)
        if drone.r1_pressed():
            drone.land()
        drone.controller_buzzer(400, 500)
        print("going forward")
        time.sleep(1)
        #avoid wall means to move forward until you hit a wall
        drone.avoid_wall(250)
        print("AHH! A WALL!")
        drone.controller_buzzer(800, 600)


        #turn systems
        turn()
            #hold height and check land
        if brn < 11:
            drone.emergency_stop()
            
        if  brn > 100:
            drone.go("down", 30, 1)
        elif brn < 50:
            drone.go("up", 30, 1)
        variable = random.randint(1, 3)
        drone.set_drone_LED(0, 255, 0, 800)
        emergency()
        drone.set_drone_LED(255, 0, 0, 800)
        drone.drone_buzzer_sequence("error")
        #emergency stop
       
      
              
      
else:
    safety_feature()
    
        
drone.close()
