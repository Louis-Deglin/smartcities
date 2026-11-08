# Horloge Connectée et Profilage Énergétique

Ce dossier contient le code permettant de réaliser une horloge connectée à l'aide d'un Raspberry Pi Pico W et d'un servo moteur. Le système se connecte au réseau Wi-Fi, récupère l'heure exacte via un serveur NTP, et ajuste l'angle du servo moteur pour simuler une aiguille sur un cadran de 12 heures. Il inclut également un script de test pour mesurer la consommation énergétique de la carte dans différents modes d'alimentation via la broche VSYS.

## Structure des fichiers

*   `main.py` : C'est le script principal qui gère la connexion Wi-Fi, la synchronisation de l'heure, la logique de calcul de l'angle et l'enchaînement séquentiel des 4 états de consommation énergétique pour les mesures.
*   `servo.py` : Il s'agit de la librairie requise pour contrôler le servo moteur. Elle encapsule la configuration de la broche PWM à 100Hz et la conversion de l'angle (0-180°) en rapport cyclique.

## Profilage Énergétique (Mesures via PPK2)

Le microcontrôleur a été alimenté de manière autonome via la broche VSYS pour mesurer sa consommation globale selon 4 états distincts :

**1. État 1 : Actif avec Wi-Fi allumé**
La consommation moyenne se situe autour de **50 mA**, avec de très forts pics oscillant entre 140 mA et 200 mA liés aux transmissions radio du module Wi-Fi.

**2. État 2 : Actif sans Wi-Fi**
Après désactivation de la puce réseau, le signal se lisse et la consommation moyenne chute à environ **36 mA**. Seuls le microcontrôleur (RP2040) et le servo sont actifs.

**3. État 3 : Light Sleep**
Le processeur passe en veille, mais la consommation globale stagne à **28,6 mA**.

**4. État 4 : Deep Sleep**
Le processeur est en extinction profonde, mais la consommation reste identique au mode précédent, soit **28,6 mA**.

### Conclusion sur les modes de veille
On remarque qu'il n'y a aucune différence de consommation entre le mode *Light Sleep* et *Deep Sleep* (28,6 mA). Cela s'explique par une très mauvaise conception du régulateur du Pico 2W.
