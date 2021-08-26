from turtle import Screen, Turtle

class Flake:
    def __init__(self, x, y):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.speed(0)
        self.turtle.color('white')
        
    def draw(self, length, level):
        for time in range(3):
            self.draw_flake(length, level)
            self.turtle.right(120)
         
    def draw_flake(self, length, level):
        if not level:
            self.turtle.forward(length)
            return
        
        length /= 3
        
        self.draw_flake(length, level-1)
        self.turtle.left(60)
        
        self.draw_flake(length, level-1)
        self.turtle.right(120)
        
        self.draw_flake(length, level-1)
        self.turtle.left(60)
        
        self.turtle.forward(length)


levels = 4
length = 300

if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Flake")
    win.setup(width=600 , height=600 , startx=400 , starty=130)
    
    flake = Flake(-length/2, 100)
    flake.draw(length, levels)
    
    win.exitonclick()
