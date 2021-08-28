from turtle import Screen, Turtle

class Shape:
    def __init__(self, x, y):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.speed(10)
        self.turtle.pensize(3)
        self.turtle.color('white')
        
    def draw(self, length=150):
        for time in range(8):
            self.turtle.forward(length)
            self.turtle.circle(40, 315)


if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Shape 13")
    win.setup(width=600 , height=600 , startx=400 , starty=130)
    
    shape = Shape(-90, 150)
    shape.draw()
    
    win.exitonclick()
