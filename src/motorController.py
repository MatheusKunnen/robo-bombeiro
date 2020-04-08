#####################################################
#   @autores:                                        #
#           - Jhonny Kristyan Vaz-Tostes de Assis   #
#           - Matheus Kunnen Ledesma                #
#           - Patricia Abe Turato                   #
#####################################################

# imports
import RPi.GPIO as GPIO
from motor import Motor

class MotorController:
    STOP = 0
    FORWARD = 1
    REVERSE = 2
    
    FAST = 0
    MEDIUM = 1
    SLOW = 2

    def __init__(self, motors_l, motors_r):
        self.motors_l = motors_l
        self.motors_r = motors_r
        self.vel = 0
        self.setVel(self.vel)



    def move(self, direction):
        if (direction == self.STOP):
            self.motors_l.setDirection(Motor.STOP)
            self.motors_r.setDirection(Motor.STOP)
        elif(direction == self.FORWARD):
            self.motors_l.setDirection(Motor.DRIVE)
            self.motors_r.setDirection(Motor.DRIVE)
        elif (direction == self.REVERSE):
            self.motors_l.setDirection(Motor.REVERSE)
            self.motors_r.setDirection(Motor.REVERSE)

    # Deve calcular a velocidade de cada motor para girar, em funcao da 
    # posicao 
    def direction(self, pos):
        pass
        
    # Falta mudar para que calcule a velocidade nova de cada motor em relacao a
    # direcao 
    def setVel(self, vel):
        if (vel == self.FAST):
            self.vel = 90
        elif (vel == self.MEDIUM):
            self.vel = 70
        elif (vel == self.SLOW):
            self.vel = 50

        self.motors_l.setSpeed(self.vel)
        self.motors_r.setSpeed(self.vel)