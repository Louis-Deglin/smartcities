from machine import I2C, Pin, ADC, PWM
from utime import sleep, ticks_ms, ticks_diff
from lcd1602 import LCD1602
from dht20 import DHT20

potentiometre = ADC(0)
led = Pin(18, Pin.OUT)
buzzer = PWM(Pin(16))
buzzer.duty_u16(0)

i2c_lcd = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
lcd = LCD1602(i2c_lcd, 2, 16)
lcd.display()

i2c_dht = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
capteur_temp = DHT20(i2c_dht)

dernier_releve = 0
dernier_clignotement = 0
etat_led = 0

temp_ambiante = 0.0
temp_consigne = 0.0

while True:
    temps_actuel = ticks_ms()

    #Lecture des capteurs et affichage toutes les secondes (1000 ms)
    if ticks_diff(temps_actuel, dernier_releve) >= 1000:
        
        #Conversion de la valeur du potentiomètre (0-65535) en température (15 à 35°C)
        val_pot = potentiometre.read_u16()
        temp_consigne = 15.0 + (val_pot / 65535.0) * 20.0
        
        #Lecture de la température ambiante via DHT20
        try:
            capteur_temp.measure()
            temp_ambiante = capteur_temp.temperature
        except RuntimeError as e:
            print("Erreur de lecture DHT20:", e)
        
        #Mise à jour de l'écran LCD
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.print("Set: {:.1f} C".format(temp_consigne))
        
        lcd.setCursor(0, 1)
        if temp_ambiante > temp_consigne + 3:
            lcd.print("ALARM")
        else:
            lcd.print("Ambient: {:.1f} C".format(temp_ambiante))
            
        dernier_releve = temps_actuel

    #Logique de contrôle (Thermostat et Alarmes)
    if temp_ambiante > temp_consigne + 3:
        # ALARME : Température mesurée > consigne + 3
        buzzer.freq(1000)
        buzzer.duty_u16(1000) # Le buzzer sonne
        
        # La LED clignote plus rapidement
        if ticks_diff(temps_actuel, dernier_clignotement) >= 100:
            etat_led = not etat_led
            led.value(etat_led)
            dernier_clignotement = temps_actuel
            
    elif temp_ambiante > temp_consigne:
        #DÉPASSEMENT SIMPLE : Température mesurée > consigne
        buzzer.duty_u16(0) # Le buzzer est éteint
        
        # La LED bat à 0.5 Hz, période de 2s, bascule toutes les 1000 ms
        if ticks_diff(temps_actuel, dernier_clignotement) >= 1000:
            etat_led = not etat_led
            led.value(etat_led)
            dernier_clignotement = temps_actuel
            
    else:
        # NORMAL : Température mesurée <= consigne
        led.value(0)
        buzzer.duty_u16(0)
        
    sleep(0.01) # Petite pause pour stabiliser la boucle
