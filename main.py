class Bulb:
    status = False

    def isOn(self):
        self.status = True

    def isOff(self):
        self.status = False

    def getStatus(self):
        if self.status==True:
            return "Bulb is Glowing"
        elif self.status == False:
            return "Bulb is Glowing"
        else:
            pass