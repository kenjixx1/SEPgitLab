import turtle


t= turtle.Turtle()

class Disk(object):
    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.t= turtle.Turtle()
        
    
    def showdisk(self):
        self.t= turtle.Turtle()
        self.t.penup()
        self.t.goto(self.dxpos,self.dypos)
        self.t.pendown()
        self.t.goto(self.dxpos+self.dwidth,self.dypos)
        self.t.goto(self.dxpos+self.dwidth,self.dypos+self.dheight)
        self.t.goto(self.dxpos,self.dypos+self.dheight)
        self.t.goto(self.dxpos,self.dypos)
        self.t.penup()

    def cleardisk(self):
        self.t.reset()

    def newpos(self,x,y):
        self.dxpos = x
        self.dypos = y
        self.cleardisk()
        self.showdisk()


        

h=Disk(xpos=30,ypos=50)
h.showdisk()

a=Disk(xpos=100,ypos=50)
a.showdisk()


h.newpos(200,300)

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