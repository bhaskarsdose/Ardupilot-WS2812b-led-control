from pymavlink import mavutil
master = mavutil.mavlink_connection('/dev/ttyACM0',baud=115200)

pattern = [0] * 24

pattern[0] = 0   #red
pattern[1] = 255 #green
pattern[2] = 0   #blue
pattern[3] = 5   # freq Hz


master.mav.led_control_send(
    master.target_system,
    master.target_component,0,0,4,pattern)



