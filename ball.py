from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.accelerate = .1

    def move(self):
        new_x_coordinate = self.xcor() + self.x_move
        new_y_coordinate = self.ycor() + self.y_move
        self.goto(new_x_coordinate, new_y_coordinate)
    
    #causes ball to 'bounce' whenever it hits an upper or lower boundary
    def bounce_y(self):
        self.y_move *= -1
    
    #causes ball to 'bounce' and speed up whenever it hits a paddle
    def bounce_x(self):
        self.x_move *= -1
        self.accelerate *= .9
    
    def position_reset(self):
        self.goto(0,0)
        self.accelerate = .1
        self.bounce_x()

