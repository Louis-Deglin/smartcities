from servo import Servo
import network
import ntptime
import utime
import machine

# Identifiants Wi-Fi et décalage horaire
SSID = 'electroProjectWifi'
PASSWORD = 'B1MesureEnv'
DECALAGE_UTC = 1

horloge_servo = Servo(20)
wlan = network.WLAN(network.STA_IF)

print("=== DEBUT DU PROFILAGE ENERGETIQUE (60s PAR ETAT) ===")

# ETAT 1 : ACTIF AVEC WI-FI ALLUMÉ (60 SECONDES)
print("\n[ETAT 1/4] Microcontroleur actif avec Wi-Fi allume...")
wlan.active(True)
wlan.connect(SSID, PASSWORD)

timeout = 0
while not wlan.isconnected() and timeout < 15:
    utime.sleep(1)
    timeout += 1

if wlan.isconnected():
    try:
        ntptime.settime()
        print("  -> Synchro heure NTP OK.")
    except Exception as e:
        print(f"  -> Erreur NTP : {e}")

# Mise à jour de la position du servo
tm = utime.localtime()
heure_locale = (tm[3] + DECALAGE_UTC) % 24
heure_cadran = heure_locale % 12
angle = int(((12 - heure_cadran) % 12) * 15)
horloge_servo.turn(angle)

print(">>> ETAT 1 ACTIF : Relevez le courant pendant 60 secondes...")
utime.sleep(60)

# ETAT 2 : ACTIF SANS WI-FI (60 SECONDES)
print("\n[ETAT 2/4] Microcontroleur actif sans Wi-Fi...")
wlan.active(False) # Coupure du module réseau[cite: 150]
print(">>> ETAT 2 ACTIF : Relevez le courant pendant 60 secondes...")
utime.sleep(60)

#ETAT 3 : LIGHT SLEEP (60 SECONDES)
print("\n[ETAT 3/4] Passage en mode Light Sleep (60s)...")
print(">>> ETAT 3 ACTIF : Relevez le courant du mode veille...")
utime.sleep(1)
machine.lightsleep(60000)
print("  -> Sortie du Light Sleep.")
utime.sleep(2)

# ETAT 4 : DEEP SLEEP (60 SECONDES)
print("\n[ETAT 4/4] Passage en mode Deep Sleep (60s)...")
print(">>> ETAT 4 ACTIF : Relevez le courant d'extinction...")
print("  -> Remarque : Le reveil redémarrera le script automatiquement depuis le debut.")
utime.sleep(1)
machine.deepsleep(60000) 
