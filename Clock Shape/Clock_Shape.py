from turtle import Screen, Turtle
from time import sleep

class Indicator:
    def __init__(self, color, height, width):
        self.angle = 90
        self.height = height
        
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.setheading(self.angle)
        self.turtle.speed(0)
        self.turtle.color(color)
        self.turtle.pensize(width)
        
        self.turtle.forward(self.height)
        
    def move(self):
        self.angle -= 6
        self.turtle.home()
        self.turtle.clear()
        self.turtle.setheading(self.angle)
        self.turtle.forward(self.height)
        

class Clock:
    def __init__(self, color, radius=150):
        turtle = Turtle()
        turtle.hideturtle()
        turtle.setpos(x=-80, y=130)
        turtle.color(color)
        turtle.speed(5)
        turtle.pensize(2)
        turtle.setheading(210)
        
        for time in range(12):
            turtle.dot()
            turtle.circle(radius, extent=30)
            
        self.hour = Indicator('white', 60, 4)
        self.minute = Indicator('white', 100, 2)
        self.second = Indicator('red', 120, 1)
        
    def start(self):
        while True:
            for m in range(60):
                for s in range(60):
                    sleep(1)
                    self.second.move()
                    
                self.minute.move()
            
            self.hour.move()


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Clock Shape')
    
    clock = Clock('white')
    clock.start()
