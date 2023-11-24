import time
from animationHelpers import wheel

class FigureLedLine():

    def __init__(self, ledLineList):
        self.ledLinesList = ledLineList
        self.lenght = len(self.ledLinesList)

    def fill(self, r, g, b):
        for line in self.ledLinesList:
            line.fill(r, g, b)

    def off(self):
        for line in self.ledLinesList:
            line.fill(0, 0, 0)

    def rainbow(self, wait):
        for line in self.ledLinesList:
            line.rainbow()
            time.sleep(wait)

    def show(self):
        for line in self.ledLinesList:
            line.neopixel.show()

class TriangleLed(FigureLedLine):

    def __init__(self,line1, line2, line3):
        super().__init__([line1, line2, line3])

class SquareLed(FigureLedLine):

    def __init__(self,line1, line2, line3, line4):
        super().__init__([line1, line2, line3, line4])


class HexagonLed(FigureLedLine):

    def __init__(self,line1, line2, line3, line4, line5, line6):
        super().__init__([line1, line2, line3, line4, line5, line6])

