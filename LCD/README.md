# Module LCD et Thermostat

Ce dossier `LCD` contient le code permettant de simuler un thermostat avec affichage et alarmes. Le système lit une température de consigne via un potentiomètre et la compare avec la température ambiante. Les informations s'affichent sur l'écran, et des alertes visuelles (LED) et sonores (buzzer) se déclenchent si la température dépasse la consigne.

## Structure des fichiers

* **`Labo3.py`** : C'est le script principal qui contient la logique de contrôle et la gestion du matériel.
* **`dht20.py`** : Il s'agit de la librairie nécessaire pour faire fonctionner le capteur de température DHT20 en I2C.
* **`lcd1602.py`** : Il s'agit de la librairie requise pour contrôler l'affichage sur l'écran LCD en I2C.
