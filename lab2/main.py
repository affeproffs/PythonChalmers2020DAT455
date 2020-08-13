# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *

# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, angle, vel):
    player = game.getCurrentPlayer()

    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj

def graphicPlay():
    game = Game(10, 3)
    gGame = GraphicGame(game)

    while True:
        inputBox = InputDialog(game.getCurrentPlayer().getAim()[0],
                               game.getCurrentPlayer().getAim()[1],
                               game.getCurrentWind())
        
        if (inputBox.interact() == "Fire!"):
            angle, vel = inputBox.getValues()
            inputBox.close()
        else:
            return
            
        proj = graphicFire(gGame, angle, vel)
        if (gGame.getOtherPlayer().projectileDistance(proj) == 0):
            gGame.getCurrentPlayer().increaseScore()
            gGame.newRound()
            
        gGame.nextPlayer()

graphicPlay()
