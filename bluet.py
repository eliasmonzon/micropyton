from machine import UART, Pin
import time
modulo = UART(0,9600, tx=Pin(16), rx=Pin(17))
Rele1 = Pin(6,Pin.OUT)
Rele2 = Pin(3,Pin.OUT)
Rele3 = Pin(4,Pin.OUT)
Rele4 = Pin(5,Pin.OUT)
Rele5 = Pin(6,Pin.OUT)
Rele6 = Pin(7,Pin.OUT)
Rele7 = Pin(8,Pin.OUT)
Rele8 = Pin(9,Pin.OUT)

while True:
    if modulo.any()>0:
        dato = modulo.read(1)   
        if "F" == dato:
            Rele1.toggle()
        if "b" in dato:
            Rele2.toggle()  
        if "c" in dato:
            Rele3.toggle()  
        if "d" in dato:
            Rele4.toggle()
        if "e" in dato:
            Rele5.toggle()  
        if "f" in dato:
            Rele6.toggle()
        if "g" in dato:
            Rele7.toggle()  
        if "h" in dato:
            Rele8.toggle() 