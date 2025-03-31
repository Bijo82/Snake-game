from turtle import Turtle

ALIGNEMENT = "center"
FONT = "Courier", 18, "normal"

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}",align=ALIGNEMENT,font=(FONT))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}",align=ALIGNEMENT,font=(FONT))

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNEMENT,font=FONT)