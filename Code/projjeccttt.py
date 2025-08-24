from machine import SoftI2C,Pin,ADC
import ssd1306 #import oled library

from ssd1306 import SSD1306_I2C
from bmp180 import BMP180 #import bmp180 library
from time import time,localtime
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)#oled pin configuration

bus = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
bmp180 = BMP180(bus)
bmp180.oversample_sett=2
bmp180.baseline = 101325

RL_VALUE = 10000
VREF = 3.3
R0_VALUE = 10000
TEMP_OFFSET = 0



display=t=hr=mi=sec=k=b=x=y=time_hr=time_last=tlm=tmq=0
temp=p=altitude=temperature=voltage=lm_35=0

touch=Pin(18,Pin.IN)
button=Pin(4,Pin.IN,pull=Pin.PULL_DOWN)
lm35_pin = ADC(Pin(34))

while True:
    if (touch.value()==1):
        display=display+1
        while(touch.value()==1):
            pass
    if(display==4):
        display=0
    if display==0:
        oled.fill(0)
        oled.text("Local Time:", 0, 0)
        oled.text(str(localtime()[3]) + ":" + str(localtime()[4]) + ":" + str(localtime()[5]), 0, 20)
        oled.text("or", 0, 30)
        if(localtime()[3]>12):
            time_last="PM"
            time_hr=localtime()[3]-12
        else:
            time_last="AM"
        oled.text(str(time_hr) + ":" + str(localtime()[4]) + ":" + str(localtime()[5])+" "+str(time_last), 0, 40)
        oled.show()
    elif display==1:
        if(button.value()==1):
            k=k+1;
            b=1
            while(button.value()==1):
                pass
        if(k%2==1 and b==1):
            t=time()+x
            b=0
        oled.fill(0)
        x=time()-t
        if(k%2==0 and b==1):
            y=x
            b=0
        if(k%2==0):
            oled.text("Lap :", 0, 30)
            oled.text(str(y), 0, 45)
            x=0
        
        
        oled.text("Stop watch:", 0, 0)
        if(t!=0):
            oled.text(str(x),0,15)
        else:
            oled.text(str(0),0,15)
        oled.show()
    elif display==2:
        temp = bmp180. temperature
        p = bmp180.pressure/101325
        altitude = bmp180.altitude
        oled.fill(0)
        oled.text("Temp Reading:", 0, 0)
        oled.text(str(round(temp, 1)) + " C", 0, 10)
        oled.text("Pres Reading:", 0, 20)
        oled.text(str(round(p, 2)) + " Pa", 0, 30)
        oled.text("Alt Reading:", 0, 40)
        oled.text(str(round(altitude, 1)) + " m", 0, 50)
        oled.show()
    elif display==3: 
        if(time()-tlm>5):
            lm35_value = lm35_pin.read()
            tlm=time()  
            voltage = (lm35_value / 4095.0) * VREF
            temperature = (voltage - TEMP_OFFSET) * 100.0
            oled.fill(0)
            oled.text("Body Temp:", 0, 10)
            oled.text(str(temperature),0,20)
            oled.show()
   