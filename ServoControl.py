class ServoControl():
    def __init__(self,rudderPos,sailPos):
        self.rudderPos = rudderPos
        self.sailPos = sailPos
        self.rudderPos = 6
        self.sailPos = 6
        self.rudderMax = 8
        self.rudderMin = 2

    def getCurrentRudderPos(self):
        return self.rudderPos

    def getCurrentSailPos(self):
        return self.sailPos

    def turn(self,desiredWinkelgesch,winkelgesch):
        if self.rudderPos < self.rudderMax:
            self.rudderPos = self.rudderPos + 0.1

    def changeSailPos(self,newPos):
        self.sailPos = newPos
        #--> steuer den servo über pwm
