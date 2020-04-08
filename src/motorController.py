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
    # Direcoes possiveis 
    STOP = 0
    FORWARD = 1
    REVERSE = 2
    
    # Velocidade predeterminadas 
    FAST = 0
    MEDIUM = 1
    SLOW = 2

    # Velocidade Maxima e Minima dos motores 
    MAX_VEL = 100
    MIN_VEL = 40

    # Constante de ajuste e sensibilidade a variacoes da direcao
    DIR_K = 1/100

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

    # @desc: Calcula a velocidade de cada motor para girar, em funcao da posicao 
    # @param: int pos, variacao da direcao
    #               pos = 0 => sem variacao de velocidad e entre motores
    #               pos > 0 => gira a direita
    #               pos < 0 => gira a esquerda
    def direction(self, pos):
        self.pos = pos

        vel_l = self.vel + self.pos*MotorController.DIR_K
        if (vel_l < MotorController.MIN_VEL):
            vel_l = MotorController.MIN_VEL
        elif(vel_l > MotorController.MAX_VEL):
            vel_l= MotorController.MAX_VEL
        
        vel_r = self.vel - self.pos*MotorController.DIR_K
        if (vel_r < MotorController.MIN_VEL):
            vel_r = MotorController.MIN_VEL
        elif(vel_r > MotorController.MAX_VEL):
            vel_r= MotorController.MAX_VEL

        self.motors_l.setVel(vel_l)
        self.motors_r.setVel(vel_r)
        
        
    def setVel(self, vel):
        if (vel == self.FAST):
            self.vel = 90
        elif (vel == self.MEDIUM):
            self.vel = 70
        elif (vel == self.SLOW):
            self.vel = 50

        self.motors_l.setVel(self.motors_l.vel^2/self.vel)
        self.motors_r.setVel(self.motors_r.vel^2/self.vel)