from turtle import Turtle
FONT = ("Courier", 80, "normal")
CENTER = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.left_score, align=CENTER, font= FONT)
        self.goto(100, 300)
        self.write(self.right_score, align=CENTER, font=FONT)


    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()
    
    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER", False, CENTER, FONT)
