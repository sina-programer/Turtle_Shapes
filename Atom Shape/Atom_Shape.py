from turtle import Screen, Turtle
import random

class Shape:
    def __init__(self):
        self.turtles = [
                        self.init_turtle('red', 0, -170, -130), 
                        self.init_turtle('blue', 110, 170, -100),
                        self.init_turtle('purple', 55, 10, -210)
                        ]
        
    def draw(self, times=30):
        for time in range(times):
            turtle = random.choice(self.turtles)
            turtle.circle(500, extent=50)
            turtle.circle(75, extent=130)
            
    def init_turtle(self, color, deg, x, y):
        turtle = Turtle(shape="circle")
        turtle.penup()
        turtle.setpos(x=x , y=y)
        turtle.pendown()

        turtle.color(color)
        turtle.left(deg)
        turtle.pensize(3)
        turtle.speed(10)

        return turtle


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Atom Shape')
    
    shape = Shape()
    shape.draw()

    root.exitonclick()
