from turtle import Turtle

ALIGNEMENT = "center"
FONT = "Courier", 18, "normal"

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            hs = file.read()
        self.highscore = int(hs)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}\t High Score : {self.highscore}", align=ALIGNEMENT, font=(FONT))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        with open("data.txt",mode="w") as file:
            file.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()