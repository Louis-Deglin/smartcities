from machine import Pin, PWM

class Servo:
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(100)

    def turn(self, angle):
        # Mappage linéaire : 0° -> 4000 (12h/00:00) et 180° -> 16500
        duty = int(4000 + (angle / 180) * 12500)
        self.pwm.duty_u16(duty)
        return duty
