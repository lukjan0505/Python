from turtle import Turtle

t=Turtle()

def square():
    t.up()
    t.setpos(-50,-50)
    t.down()
    for i in range(4):
        t.forward(100)
        t.right(90)

def triangle():
    t.up()
    t.setpos(50,50)
    t.down()
    for i in range(3):
        t.forward(100)
        t.right(120)

def star():
    t.up()
    t.setpos(-200,100)
    t.down()
    for i in range(5):
        t.forward(150)
        t.right(144)

square()
triangle()
star()
t.screen.done()