from turtle import Screen, Turtle

class Star:
    def __init__(self, x, y, pen_size, speed, colors):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.setpos(x=x , y=y)
        self.turtle.pensize(pen_size)
        self.turtle.speed(speed)
        self.colors = colors
        
    def draw(self, times=5, deg=144, length=300):
        for time in range(times):
            for side in range(5):
                try:
                    self.turtle.color(self.colors[side+time])
                except:
                    self.turtle.color(self.colors[side-(4-time)])
                    
                self.turtle.forward(length)
                self.turtle.right(deg)
                
                if time==times-1 and side==4:
                    self.turtle.color(self.colors[0])                    
                    self.turtle.forward(length)


colors = ['red', 'blue', 'green', 'white', 'purple']
if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Shape 3')
    root.setup(width=600, height=600)
    
    star = Star(-140, 80, 5, 3, colors)
    star.draw()

    root.exitonclick()