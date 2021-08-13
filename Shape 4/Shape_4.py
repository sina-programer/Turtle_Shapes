from turtle import Screen, Turtle

class Shape:
    def __init__(self, x, y, size, color):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(size)
        
    def draw(self, times, deg, radius, extent):
        for i in range(times):
            self.turtle.circle(radius, extent)
            self.turtle.left(deg)
        

if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Shape 4")
    win.setup(width=700 , height=700 , startx=350 , starty=80)
    
    t1 = Shape(-200, -50, 3, 'red')
    t1.draw(9, 150, 500, 50)
    
    win.exitonclick()
    