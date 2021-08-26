from turtle import Screen, Turtle

class Shape:
    def __init__(self, color, pen_size, x, y, speed=0):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setpos(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(pen_size)
        self.turtle.speed(speed)
        
    def draw(self, length, deg=10, times=40):
        for time in range(times):
            self.draw_shape(length)
            self.turtle.right(deg)

            
    def draw_shape(self, length):
        self.turtle.forward(length+3)
        self.turtle.left(120)
        self.turtle.forward(length)
        self.turtle.right(120)
        self.turtle.forward(length+10)
        self.turtle.right(120)
        self.turtle.forward(length)
        self.turtle.left(120)


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Shape 11')
    root.setup(width=700, height=700)

    shape = Shape('blue', 3, 0, 200)
    shape.draw(20)
    
    root.exitonclick()