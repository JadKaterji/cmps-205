# Assignment 6 part 3
import turtle

def tree(n,a,b):
        if  n == 0:
                turtle.pensize(b)
                turtle.forward(a)
                turtle.backward(a)
        
        else:
                turtle.pensize(b)
                turtle.forward(a)
                turtle.left(40)
                tree(n-1,a/2,b/2)
                turtle.right(25)
                tree(n-1,a/4,b/2)
                turtle.right(40)
                tree(n-1,a/2,b/2)
                turtle.left(25)
                turtle.backward(a)
turtle.left(90)
turtle.speed(100)


tree(4,100,7)

turtle.done()