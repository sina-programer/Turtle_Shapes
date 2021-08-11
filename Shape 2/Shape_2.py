from turtle import Screen, Turtle

class Shape:
    def __init__(self, color, pen_size, x, y, speed=2):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.setpos(x=x , y=y)
        self.turtle.color(color)
        self.turtle.pensize(pen_size)
        self.turtle.speed(speed)
        
    def draw(self, time, deg, length):
        for i in range(time):
            self.turtle.left(deg)
            self.turtle.forward(length)


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Shape 2')
    root.setup(width=600, height=600)
    
    shape1 = Shape('blue', 4, 200, -10)
    shape1.draw(12, 150, 400)
    
    shape2 = Shape('red', 2, 45, 15)
    shape2.draw(13, 111, 85)

    root.exitonclick()
