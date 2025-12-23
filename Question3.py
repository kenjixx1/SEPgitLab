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


