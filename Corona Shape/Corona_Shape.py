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
        
    def draw(self, times=210):
        deg = 0
        length = 0
        for time in range(times):
            self.turtle.forward(length)
            self.turtle.right(deg)
            length += 3
            deg += 1


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Corona Shape')
    root.setup(width=700, height=700)
    
    corona = Shape('green', 1, 0, 200)
    corona.draw()

    root.exitonclick()
