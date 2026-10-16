#LED RGB couleur change
'''from ws2812 import WS2812
import utime

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

led = WS2812(18,1)

while True:
    print("fills")
    for color in COLORS:
        led.pixels_fill(color)
        led.pixels_show()
        utime.sleep(0.2)
        '''

#Ventilateur boutton
'''import machine
import utime
button = machine.Pin(18, machine.Pin.IN)
miniFan = machine.Pin(16, machine.Pin.OUT)
val = 0
while True:
    val = button.value()
    if val == 1:
        miniFan.toggle()
        utime.sleep_ms(100)'''
        
'''# ventilateur relais
from machine import Pin
from time import sleep
button = Pin(16,Pin.IN)
fan = Pin(18,Pin.OUT)
relay = Pin(20,Pin.OUT)

while True:
    fan.value(1)
    while button.value() == 1:
        relay.toggle()
        sleep(1)'''


#intlligent light
'''from ws2812 import WS2812
from machine import I2C,Pin,ADC
from utime import sleep

led = WS2812(18,1)
LIGHT_SENSOR = ADC(0)
SOUND_SENSOR = ADC(1)

while True:
    average = 0
    light = LIGHT_SENSOR.read_u16()/256
    for i in range (1000):
        noise = SOUND_SENSOR.read_u16()/256
        average += noise
    noise = average/1000
    print(noise)
    
    if light < 80:
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.2)
    else:
        if noise < 15:
            led.pixels_fill((0, 255, 0))
            led.pixels_show()
            sleep(1)
        if noise >= 15 and noise < 25:
            led.pixels_fill((255, 255, 0))
            led.pixels_show()
            sleep(1)
        if noise >= 25:
            led.pixels_fill((255, 0, 0))
            led.pixels_show()
            sleep(1)'''

#Exercice 4
from machine import ADC
import utime
import random
from ws2812 import WS2812

led = WS2812(18, 1)      #LED RGB sur D18
mic = ADC(0)             #Microphone sur A0

# Paramètres de détection
# Le seuil a été ajusté après plusieurs tests
SEUIL_SONORE = 30000
DELAI_ANTI_REBOND = 250

dernier_battement = utime.ticks_ms()

while True:
    #Lecture du capteur de son
    valeur_son = mic.read_u16()
    maintenant = utime.ticks_ms()
    
    #Détection d'un battement
    #Si le son dépasse le seuil et qu'assez de temps s'est écoulé depuis le dernier pic
    if valeur_son > SEUIL_SONORE and utime.ticks_diff(maintenant, dernier_battement) > DELAI_ANTI_REBOND:
        
        #Changer la couleur aléatoirement
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        led.pixels_fill((r, g, b))
        led.pixels_show()
        
        print("Battement détecté !")
                
        #Mise à jour du temps du dernier battement
        dernier_battement = maintenant
        
    utime.sleep_ms(10)
