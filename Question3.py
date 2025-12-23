import turtle


t= turtle.Turtle()
t.speed(0)

class Disk:
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    def showDisk(self):
        t.pencolor("black")
        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)

        t.down()
        t.forward(self.dwidth//2)
        t.left(90)
        t.forward(self.dheight)
        t.left(90)
        t.forward(self.dwidth)
        t.left(90)
        t.forward(self.dheight)
        t.left(90)
        t.forward(self.dwidth//2)

        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)
    def newpos(self, xpos, ypos):
        self.clearDisk()

        self.dxpos = xpos
        self.dypos = ypos
        
    def clearDisk(self):
        t.color("white")
        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)

        t.down()
        t.backward(self.dwidth//2)
        t.right(90)
        t.backward(self.dheight)
        t.right(90)
        t.backward(self.dwidth)
        t.right(90)
        t.backward(self.dheight)
        t.right(90)
        t.backward(self.dwidth//2)

        t.setheading(0)
        t.up()
        t.goto(self.dxpos, self.dypos)

class Pole:
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.thick = thick
        self.length = length

        self.stack = []
        self.toppos = 0
    def showPole(self):
        t.pu()
        t.goto(self.xpos, self.ypos)
        t.pd()
        t.forward(self.thick / 2)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.thick)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.thick / 2)
    def pushDisk(self, disk):
        if disk:
            disk.newpos(self.xpos, self.ypos + self.toppos*20)
            self.stack.append(disk)
            self.toppos += 1
            disk.showDisk()
        
    def popDisk(self):
        print("popping from", self.name)
        if len(self.stack) != 0:
            disk = self.stack.pop()
            self.toppos -= 1
            disk.clearDisk()
            disk.newpos(disk.dxpos, 120)
            disk.showDisk()
            return disk


        





class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showPole()
        self.workspacep.showPole()
        self.destinationp.showPole()
        for i in range(n):
            self.startp.pushDisk(Disk("d"+str(i),0,i*150,20,(n-i)*30))

    def move_disk(self,start,destination):
        disk = start.popDisk()
        destination.pushDisk(disk)
    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)
    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)

h = Hanoi()
h.solve()




