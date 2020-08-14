#------------------------------------------------------
#This module contains all graphics-classes for the game
#Most classes are wrappers around model classes, e.g. 
#  * GraphicGame is a wrappoer around Game
#  * GraphicPlayer is a wrapper around Player
#  * GraphicProjectile is a wrapper around Projectile
#In addition there are two UI-classes that have no 
#counterparts in the model:
#  * Button
#  * InputDialog
#------------------------------------------------------
from graphics import *

class GraphicGame:
    def __init__(self, game):
        self.win = GraphWin("Cannon game" , 640, 480, autoflush=False)
        self.win.setCoords(-110, -10, 110, 155)
        self.game = game
        self.game.setPlayers([GraphicPlayer(self.getCurrentPlayer(), self),
                              GraphicPlayer(self.getOtherPlayer(), self)])
        
        horiLine = Line(Point(-110, 0), Point(110, 0))
        horiLine.draw(self.win)

    def setCurrentWind(self, wind):
        return self.game.setCurrentWind(wind)

    def getWindow(self):
        return self.win

    def __getattr__(self, name):
        return getattr(self.game, name)

class GraphicPlayer:
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.proj = None
        
        p1 = Point(player.x - game.getCannonSize() / 2, game.getCannonSize())
        p2 = Point(player.x + game.getCannonSize() / 2, 0)        
        pRect = Rectangle(p1, p2)
        pRect.setFill(player.getColor())
        pRect.setOutline(player.getColor())
        pRect.draw(self.game.getWindow())

        self.scoreGraphic = Text(Point(self.getX(), -5), "Score: 0")
        self.scoreGraphic.draw(game.getWindow())
    
    def fire(self, angle, vel):
        proj = self.player.fire(angle, vel)
        
        if self.proj:
            self.proj.undraw()

        self.proj = GraphicProjectile(proj, self.game, self.getColor())
        return self.proj

    def projectileDistance(self, proj):
        return self.player.projectileDistance(proj)
        
    def increaseScore(self):
        self.player.increaseScore()
        self.scoreGraphic.setText("Score: " + str(self.getScore()))

    def __getattr__(self, name):
        return getattr(self.player, name)

""" A graphic wrapper around the Projectile class (adapted from ShotTracker in book)"""
class GraphicProjectile:
    def __init__(self, proj, game, color):
        self.proj = proj
        self.game = game

        graphic = Circle(Point(proj.getX(), proj.getY()), game.getBallSize())
        graphic.setOutline(color)
        graphic.setFill(color)        
        graphic.draw(game.getWindow())
        
        self.graphic = graphic

    def update(self, dt):
        oldX, oldY = self.proj.getX(), self.proj.getY()        
        self.proj.update(dt)        
        newX, newY = self.proj.getX(), self.proj.getY()
        self.graphic.move(newX - oldX, newY - oldY)

    def undraw(self):
        self.graphic.undraw()

    def __getattr__(self, name):
        return getattr(self.proj, name)
        

""" A somewhat specific input dialog class (adapted from the book) """
class InputDialog:
    """ Takes the initial angle and velocity values, and the current wind value """
    def __init__ (self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0,4.5,4,.5)
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))
        
        Text(Point(1,3), "Wind").draw(win)
        self.height = Text(Point(3,3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))
        
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    """ Runs a loop until the user presses either the quit or fire button """
    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    """ Returns the current values of (angle, velocity) as entered by the user"""
    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a,v

    def close(self):
        self.win.close()

""" A general button class (from the book) """
class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0
