from turtle import Screen, Turtle

    
class Shape:
    def __init__(self, size, color, x, y, speed=2, deg=False):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.speed(speed)
        
        if deg:
            self.turtle.left(deg)

    def draw(self):
        self.draw_oct()
        self.draw_triangles()
        self.draw_lines()
        
    def draw_oct(self):
        for side in range(8):
            self.turtle.left(45)
            self.turtle.forward(100)
            
    def draw_triangles(self):
        self.turtle.color('cyan')
        for time in range(16):
            if not time:
                self.turtle.right(15)
            elif time%2:
                self.turtle.left(120)
            else:
                self.turtle.right(75)
                
            self.turtle.forward(100)
            
    @classmethod
    def draw_lines(cls):
        xs = [50, -50, 120, -120, 120, -120, 50, -50]
        ys = [-100, -100, -30, -30, 70, 70, 140, 140]
        degs = [112, 68, 157, 23, 203, 337, 248, 292]
        turtles = [ cls(4, 'purple', xs[idx], ys[idx], deg=degs[idx]) for idx in range(len(xs))]

        for time in range(65):
            for turtle in turtles:
                turtle.turtle.forward(2)
                
        for idx, turtle in enumerate(turtles):
            turtle.go(xs[idx]*-1, ys[len(ys)-idx-1])
        
        for time in range(80):
            for turtle in turtles:
                turtle.turtle.forward(3)
        
    def go(self, x, y):      
        self.turtle.penup()
        self.turtle.goto(x=x, y=y)
        self.turtle.pendown()
        self.turtle.left(157)



if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Shape 9")
    win.setup(width=600 , height=600 , startx=400 , starty=130)
    
    shape = Shape(4, 'blue', 50, -100)
    shape.draw()
    
    win.exitonclick()
