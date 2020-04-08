#####################################################
#   @autores:                                        #
#           - Jhonny Kristyan Vaz-Tostes de Assis   #
#           - Matheus Kunnen Ledesma                #
#           - Patricia Abe Turato                   #
#####################################################

# imports
import RPi.GPIO as GPIO

class Motor:
    # Direcoes do motor
    STOP = 0
    DRIVE = 1
    REVERSE = 2
    def __init__(self, in01, in02, en):
        self.in01 = in01        # Pino direcao 1
        self.in02 = in02        # Pino direcao 2
        self.en = en            # Pino velocidade
        self.vel = 0            # Velocidade inicial
        self.initPinout()       
        
    def initPinout(self):  
        # Mapeamento dos pinos 
        GPIO.setup(self.in01,GPIO.OUT)
        GPIO.setup(self.in02,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        # Init GPIO States
        self.setDirection(Motor.STOP)
        self.setVel(self.vel)
        
    def setDirection(self, direction):  # Controle de direcao de rotacao do motor
        if (direction == self.STOP):
            GPIO.output(self.in01, GPIO.LOW)
            GPIO.output(self.in02, GPIO.LOW)
        elif (direction == self.REVERSE):
            GPIO.output(self.in01, GPIO.HIGH)
            GPIO.output(self.in02, GPIO.LOW)
        elif (direction == self.DRIVE):
            GPIO.output(self.in01, GPIO.LOW)
            GPIO.output(self.in02, GPIO.HIGH)
            
    def setVel(self, vel):  # Controle de velocidade de rotacao
        self.vel = vel
        self.pwm.ChangeDutyCycle(vel)