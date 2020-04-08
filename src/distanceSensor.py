#####################################################
#   @autores:                                        #
#           - Jhonny Kristyan Vaz-Tostes de Assis   #
#           - Matheus Kunnen Ledesma                #
#           - Patricia Abe Turato                   #
#####################################################

class DistanceSensor:
    def __init__(self, pin_echo, pin_trigger):
        self.pin_echo = pin_echo
        self.pin_trigger = pin_trigger
        self.initPinout()

    def initPinout(self):
        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)

    # Codigo adaptado de https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
    # OBS: Adicionar no relatorio referencia do codigo
    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.pin_trigger, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.pin_trigger, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(self.pin_echo) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(self.pin_echo) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = TimeElapsed * 17500.0
    
        return distance