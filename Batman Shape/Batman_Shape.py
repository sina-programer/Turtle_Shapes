from turtle import Screen, Turtle

class Shape:
    def __init__(self):
        self.zoom = 30
        
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color('red')
        self.turtle.pensize(3)
        self.turtle.speed(0)
        
        self.turtle.penup()
        self.turtle.goto(-210, 0)
        self.turtle.pendown()
        
    def draw(self):
        self.draw_big_edge_up(-7*self.zoom, -3*self.zoom)
        
        self.draw_small_edge(-3*self.zoom, -self.zoom-1)
        
        self.turtle.goto(-self.zoom,3*self.zoom)
        self.turtle.goto(int(-0.5*self.zoom),int(2.2*self.zoom))
        self.turtle.goto(int(0.5*self.zoom),int(2.2*self.zoom))
        self.turtle.goto(1*self.zoom,3*self.zoom)
        
        self.draw_small_edge(self.zoom+1, 3*self.zoom+1)
        
        self.draw_big_edge_up(3*self.zoom+1, 7*self.zoom+1)
        
        self.draw_big_edge_down(7*self.zoom, 4*self.zoom)

        for xz in range(4*self.zoom, -4*self.zoom, -1):
            x = xz/self.zoom
            absx = abs(x)
            y = abs(x/2)-0.0913722 * x**2 -3 + ((1-(abs(absx-2)-1)**2)**.5)
            self.turtle.goto(xz, y*self.zoom)

        self.draw_big_edge_down(-4*self.zoom-1, -7*self.zoom-1)

    def draw_big_edge_up(self, start, stop):
        for xz in range(start, stop):
            x = xz/self.zoom
            absx = abs(x)
            y = 1.5 * (((-abs(absx-1)) * abs(3-absx) / ((absx-1)*(3-absx)))**.5) * ((1-(x/7)**2)**.5)*2
            self.turtle.goto(xz, y*self.zoom)

    def draw_big_edge_down(self, start, stop):
        for xz in range(start, stop, -1):
            x = xz/self.zoom
            absx = abs(x)
            y = -3 * ((1-(x/7)**2)**.5) * ((abs(absx-4)/(absx-4))**.5)
            self.turtle.goto(xz, y*self.zoom)        

    def draw_small_edge(self, start, stop):
        for xz in range(start, stop):
            x = xz/self.zoom
            absx = abs(x)
            y = (4.21052 - (absx/2) - 1.35526 * ((4-(absx-1)**2)**.5)) * ((abs(absx-1)/(absx-1))**.5)
            self.turtle.goto(xz, y*self.zoom)


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Batman Shape')

    shape = Shape()
    shape.draw()

    root.exitonclick()
