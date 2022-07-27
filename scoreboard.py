from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-0, 265)

    def display_score(self):
        self.clear()
        style = ('Courier', 25, 'italic')
        self.write(f"Your score is {self.score}!", font=style, align='center')
        self.score += 1
