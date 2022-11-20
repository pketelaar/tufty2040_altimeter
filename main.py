
import machine
import time
import math
import random



import breakout_icp10125
import pimoroni_i2c

i2c = pimoroni_i2c.PimoroniI2C(4, 5)

icp10125 = breakout_icp10125.BreakoutICP10125(i2c)


#from pimoroni import RGBLED
from picographics import PicoGraphics, DISPLAY_TUFTY_2040

# set up the hardware
display = PicoGraphics(display=DISPLAY_TUFTY_2040, rotate=180)

# set the display backlight to 99%
display.set_backlight(0.99)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()

BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
BLUE = display.create_pen(0, 0, 255)

BG = display.create_pen(40, 40, 40)


#import pressure altitude from pressure sensor    


display.set_pen(BLACK)
display.clear()
display.set_pen(WHITE)
display.text("Altimeter", 0, 0, 320, 2)
altitude = 0
  
    
while True:
    t, p, status = icp10125.measure(icp10125.NORMAL)
    metric_alt = 44331.5 - 4946.62 * p ** (0.190263)
    feet_alt = metric_alt * 3.28
    #print(t, p)
    #print(feet_alt)
    rounded = round(feet_alt)
    feet = str(rounded)
    
    display.set_pen(WHITE)
    display.circle(160, 120, 100)
    display.set_pen(BLACK)

    altitude = feet_alt
    max_altitude = 1000
    
    converted = altitude/max_altitude
    #print(converted)
    target = converted * 360
    deg = ((target - 90) * (3.14/180))
   
    #print(target)
    len = 100
    
    centerx=160
    centery=120
    
    endx=(int(len*math.cos(deg)))
    endy=(int(len*math.sin(deg)))
    
       
    #print((centerx+endx), (centery+endy))
    
    display.line(centerx, centery, centerx+endx, centery+endy)
    
    
    ###thousands

    #thousands = altitude / 1000
    #thou = round(thousands)
    #print(thou)
    
    #max_altitude = 10000
    
    #converted2 = thou/max_altitude
    #print(converted2)
    
    #target2 = converted * 360
    #deg2 = ((target2 - 90) * (3.14/180))
   
    #len2 = 50
    
    #centerx2=160
    #centery2=120
    
    #endx2=(int(len2*math.cos(deg2)))
    #endy2=(int(len2*math.sin(deg2)))
    
       
    
    #display.line(centerx2, centery2, centerx2+endx2, centery2+endy2)
    

    
    
    
    ###endthousands
    
    
    
    display.set_pen(WHITE)
    display.text(str(feet), 0, 210, 320, 3)
#    display.set_pen(BLACK)
#    display.text(str(altitude), 0, 220, 320, 2)
    prevalt=feet
    #print(altitude)
    display.set_pen(BLUE)
    #display.set_font(bitmap8)

    #display.text("number", X, y, scale)
    display.text("0", 155, 20, 10)
    display.text("5", 155, 205, 10)
    display.text("1", 210, 40, 4)
    display.text("9", 100, 40, 4)
    display.text("2", 240, 80, 4)
    display.text("8", 70, 80, 4)
    display.text("7", 70, 140, 4)
    display.text("3", 240, 140, 4)
    display.text("6", 100, 185, 4)
    display.text("4", 210, 185, 4)
    

    
    
    display.update()
    #altitude= altitude + random.randint(-100,250)
    #if altitude > 10000:
    #    altitude = 0
    time.sleep(.1)
    display.set_pen(BLACK)
    display.text(str(prevalt), 0, 210, 320, 3)
    display.text("0", (160), 40, 3)
    
    
