from turtle import Screen, Turtle

class Shape:
    def __init__(self, size, color, x, y, speed=3):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.speed(speed)
        
    def draw(self, times=36, deg=70, length=160):
        for time in range(times):
            self.turtle.left(deg)
            self.turtle.forward(length)
            

if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Shape 9")
    win.setup(width=450 , height=450 , startx=530 , starty=200)
    
    shape = Shape(3, 'red', 70, -100, 3)
    shape.draw()
    
    win.exitonclick()
