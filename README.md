# Ardupilot-WS2812b-led-control
This repo helps in controlling the ws2812b led through flight controller integral driver using pymavlink.

Steps:

1. Connect as shown in the circuit.
   * ![](https://github.com/bhaskarsdose/Ardupilot-WS2812b-led-control-/blob/master/Circuit.png)
2. Ensure that servo function is set to 120.
3. Connect the strip with external power source with +5V (each led consumes 60mA average).
4. use the python program attached  to turn on the led strip and changing its color or its frequency also you can use 4 led strips on 4 different channels.
5. For changing the number of led go to firmware part(libraries/AP_notify/Neopixel.cpp) in neopixel.cpp change the \#define HAL_NEOPIXEL_COUNT 16 to your desired value.