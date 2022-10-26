#A class for a score object that will be displayed at the top of the screen
import pyray

class Score:

    #The only variable for this class is the score
    def __init__(self):
        self.currentScore = 0

    #Adds a given point value to the score
    def updateScore(self, points):
        self.currentScore += points
        return self.currentScore

    #Converts score to a string, then prints it on the screen
    def drawScore(self):
        text = "SCORE: " + str(self.currentScore)
        x = 0
        y = 0
        fontSize = 20
        color = [255, 255, 255, 255]

        pyray.draw_text(text, x, y, fontSize, color)
