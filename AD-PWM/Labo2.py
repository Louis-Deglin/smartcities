'''# Allumer LED avec Rotor
from machine import ADC,Pin
from utime import sleep

LED = Pin(16,Pin.OUT)
ROTARY_ANGLE_SENSOR = ADC(1)

while True:
    print(ROTARY_ANGLE_SENSOR.read_u16())
    if ROTARY_ANGLE_SENSOR.read_u16() > 30000:
        LED.value(1)
        sleep(1)
    else:
        LED.value(0)
        sleep(1)'''
        
'''# Allumer LED avc rotor et intensité avec rotor
from machine import ADC,Pin,PWM
from utime import sleep

LED_PWM = PWM(Pin(18))
ROTARY_ANGLE_SENSOR = ADC(0)

LED_PWM.freq(500)

while True:
    val = ROTARY_ANGLE_SENSOR.read_u16()
    LED_PWM.duty_u16(val)'''

'''#Buzzer note
from machine import Pin,PWM
from utime import sleep

buzzer = PWM(Pin(27))
while True:
    buzzer.freq(1046)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1175)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1318)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1397)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1568)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1760)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1967)
    buzzer.duty_u16(1000)
    sleep(1)'''

'''#Chanson buzzer
from machine import Pin, I2C, ADC, PWM
from time import sleep

buzzer = PWM(Pin(27))
vol = 1000

def DO(time):
    buzzer.freq(1046)
    buzzer.duty_u16(vol)
    sleep(time)
def RE(time):
    buzzer.freq(1175)
    buzzer.duty_u16(vol)
    sleep(time)
def MI(time):
    buzzer.freq(1318)
    buzzer.duty_u16(vol)
    sleep(time)
def FA(time):
    buzzer.freq(1397)
    buzzer.duty_u16(vol)
    sleep(time)
def SO(time):
    buzzer.freq(1568)
    buzzer.duty_u16(vol)
    sleep(time)
def LA(time):
    buzzer.freq(1760)
    buzzer.duty_u16(vol)
    sleep(time)
def SI(time):
    buzzer.freq(1967)
    buzzer.duty_u16(vol)
    sleep(time)
def N(time):
    buzzer.duty_u16(0)
    sleep(time)

while True:
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    N(0.01)
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    MI(0.25)
    FA(0.25)
    SO(0.5)
    
    MI(0.25)
    FA(0.25)
    SO(0.5)
    N(0.01)
    
    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    RE(0.25)
    SO(0.25)
    DO(0.5)
    N(0.01)
    
    RE(0.25)
    SO(0.25)
    DO(0.5)'''

#Exercice 2
from machine import Pin, ADC, PWM
from time import sleep, ticks_ms, ticks_diff

buzzer = PWM(Pin(27))
rotor = ADC(0)
led = Pin(16, Pin.OUT)
bouton = Pin(18, Pin.IN, Pin.PULL_UP)

melodie_choisie = 1
melodie_en_cours = 1
dernier_clic = 0

#interruption (Détecte le clic instantanément)
def changer_melodie(pin):
    global melodie_choisie, dernier_clic
    if ticks_diff(ticks_ms(), dernier_clic) > 300: # Anti-rebond
        if melodie_choisie == 1:
            melodie_choisie = 2
        else:
            melodie_choisie = 1
        dernier_clic = ticks_ms()

bouton.irq(trigger=Pin.IRQ_FALLING, handler=changer_melodie)

def get_volume():
    return rotor.read_u16() // 2

def pause_check(secondes):
    # Convertit les secondes en millisecondes et calcule le nombre de boucles de 10ms
    boucles = int((secondes * 1000) / 10) 
    
    for _ in range(boucles):
        if melodie_choisie != melodie_en_cours:
            buzzer.duty_u16(0) # Coupe le son immédiatement
            led.value(0)       # Éteint la LED immédiatement
            return             # Quitte la pause
        sleep(0.01)            # Petite pause de 10ms

# Si la mélodie a changé, le 'return' fait passer la note sans la jouer
def DO(time):
    if melodie_choisie != melodie_en_cours: return
    led.value(1); buzzer.freq(1046); buzzer.duty_u16(get_volume()); pause_check(time); led.value(0)
    
def RE(time):
    if melodie_choisie != melodie_en_cours: return
    led.value(1); buzzer.freq(1175); buzzer.duty_u16(get_volume()); pause_check(time); led.value(0)
    
def MI(time):
    if melodie_choisie != melodie_en_cours: return
    led.value(1); buzzer.freq(1318); buzzer.duty_u16(get_volume()); pause_check(time); led.value(0)
    
def FA(time):
    if melodie_choisie != melodie_en_cours: return
    led.value(1); buzzer.freq(1397); buzzer.duty_u16(get_volume()); pause_check(time); led.value(0)
    
def SO(time):
    if melodie_choisie != melodie_en_cours: return
    led.value(1); buzzer.freq(1568); buzzer.duty_u16(get_volume()); pause_check(time); led.value(0)
    
def LA(time):
    if melodie_choisie != melodie_en_cours: return
    led.value(1); buzzer.freq(1760); buzzer.duty_u16(get_volume()); pause_check(time); led.value(0)
    
def SI(time):
    if melodie_choisie != melodie_en_cours: return
    led.value(1); buzzer.freq(1967); buzzer.duty_u16(get_volume()); pause_check(time); led.value(0)
    
def N(time):
    if melodie_choisie != melodie_en_cours: return
    buzzer.duty_u16(0); led.value(0); pause_check(time)

while True:
    # On mémorise la mélodie qui doit être jouée pour ce cycle
    melodie_en_cours = melodie_choisie 
    
    if melodie_en_cours == 1:
        DO(0.25)
        RE(0.25)
        MI(0.25)
        DO(0.25)
        N(0.05)
        
        DO(0.25)
        RE(0.25)
        MI(0.25)
        DO(0.25)
        N(0.05)
        
        MI(0.25)
        FA(0.25)
        SO(0.5)
        N(0.05)
        
        MI(0.25)
        FA(0.25)
        SO(0.5)
        N(0.05)
        
        SO(0.125)
        LA(0.125)
        SO(0.125)
        FA(0.125)
        MI(0.25)
        DO(0.25)
        N(0.05)
        
        SO(0.125)
        LA(0.125)
        SO(0.125)
        FA(0.125)
        MI(0.25)
        DO(0.25)
        N(0.05)
        
        RE(0.25)
        SO(0.25)
        DO(0.5)
        N(0.05)
        
        RE(0.25)
        SO(0.25)
        DO(0.5)
        N(0.5) 
        
    elif melodie_en_cours == 2:
        DO(0.3)
        RE(0.3)
        MI(0.3)
        FA(0.3)
        SO(0.3)
        LA(0.3)
        SI(0.3)
        N(0.5)




