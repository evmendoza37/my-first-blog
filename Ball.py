# 8/9/2021 ball class
#practice OOP within python
class Ball:
    def __init__(self,color,diameter):
        self.color = color
        self.diameter = diameter

    def roll(self,distance):
        self.distance = distance
        print("Ball rolled: "+ str(distance) + "! ")
    def bounce(self,jumps):
        self.jumps = jumps
        print("Ball bounced: " + str(jumps) + "! ")

myfavball = Ball('marble blue', 3) #create ball
print(myfavball.color)
print (str(myfavball.diameter))

myfavball.roll(5)
myfavball.bounce(2)
