# Ardupilot-WS2812b-led-control
This repo helps in controlling the ws2812b led through flight controller integral driver using pymavlink.

Steps:

1. Read the doc file attached.
2. Ensure that servo function is set to 120.
3. use the python program attached.
4. For changing the number of led go to firmware part(libraries/AP_notify/Neopixel.cpp) in neopixel.cpp change the \#define HAL_NEOPIXEL_COUNT 16 to your desired value.