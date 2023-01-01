


import turtle
import random

greg = turtle.Turtle()


def branch(t,l,d,a):  ## turtle len depth
    if d == 0:       ## this is the exit condition and size of lines that make up koch
        return            ##  it defacto sets the level
    else:
        t.forward(l)
        
        t.right(a)
        branch(t,l*0.67,d-1,a)

        
        t.left(2*a)
        branch(t,l*0.67,d-1,a)

        t.right(a)
        t.forward(-l)


greg.right(-90)
branch(greg,100,6,25)

turtle.exitonclick()

