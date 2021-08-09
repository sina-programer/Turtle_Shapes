from turtle import Screen, Turtle, done

class Shape:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.pensize(3)
        self.turtle.setheading(5)
        self.turtle.color('red')
        self.go(-60, 60)
        self.turtle.left(36)
                
    def draw(self):
        for i in range(90):
            self.turtle.speed((i//14)+2)
            if i%2:
                self.move()
            else:
                self.move(True)
        
    def move(self, left=False):
        if left:
            self.turtle.left(36)
        else:
            self.turtle.right(140)
        self.turtle.forward(200)
        
    def go(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x=x, y=y)
        self.turtle.pendown()
        

if __name__ == "__main__":
    root = Screen()
    root.title('Star')
    root.bgcolor('black')   

    star = Shape()
    star.draw()
    
    done()