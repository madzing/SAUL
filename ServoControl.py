class ServoControl():
    def __init__(self,rudderPos,sailPos):
        self.rudderPos = rudderPos
        self.sailPos = sailPos
        self.changeRudderPos(self,self.rudderPos)
        self.changeRudderPos(self,self.sailPos)

    def getCurrentRudderPos(self):
        return self.rudderPos

    def getCurrentSailPos(self):
        return self.sailPos

    def changeRudderPos(self,newPos):
        self.rudderPos = newPos
        #--> steuer den servo über pwm

    def changeSailPos(self,newPos):
        self.sailPos = newPos
        #--> steuer den servo über pwm
