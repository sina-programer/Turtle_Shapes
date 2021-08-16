from turtle import Screen, Turtle

class Shape:
    def __init__(self, size, color, x, y, speed=0):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.speed(speed)
        
    def draw(self, times=30):
        for time in range(times):
            for side in range(4):
                self.draw_line()
                
            self.turtle.right(12)
            
    def draw_line(self, length=100, deg=90):
        self.turtle.forward(length)
        self.turtle.left(deg)


if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Shape 7")
    win.setup(width=410 , height=410 , startx=550 , starty=230)
    
    shape = Shape(3, 'yellow', 0, 0)
    shape.draw()
    
    win.exitonclick()
