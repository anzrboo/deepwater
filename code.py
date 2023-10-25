"""

Immortal Bloom Deep Water lights

Board is a Pi Pico or other R2040 microcontroller running Adafruit CircuitPython

"""
import board
import neopixel
import time
import random
import analogio

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 99

#  set up the Neopixels

pixels = neopixel.NeoPixel(board.GP1, num_pixels, auto_write=False)
pixels.brightness = 0.4

# set up the analogue input pin

adc = analogio.AnalogIn(board.A2)
mic = adc.value

# initial variable setup

bleach = False
increment = 1

rval = 45
gval = 5
bval = 15

# main loop

while True:
    mic = adc.value # read microphone
    print("mic: ", mic) # print to serial, if using a REPL like Mu, you can see this

    for j in range(0, 20):
        for i in range(num_pixels): # random variation to make lights "twinkle"
            rvit = rval + random.randint(0, 5)
            gvit = gval + random.randint(0, 5)
            bvit = bval + random.randint(0, 5)
            pixels[i] = (rvit, gvit, bvit)
        pixels.write()
        time.sleep(0.05)

    # increment the values (closer to white)
    rval += increment
    gval += increment
    bval += increment

    # if there is a high level of input on the analogue, then move the process faster
    if mic > 35000:
        rval += increment
        gval += increment
        bval += increment

    print("red: ", rval)

    # end loop, fade out then go back to the start
    if rval > 200:
        increment = 1
        rval = 20
        for k in range(0, 200):
            level = 200 - k
            for m in range(num_pixels):
                pixels[m] = (level, level, level)
            pixels.write()
            time.sleep(0.02)
            time.sleep(0.02)
        time.sleep(10)
        rval = 45
        gval = 5
        bval = 15

