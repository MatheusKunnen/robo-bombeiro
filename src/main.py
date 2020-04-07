#####################################################
#   @author:                                        #
#           - Jhonny Kristyan Vaz-Tostes de Assis   #
#           - Matheus Kunnen Ledesma                #
#           - Patricia Abe Turato                   #
#####################################################

# imports
from motorController import MotorController
from distanceSensor import DistanceSensor
from fireDetector import FireDetector

#   @desc: controlar o funcionamento integro do robo
class Main:
    def __init__(self):
        self.motor_controller = MotorController()
        self.distanceSensor = DistanceSensor()
        self.fire_detector = FireDetector()


exit(0)