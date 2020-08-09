from math import sin,cos,radians
import random

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.players = [Player(self, (45, 40), -90, "blue"), Player(self, (-45, 40), 90, "red")]
        self.currentPlayer = 0
        self.newRound()

    """ A list containing both players """
    def getPlayers(self):
        return self.players

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.cannonSize

    """ The radius of cannon balls """
    def getBallSize(self):
        return self.ballSize        

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.players[self.currentPlayer]

    """ The opponent of the current player """
    def getOtherPlayer(self):
        return self.players[0] if self.currentPlayer else self.players[1]
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.currentPlayer
    
    """ Switch active player """
    def nextPlayer(self):
        self.currentPlayer += 1 if not self.currentPlayer else -1

    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        self.wind = wind
    
    def getCurrentWind(self):
        return self.wind

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        self.setCurrentWind(random.randint(-10, 10))
        
""" Models a player """
class Player:
   #HINT: It should probably take the Game that creates it as parameter and some additional properties that differ between players (like firing-direction, position and color)
    def __init__(self, game, firingDir, x, color):
        self.game = game
        self.firingDir = firingDir
        self.x = x
        self.color = color
        self.score = 0
    
    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        self.projectile = Projectile(angle, velocity, self.game.getCurrentWind(), self.x,
                                     self.game.getCannonSize() / 2, -110, 110)
        self.firingDir = (angle, velocity)

        return self.projectile

    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        # HINT: both self (a Player) and proj (a Projectile) have getX()-methods.
        # HINT: This method should give a negative value if the projectile missed to the left and positive if it missed to the right.
        # The distance should be how far the projectile and cannon are from touching, not the distance between their centers.
        # You probably need to use getCannonSize and getBallSize from Game to compensate for the size of cannons/cannonballs
        projLower = proj.getX() - self.game.getBallSize() / 2
        projUpper = proj.getX() + self.game.getBallSize() / 2
        
        playerLower = self.getX() - self.game.getCannonSize() / 2
        playerUpper = self.getX() + self.game.getCannonSize() / 2

        print(playerLower, playerUpper)
        print(projLower, projUpper)
        print(playerLower - projUpper, playerUpper - projUpper,
              projLower - playerLower, playerUpper - projLower)

    """ The current score of this player """
    def getScore(self):
        return self.score

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self.score += 1

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.x

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return self.firingDir[0], self.firingDir[1]



""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind


    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos
