import turtle


t= turtle.Turtle()

class Disk(object):
    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        
        
        
    
    def showdisk(self):
        tempx = self.dxpos - self.dwidth/2
        tempy = self.dypos - self.dheight/2
        self.t= turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(tempx,tempy)
        self.t.pendown()
        self.t.goto(tempx+self.dwidth,tempy)
        self.t.goto(tempx+self.dwidth,tempy+self.dheight)
        self.t.goto(tempx,tempy+self.dheight)
        self.t.goto(tempx,tempy)
        self.t.penup()

    def cleardisk(self):
        self.t.reset()

    def newpos(self,x,y):
        self.dxpos = x
        self.dypos = y
        self.cleardisk()
        self.showdisk()

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


        






t.screen.mainloop()


# import turtle

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t1.circle(50)
# t2.forward(100)

# # Clear the entire screen and remove all turtles
# t1.reset()

# turtle.done()

class Hanoi(object):
    def init(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)


h = Hanoi()
h.solve()