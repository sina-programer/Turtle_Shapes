from turtle import Screen, Turtle

class Shape:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.color('white')
        
    def draw(self):
        for i in range(430):
            self.turtle.forward(i)
            self.turtle.right(50)
         

if __name__ == "__main__":
    root = Screen()
    root.bgcolor("black")
    root.title("Spiral Tunnel Shape")
    # root.setup(width=600 , height=600 , startx=400 , starty=130)
    
    shape = Shape()
    shape.draw()
    
    root.exitonclick()
