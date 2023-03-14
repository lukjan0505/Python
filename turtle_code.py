import turtle
t = turtle.Turtle()

# set the turtle's pen size
t.pensize(3)

# set the number of steps for the loop
steps = 20

# initialize a variable to keep track of the current step
current_step = 0

# move the turtle forward and leave a mark
t.pendown()
while current_step < steps:
    t.forward(5)
    t.penup()
    t.forward(5)
    current_step += 1 
    turtle.done()