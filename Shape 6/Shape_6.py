from turtle import Screen, Turtle

class Shape:
    def __init__(self, size, color, x, y):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.left(11)
        
    def draw(self, times=5):
        for time in range(times):
            self.turtle.circle(500, extent=50)
            self.turtle.circle(50, extent=94)


if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Shape 6")
    win.setup(width=700 , height=700 , startx=400 , starty=80)
    
    shape = Shape(3, 'red', -130, -200)
    shape.draw()
    
    win.exitonclick()
