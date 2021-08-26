from turtle import Screen, Turtle

    
class Shape:
    def __init__(self, x, y):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.pensize(1)
        self.turtle.speed(0)
        self.turtle.color('white')
         
    def draw_star(self, length, level):
        if level == 0:
            return 
        
        for side in range(5):
            self.turtle.forward(length)
            self.turtle.right(144)
            
            self.draw_star(length/3, level-1)


levels = 4
length = 300

if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Stars")
    win.setup(width=600 , height=600 , startx=400 , starty=130)
    
    shape = Shape(-150, 50)
    shape.draw_star(length, levels)
    
    win.exitonclick()
