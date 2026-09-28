#Allumer / éteindre
'''import machine
LED = machine.Pin(16,machine.Pin.OUT)
LED.value(1)'''

#Faire clignoter
'''import machine
import utime

LED = machine.Pin(16,machine.Pin.OUT)

while True:
    LED.value(1)
    utime.sleep(0.1)
    LED.value(0)
    utime.sleep(0.1)
'''

#Allumer /éteindre avec bouton
'''import machine
import utime

LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

val = 0

while True:
    if BUTTON.value() == 1:
        LED.value(1)
        utime.sleep(1)
    elif BUTTON.value() == 0:
        LED.value(0)
        utime.sleep(1)
        '''
#Allumer au clic
'''import machine
import utime

LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

val = 0

while True:
    if BUTTON.value() == 1:
        val = val+1
        utime.sleep(1)
    elif val == 2:
        val = 0
        utime.sleep(1)
    LED.value(val)'''

#Exercice (1 clic clignotant 0,50Hz, 2 clic plus rapide clignotant, 3 clic éteins)
import machine
import utime

# Configuration des broches (Pins)
# Broche 16 en sortie pour contrôler la LED
LED = machine.Pin(16, machine.Pin.OUT)
# Broche 18 en entrée pour lire le bouton, avec une résistance PULL_DOWN interne pour forcer l'état à 0 quand le bouton n'est pas pressé
BUTTON = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Variables globales pour suivre l'état du système
etat_clic = 0               # Compteur d'état (0=éteint, 1=lent, 2=rapide, 3=éteint)
dernier_etat_bouton = 0     # Mémorise l'état précédent du bouton pour détecter le changement
etat_avant_pause = 0        # Sauvegarde l'état avant d'entrer dans une pause

#Vérifie l'état du bouton et incrémente le compteur d'état si un clic est détecté et gère le rebond.
def gestion_bouton():
    global etat_clic, dernier_etat_bouton
    
    etat_actuel = BUTTON.value()
    
    # Détecte le passage de l'état relâché (0) à pressé (1)
    if etat_actuel == 1 and dernier_etat_bouton == 0:
        etat_clic += 1
        
        # Réinitialisation du cycle après le 3ème clic
        if etat_clic > 3:
            etat_clic = 0
            
        # Délai anti-rebond
        utime.sleep(0.05) 
        
    # Met à jour la mémoire de l'état du bouton pour le prochain cycle
    dernier_etat_bouton = etat_actuel

#Met le programme en pause afin de découper le temps d'attente en petites tranches de 10ms pour vérifier le bouton
#en continu, ce qui permet d'interrompre la pause immédiatement si l'utilisateur clique. Sans ça, il fallait avoir de la chance lors d'un clic pour être détecté
def pause_check(millisecondes):
    global etat_avant_pause
    etat_avant_pause = etat_clic
    
    # Calcul du nombre de boucles de 10ms nécessaires
    boucles = millisecondes // 10
    
    for _ in range(boucles):
        gestion_bouton() # Lecture de l'état du bouton
        
        # Si le bouton a été pressé pendant l'attente, l'état change et on quitte la pause
        if etat_clic != etat_avant_pause:
            return 
            
        utime.sleep(0.01) # Petite pause de 10ms

#Gère le comportement de la LED en fonction de l'état actuel (etat_clic).
def clignotant():
    if etat_clic == 1:
        # État 1 : Clignotement lent (0.5 Hz)
        LED.value(1)
        pause_check(1000)
        
        # Vérifie si l'utilisateur a cliqué pendant l'allumage avant d'éteindre
        if etat_clic == 1: 
            LED.value(0)
            pause_check(1000)
            
    elif etat_clic == 2:
        # État 2 : Clignotement rapide
        LED.value(1)
        pause_check(100) # Attente de 100ms
        
        # Vérifie si l'utilisateur a cliqué pendant l'allumage avant d'éteindre
        if etat_clic == 2:
            LED.value(0)
            pause_check(100)
            
    elif etat_clic == 3 or etat_clic == 0:
        # État 3 ou 0 : LED éteinte
        LED.value(0)
        # Légère pause pour éviter que la boucle ne tourne à pleine vitesse pour rien
        utime.sleep(0.05) 

# Boucle principale infinie
while True:
    gestion_bouton()
    clignotant()
