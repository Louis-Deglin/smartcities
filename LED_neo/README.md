Module Capteurs et Actionneurs : LED RGB, Micro et Ventilateur

Ce fichier contient les codes Python avec d'abord les exercices pour s'entraîner (tests de LED RGB, ventilateur avec bouton/relais, et veilleuse intelligente via capteurs de son/lumière) et ensuite le code de l'exercice 4.

Exercice demandé : Contrôle d'une LED RGB en fonction du rythme de la musique (Exercice 4)

Comportement programmé :

Écoute continue de l'environnement via le capteur de son (Microphone).

Détection de battement : Lorsqu'un pic sonore dépasse le seuil défini (30000), la LED RGB affiche une nouvelle couleur générée aléatoirement.

Stabilisation : Un délai anti-rebond de 250 ms est appliqué entre chaque détection pour éviter les changements de couleur multiples sur un même battement.
