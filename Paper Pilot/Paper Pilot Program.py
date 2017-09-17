#######################
## PAPER PILOT V 4.0 ##
#######################

#BY:            Alex Vucicevich
#CLASS:         ICS3UI
#PROJECT:       Final Project: Game Project
#FINAL EDIT:    22/01/2016 @ 11:30pm
#FILE SIZE:     71.3Mb

#############
## IMPORTS ##
#############

from tkinter import *
from math import *
from time import *
from random import *

import winsound
from Levels import levels

root = Tk()
screen = Canvas(root, width=500, height=800, background="black")
root.title("Paper Pilot")
root.iconbitmap("shipIcon.ico")

####################
## INITIAL VALUES ##
####################

def setInitialValues():
#Global variables 
    global xPlayer, yPlayer, ySpeed, xSpeed, maxSpeed, xMouse, yMouse, player
    global gameRunning, frame
    global bulletlist, generatorlist
    global bullet, currentLevel, background, ship, shipLeft, shipRight, prevXMouse, shipLag, currentShip, currentLives, shipSmall, level, previousLevel, gameOver, currentPic, title, selectLevel
    global zero, one, two, three, four, five, six, seven, eight, nine, ten, bulletInsta, times, earth
    global help1, help2, help3, lives, quitGame, pauseGame, backCheck, mouse, mouseDirections
    global paused, maxLives
    global thanks1, thanks2, thanks3
    global levelSelectCheck, gameOverCheck, beatLevelCheck, backCheck, helpMenuCheck

#Image variables   
    bullet = PhotoImage(file = "bullet.gif")
    bulletInsta = PhotoImage(file = "bulletInsta.gif")
    background = PhotoImage(file = "paperbg.gif")

    ship = PhotoImage(file = "ship.gif")
    shipLeft = PhotoImage(file = "ship1left.gif")
    shipRight = PhotoImage(file = "ship1right.gif")
    shipSmall = PhotoImage(file = "shipSmall.gif")

    level = PhotoImage(file = "Level.gif")
    zero = PhotoImage(file = "Zero.gif")
    one = PhotoImage(file = "One.gif")
    two = PhotoImage(file = "Two.gif")
    three = PhotoImage(file = "Three.gif")
    four = PhotoImage(file = "Four.gif")
    five = PhotoImage(file = "Five.gif")
    six = PhotoImage(file = "Six.gif")
    seven = PhotoImage(file = "Seven.gif")
    eight = PhotoImage(file = "Eight.gif")
    nine = PhotoImage(file = "Nine.gif")
    ten = PhotoImage(file = "Ten.gif")

    times = PhotoImage(file = "x.gif")

    gameOver = PhotoImage(file = "GameOver.gif")
    title = PhotoImage(file = "Title.gif")

    help1 = PhotoImage(file = "help1.gif")
    help2 = PhotoImage(file = "help2.gif")
    help3 = PhotoImage(file = "BulletHelp.gif")
    quitGame = PhotoImage(file = "quit.gif")
    pauseGame = PhotoImage(file = "pause.gif")
    mouse = PhotoImage(file = "helpMouse.gif")
    mouseDirections = PhotoImage(file = "mouseD.gif")

    selectLevel = PhotoImage(file = "SelectLevel.gif")
    earth = PhotoImage(file = "Earth.gif")

    thanks1 = PhotoImage(file = "Thanks1.gif")
    thanks2 = PhotoImage(file = "Thanks2.gif")
    thanks3 = PhotoImage(file = "Thanks3.gif")

#Check Variables
    levelSelectCheck = 0
    gameOverCheck = 0
    beatLevelCheck = 0
    backCheck = 0
    helpMenuCheck = 0

    paused = False

#Appending Images
    lives = []

    lives.append(zero)
    lives.append(one)
    lives.append(two)
    lives.append(three)
    lives.append(four)
    lives.append(five)
    lives.append(six)
    lives.append(seven)
    lives.append(eight)
    lives.append(nine)
    lives.append(ten)

#Frame variable
    frame = 0

#Bullet/Generator list arrays
    bulletlist = []
    generatorlist = []


#Player related variables
    xPlayer = 250
    yPlayer = 400

#Player speed related variables      
    xSpeed = 0
    ySpeed = 0
    maxSpeed = 10
    xMouse = 250
    yMouse = 600
    player = 0

#Ship Related Variables
    prevXMouse = 0
    shipLag = 5
    currentShip = ship

#gameRunning variables    
    gameRunning = True
    currentLives = 3
    maxLives = 3

    previousLevel = 0
    currentPic = 0

##############################
##BULLET / GENERATOR CLASSES##
##############################

#Bullets keep track of own position
#Bullets keep track of own Speeds
#Draws Bullets onto Screen
class Bullet():
    def __init__(self, xPos, yPos, xSpeed, ySpeed, image):
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.image = image
        self.eBullet = None
        self.dead = False

    def draw(self):
        self.eBullet = screen.create_image(self.xPos, self.yPos, image=self.image)

    def update(self):
        self.xPos = self.xPos + self.xSpeed
        self.yPos = self.yPos + self.ySpeed

        self.delete()

    def delete(self):
        screen.delete(self.eBullet)

    def checkOOB(self):
        if self.yPos > 800 or self.yPos < 0 or self.xPos < 0 or self.xPos > 500:
            self.dead = True

#Generators CREATE bullets in various patters with the class bullet information
#Puts created information into bulletlist

#Original Generator
class Generator():
    def __init__(self, xPos, yPos):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False

    def update(self):
        pass

    def spawnBullet(self, xSpeed, ySpeed, image):
        global bulletlist

        bulletlist.append(Bullet(self.xPos, self.yPos, xSpeed, ySpeed, image))

#Whip Generator

#VARIABLES:
#xPos
#yPos
#frames
class WhipGenerator(Generator):
    def __init__(self, xPos, yPos, frames):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False

        self.x = 1
        self.y = 0
        self.xSpeed = 10
        self.ySpeed = 10
        self.frames = frames

    def update(self):
        global frame, bullet

        if self.x == 1:
            if self.xSpeed <= 10:
                self.xSpeed = self.xSpeed + 1
            else:
                self.xSpeed = self.xSpeed - 1
                self.x = 0
        else:
            if self.xSpeed >= -10:
                self.xSpeed = self.xSpeed - 1
            else:
                self.xSpeed = self.xSpeed + 1
                self.x = 1

        if self.y == 1:
            if self.ySpeed <= 10:
                self.ySpeed = self.ySpeed + 1
            else:
                self.ySpeed = self.ySpeed - 1
                self.x = 0
        else:
            if self.ySpeed >= -10:
                self.ySpeed = self.ySpeed - 1
            else:
                self.ySpeed = self.ySpeed + 1
                self.y = 1

        self.spawnBullet(self.xSpeed, self.ySpeed, bullet)
        if frame == self.startFrame + self.frames:
            self.complete = True

#Wave Generator

#VARIABLES:
#xPos
#yPos
#directionY
#frames
class WaveGenerator(Generator):
    def __init__(self, xPos, yPos, directionY, frames):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False

        self.directionY = directionY

        self.xSpeed = -5
        self.x = 1
        self.y = 0
        self.frames = frames

    def update(self):
        global frame, bullet


        if self.directionY == 0: 
            ySpeed = 10
        else:
            ySpeed = -10

        if self.x == 1:
            if self.xSpeed <= 5:
                self.xSpeed = self.xSpeed + 1
            else:
                self.x = 0
        else:
            if self.xSpeed >= -5:
                self.xSpeed = self.xSpeed - 1
            else:
                self.x = 1

            
        self.spawnBullet(self.xSpeed, ySpeed, bullet)
        if frame == self.startFrame + self.frames:
            self.complete = True

#Random Generator

#VARIABLES:
#xPos
#yPos
#xMove (left->right)
#frequency
#frames
class RandomGenerator(Generator):
    def __init__(self, xPos, yPos, xMove, frequency, frames):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False

        self.xMove = xMove
        self.frequency = frequency
        self.frames = frames
        
    
    def update(self):
        global frame, bullet

        if (self.startFrame - frame) % self.frequency == 0:
            self.xPos = self.xPos + self.xMove
            if self.xPos >= 475:
                self.xPos = 20
            if self.xPos < 20:
                self.xPos = 470
                
            xSpeed = randint(-3, 3)
            ySpeed = randint(2,5)

            self.spawnBullet(xSpeed, ySpeed, bullet)
        if frame == self.startFrame + self.frames:
            self.complete = True

#Random Generator V2

#VARIABLES:
#xPos
#yPos
#frequency
#frames
class RandomGeneratorV2(Generator):
    def __init__(self, xPos, yPos, frequency, frames):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False

        self.frequency = frequency
        self.frames = frames

    def update(self):
        global frame, bullet


        if (self.startFrame-frame) % self.frequency == 0:
            self.xPos = randint(25, 475)
            ySpeed = randint(2,8)
            xSpeed = 0

            self.spawnBullet(xSpeed,ySpeed,bullet)
        if frame == self.startFrame + self.frames:
            self.complete = True

#Draws Spiral

#VARIABLES:
#xPos
#yPos
#Start Angle
#End Angle
#Frequency
class SpiralGenerator(Generator):
    def __init__(self, xPos, yPos, startAngle, endAngle, frequency):
        global frame

        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False

        self.speed = 5
        self.angle = radians(startAngle)
        self.endAngle = radians(endAngle)
        self.frequency = frequency
    
    def update(self):
        global frame, bullet

        if (self.startFrame - frame) % self.frequency == 0:
            xSpeed = cos(self.angle)*self.speed
            ySpeed = sin(self.angle)*self.speed
            self.angle = self.angle+pi/20

            self.spawnBullet(xSpeed, ySpeed, bullet)
        if self.angle > self.endAngle+0.01:
            self.complete = True

#Draws Circle

#VARIABLES:
#xPos
#yPos
#numBullets
#speed
#frequency
class CircleGenerator(Generator):
    def __init__(self, xPos, yPos, numBullets, speed, frequency):
        global frame

        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False

        self.speed = speed
        self.numBullets = numBullets
        self.frequency = frequency

    def update(self):
        global frame, bullet

        angle = 0
        
        while angle < pi*2:
            xSpeed = cos(angle)*self.speed
            ySpeed = sin(angle)*self.speed

            angle = angle+pi/self.numBullets
            self.spawnBullet(xSpeed, ySpeed, bullet)

        self.complete = True

#Draws Wavey Lines

#VARIABLES:
#xPos
#yPos
#startXPos
#endXPos
#jump
#frames
class WaveyLineGenerator(Generator):
    def __init__(self, xPos, yPos, startXPos, endXPos, jump, frequency, frames):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startXPos = startXPos
        self.endXPos = endXPos
        self.x = 1
        self.jump = jump
        self.frequency = frequency
        
        self.startFrame = frame
        self.complete = False
        self.frames = frames


    def update(self):
        global frame, bullet

        xSpeed  = 0
        ySpeed = 8

        if (self.startFrame-frame) % self.frequency == 0:
            if self.x == 1:
                if self.xPos <= self.endXPos :
                    self.xPos = self.xPos + self.jump
                else:
                    self.x = 0
            else:
                if self.xPos >= self.startXPos:
                    self.xPos = self.xPos - self.jump
                else:
                    self.x = 1

            self.spawnBullet(xSpeed, ySpeed, bullet)

        if frame == self.startFrame + self.frames:
            self.complete = True

#Creates straight-line bullet

#VARIABLES:
#xPos
#yPos
#speed
#Frequency
#Frames
class HomingBulletGenerator(Generator):
    def __init__(self, xPos, yPos, speed, frequency, frames):
        global frame, xMouse, yMouse

        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed

        self.startFrame = frame
        self.complete = False
        self.frames = frames
        self.frequency = frequency

    def update(self):
        global frame, bullet, xMouse, yMouse

        if (self.startFrame-frame) % self.frequency == 0:
            xMissleDirection = xMouse - self.xPos
            yMissleDirection = yMouse - self.yPos

            x = checkDist(xMouse,yMouse,self.xPos,self.yPos)
            
            xMissleSpeed = self.speed * xMissleDirection / x
            yMissleSpeed = self.speed * yMissleDirection / x

            self.spawnBullet(xMissleSpeed,yMissleSpeed, bullet)

        if frame == self.startFrame + self.frames:
            self.complete = True
#Line Generator:

#VARIABLES:
#xPos
#yPos
#End
#direction
#moveSpeed
#frames
class LineGenerator(Generator):
    def __init__(self, xPos, yPos, End, direction, moveSpeed,  frames):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.complete = False
        self.frames = frames
        self.End = End
        self.moveSpeed = moveSpeed

        self.direction = direction

    def update(self):
        global frame, bulletInsta

        if self.direction == 1:
            ySpeed = 15
            xSpeed = 0
            if self.End != self.xPos:
                if self.End > self.xPos:
                    self.xPos = self.xPos + self.moveSpeed
                elif self.End < self.xPos:
                    self.xPos = self.xPos - self.moveSpeed
        else:

            ySpeed = 0
            xSpeed = 15

            if self.End != self.yPos:
                if self.End > self.yPos:
                    self.yPos = self.yPos + self.moveSpeed
                elif self.End < self.yPos:
                    self.yPos = self.yPos - self.moveSpeed
    
        self.spawnBullet(xSpeed, ySpeed, bulletInsta)

        if frame == self.startFrame + self.frames:
            self.complete = True

#Creates Wall Of Bullets To Dodge

#VARIABLES:
#xPos
#yPos
#Number of Bullets
#Frequency
#Frames
class WallGenerator(Generator):
    def __init__(self, xPos, yPos, numBullets, frequency, frames):
        global frame
        self.xPos = xPos
        self.yPos = yPos
        self.startFrame = frame
        self.frames = frames
        self.complete = False

        self.numBullets = numBullets
        self.frequency = frequency

    def update(self):
        global frame, bullet

        original = self.xPos

        ySpeed = 5
        xSpeed = 0

        placement = 500/self.numBullets
        ballNum = placement
        arrayP = placement

        placementA = []

        while arrayP <= 500:
            placementA.append(arrayP)
            arrayP = arrayP + placement

        if (self.startFrame-frame) % self.frequency == 0:

            random = choice(placementA)
            
            while ballNum <= 500:
                self.xPos = self.xPos + placement
                ballNum += placement

                if random == self.xPos or random + placement == self.xPos or random - placement == self.xPos:
                    pass
                else:
                    self.spawnBullet(xSpeed, ySpeed, bullet)

            self.xPos = original
                
        if frame == self.startFrame + self.frames:
            self.complete = True
        

######################
## PLAYER VARIABLES ##
######################

#Draws Player
#Uses "shipLag" to make the images of the ship appear to be leaning left and right
#Uses currentShip to tell which side (left/right) it should lag with
        
def drawPlayer():
    global player, xMouse, yMouse, ship, shipLeft, shipRight, prevXMouse, shipLag, currentShip
    
    screen.delete(player)    
    if xMouse  > prevXMouse + 1:
        player = screen.create_image(xMouse,yMouse, image = shipRight)
        shipLag = 0
        currentShip = shipRight

    elif xMouse  < prevXMouse - 1:
        player = screen.create_image(xMouse,yMouse, image = shipLeft)
        shipLag = 0
        currentShip = shipLeft

    else:
        if shipLag < 10:
            player = screen.create_image(xMouse,yMouse, image = currentShip)
            shipLag = shipLag + 1
        else:
            player = screen.create_image(xMouse,yMouse, image = ship)

#Updates player position
def updatePlayer():
    global xPlayer, yPlayer, xSpeed, ySpeed
    
    xPlayer = xPlayer + xSpeed
    yPlayer = yPlayer + ySpeed

############################
## MOUSE MOVEMENT HANDLER ##
############################

#Moves player around
def mouseMoveHandler(event):
    global xMouse, yMouse, prevXMouse

    prevXMouse = xMouse 

    xMouse = event.x
    yMouse = event.y
    drawPlayer() 

#################
## KEY HANDLER ##
#################    

#Quits Game
def keyPressHandler(event):
    global gameRunning, ship, paused, pause
    global xMouse, yMouse, checkXMouse, checkYMouse

    if event.keysym == "q" or event.keysym == "Q":
        gameRunning = False
        root.destroy()


    if event.keysym == "p" or event.keysym == "P":
       
        if paused == False:
            checkXMouse = xMouse
            checkYMouse = yMouse
            paused = True
            pause = screen.create_image(250,400, image = ship)
            screen.update()
        else:
            xMouse = checkXMouse
            yMouse = checkYMouse
            screen.delete(pause)
            screen.update()
            paused = False

################################        
## CHECK DISTANCE & CHECK HIT ##
################################

#Distance between two points
def checkDist(x1,y1,x2,y2):
    return sqrt((x2 - x1)**2+(y2 - y1)**2)

#Checks if player has been hit
def checkHit():
    global bulletlist, eBullety, xMouse, yMouse, gameRunning, currentLives, x

    hitCount = 0
    
    for i in bulletlist:

        x = checkDist(xMouse,yMouse,i.xPos,i.yPos)

        if x <= 15:
            currentLives = currentLives - 1
            i.dead = True
            hitCount = hitCount + 1
            if currentLives == 0:
                gameRunning = False

    
    if hitCount > 0:
        deleteLives()
        drawLives()
                

######################################
## GENERATOR & BULLET LIST UPDATERS ##
######################################

#Updates/Deletes Bullets which are out of bounds

#Example on how these work:
#Array                [Cat, Dog, Snake]
#Index                [0     1     2]
#Animals I dont like  [Dog]
#IndexofAnimal        [ 1 ]
#newArray             [Cat, Snake]
#newIndex             [ 0    1 ]

#In this senario, "Animals I dont like" are bullets that have left the screen which have been removed existance
#"gen" and "bull" = variables that are staying in next array
#Deleting GeneratorList: 
#"dels" = deselect

#Updates GeneratorList
def updateGeneratorList():
    global generatorlist
    generatorDels = []

    for index, i in enumerate(generatorlist):
        i.update()
        if i.complete:
            generatorDels.append(index)

    generatorlist = [gen for index, gen in enumerate(generatorlist) if index not in generatorDels]

#Updates Bulletlist
def updateBulletList():
    global bulletlist, currentLives

    for index, i in enumerate(bulletlist):
        i.update()
        if i.checkOOB():
            i.dead = True

def deleteBullets():
    global bulletlist, currentLives
    bulletDels = []

    for index, i in enumerate(bulletlist):
        if i.dead == True:
            bulletDels.append(index)

    bulletlist = [bull for index, bull in enumerate(bulletlist) if index not in bulletDels]

##def deleteAllBullets():
##    global bulletlist
##    bulletDels = []
##
##    for index, i in enumerate(bulletlist):
##        bulletDels.append(index)
##
##    bulletlist = [bull for index, bull in enumerate(bulletlist) if index not in bulletDels]
##
##    screen.update()


#Draws bullets based on their speed and position in class "Bullets"
def drawBullets():
    global bulletlist, generatorlist

    for i in bulletlist:
        i.draw()
   
#Plays Levels
def playLevels():
    global levels, currentLevel, previousLevel, frame, currentLives, maxLives, levelSelectCheck, gameRunning
    
    if levels[currentLevel].get(frame, False):
        for action in levels[currentLevel].get(frame):
            if action[0] == "Circle":
                generatorlist.append(CircleGenerator(*action[1]))
            elif action[0] == "Whip":
                generatorlist.append(WhipGenerator(*action[1]))
            elif action[0] == "Wave":
                generatorlist.append(WaveGenerator(*action[1]))
            elif action[0] == "Random":
                generatorlist.append(RandomGenerator(*action[1]))
            elif action[0] == "RandomV2":
                generatorlist.append(RandomGeneratorV2(*action[1]))
            elif action[0] == "Spiral":
                generatorlist.append(SpiralGenerator(*action[1]))
            elif action[0] == "WaveLine":
                generatorlist.append(WaveyLineGenerator(*action[1]))
            elif action[0] == "Homing":
                generatorlist.append(HomingBulletGenerator(*action[1]))
            elif action[0] == "Line":
                generatorlist.append(LineGenerator(*action[1]))
            elif action[0] == "Wall":
                generatorlist.append(WallGenerator(*action[1]))

    if frame > 2000:
        frame = 0
        if levelSelectCheck != True:
            previousLevel = currentLevel
            currentLevel = currentLevel + 1
            if currentLives < maxLives:
                currentLives = 3
            elif currentLives >= 3:
                currentLives = currentLives  + 1
        else:
            drawBeatLevel()
            gameRunning = False
    if currentLevel  >= 10:
        ending()

################
## BACKGROUND ##
################

#Draws background image
def drawBackground():
    global background, helpMenuCheck

    screen.create_image(250,400,image = background)

    screen.update()

#Draws lives image
def drawLivesImage():
    global shipLives, timesSymbol, ship, times
    
    shipLives = screen.create_image(40,755, image = ship)
    timesSymbol = screen.create_image( 100, 735, image = times)

    screen.update()

################################
## DIFFERENT BUTTONS / IMAGES ##
################################

#Draws beating level for level select
def drawBeatLevel():
    global menu2, menu1, beatLevelCheck, currentPic

    screen.delete(currentPic)

    beatLevelCheck = True
    
    menu1 = Button(screen, text = "Back To Main Menu?",font = ("Lucida Console", 20), command = startMenu)
    menu2 = Button(screen, text = "Back To Level Select?",font = ("Lucida Console", 20), command = startLevelSelect)

    menu1.place(x = 97, y = 600)
    menu2.place(x = 75, y = 700)
    

#Draws game over screen
def drawGameOver():
    global gameOver, currentPic, wordLevel, replay, menu, gameOverCheck

    gameOverCheck = True

    winsound.PlaySound('test4.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    
    screen.delete(currentPic)

    screen.create_image(275, 300, image = gameOver)

    screen.update()

    replay = Button(screen, text = "Retry?", font = ("Lucida Console", 20), command = startProgram)
    menu = Button(screen, text = "Back To Main Menu?",font = ("Lucida Console", 20), command = startMenu)

    replay.place(x = 185, y = 600)
    menu.place(x = 90, y = 700)

#Draws images for different levels
def drawLevelCounter():
    global currentLevel, previousLevel, level
    global zero, one, two, three, four, five, six, seven, eight, nine, ten
    global currentPic, lives

    x = 200
    xNum = 150
    y = 350
 
    screen.delete(currentPic)

    currentPic = screen.create_image(x + xNum, y, image = lives[currentLevel+1])

    screen.update()    

#Draws the word level
def drawWordLevel():
    global wordLevel
    wordLevel = screen.create_image(200,350,image = level)

#Draws lives    
def drawLives():
    global currentLives, lives, times, timesSymbol, ship
    global shipLives, timesSymbol, l1

    l1 = screen.create_image( 150, 750, image = lives[currentLives])


#Current lives updater
def deleteLives():
    global l1
    
    screen.delete(l1)
    
############################
## PROGRAM START FUNCTION ##
############################

#Start function
#Did this so that setInitialValues was not constantly reset in startMenu()
def start():
    setInitialValues()
    startMenu()

#Menu Screen
def startMenu():
    global play, info, select, title, titlePic, currentLevel, levelSelectCheck 

    currentLevel = 0

    deleteButtons1()

    drawBackground()

    levelSelectCheck = False

    winsound.PlaySound('test3.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    
    play = Button(screen, text = "Story mode", font = ("Lucida Console", 20), command = startProgram)
    info = Button(screen, text = "Help", font = ("Lucida Console", 20), command = startHelpMain)
    select = Button(screen, text = "Level Select", font = ("Lucida Console", 20), command = startLevelSelect)

    titlePic = screen.create_image(250,400,image = title)
    
    play.place(x = 170, y = 400)
    info.place(x = 215, y = 500)
    select.place(x = 146, y = 600)


#Info Screen
def startHelpMain():
    global nextPage, play2, help1, help2, bullet, bulletInsta, quitGame, pauseGame, backCheck
    global titlePic, helpMenuCheck
    global help1Pic, help2Pic, help3Pic, help4Pic, help5Pic, help6Pic, help9Pic
    global levelSelectCheck

    screen.delete(titlePic)

    helpMenuCheck = True

    if backCheck == True:
        global back,help7Pic, help8Pic
        back.destroy()
        screen.delete(help7Pic, help8Pic)
    
    deleteButtons2()

    play2 = Button(screen, text = "Menu", font = ("Lucida Console", 20), command = startMenu)
    nextPage = Button(screen, text = "--->", font = ("Lucida Console", 20), command = startHelpSecond)

    play2.place(x = 215, y = 700)
    nextPage.place(x = 400, y = 700)

    help1Pic = screen.create_image(275,75,image = help1)
    help2Pic = screen.create_image(275,215,image = help2)
    help3Pic = screen.create_image(50,30, image = bullet)
    help4Pic = screen.create_image(50,160, image = bulletInsta)
    help5Pic = screen.create_image(275, 625, image = quitGame)
    help6Pic = screen.create_image(275, 700, image = pauseGame)
    help9Pic = screen.create_image(250,400,image = help3)

#Second Info Screen
def startHelpSecond():
    global play, nextPage, back, mouse
    global help1Pic, help2Pic, help3Pic, help4Pic, help5Pic, help6Pic, help7Pic, help8Pic, help9Pic, backCheck, mouseDirections

    deleteButtons1()
    
    backCheck = True
    screen.delete(help1Pic, help2Pic, help3Pic, help4Pic, help5Pic, help6Pic, help9Pic)

    help7Pic = screen.create_image(250,400,image = mouse)
    help8Pic = screen.create_image(250,450,image = mouseDirections)

    back = Button(screen, text = "<---", font = ("Lucida Console", 20), command = startHelpMain)
    back.place(x = 10, y = 700)

#Level Selecter
def currentLevelSelector(l):
    global currentLevel
    currentLevel = l

#Level Select
def startLevelSelect():
    global currentLevel, levelSelectCheck
    global Level1, Level2, Level3, Level4, Level5, Level6, Level7, Level8, Level9, Level10 , playLevel, menu3
    global titlePic, levelSelect, selectLevel

    screen.delete(titlePic)

    levelSelect = screen.create_image(250,100,image = selectLevel)

    deleteButtons1()

    deleteButtons2()

    Level1 = Button(screen, text = "Level 1",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(0))
    Level2 = Button(screen, text = "Level 2",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(1))
    Level3 = Button(screen, text = "Level 3",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(2))
    Level4 = Button(screen, text = "Level 4",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(3))
    Level5 = Button(screen, text = "Level 5",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(4))
    Level6 = Button(screen, text = "Level 6",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(5))
    Level7 = Button(screen, text = "Level 7",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(6))
    Level8 = Button(screen, text = "Level 8",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(7))
    Level9 = Button(screen, text = "Level 9",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(8))
    Level10 = Button(screen, text = "Level 10",font = ("Lucida Console", 20), command=lambda *args: currentLevelSelector(9))

    playLevel = Button(screen, text = "Play Selected Level",font = ("Lucida Console", 20),command = startProgram)
    menu3 = Button(screen, text = "Menu",font = ("Lucida Console", 20),command = startMenu)
    
    Level1.place(x = 20, y = 250)
    Level2.place(x = 180, y = 250)
    Level3.place(x = 340, y = 250)

    Level4.place(x = 20, y = 375)
    Level5.place(x = 180, y = 375)
    Level6.place(x = 340, y = 375)

    Level7.place(x = 20, y = 500)
    Level8.place(x = 180, y = 500)
    Level9.place(x = 340, y = 500)

    Level10.place(x = 180, y = 625)

    playLevel.place(x = 25, y = 725)
    menu3.place(x = 400, y = 725)

    levelSelectCheck = True

#Delete Check Buttons
def deleteButtons1():
    global levelSelectCheck, gameOverCheck, beatLevelCheck, helpMenuCheck, backCheck
    
    if levelSelectCheck == True:
        Level1.destroy()
        Level2.destroy()
        Level3.destroy()
        Level4.destroy()
        Level5.destroy()
        Level6.destroy()
        Level7.destroy()
        Level8.destroy()
        Level9.destroy()
        Level10.destroy()
        playLevel.destroy()
        menu3.destroy()

    if helpMenuCheck == True:

        play2.destroy()

        if backCheck == True:
            back.destroy()
            nextPage.destroy()
        else:
            nextPage.destroy()

    if gameOverCheck == True:
        replay.destroy()
        menu.destroy()

    if beatLevelCheck == True:
        menu1.destroy()
        menu2.destroy()

#Delete Basic Buttons
def deleteButtons2():
    play.destroy()
    info.destroy()
    select.destroy()

#Small Ending Animation
#Beating Story Mode
def ending():
    global earth, thanks1, thanks2, thanks3

    drawBackground()

    winsound.PlaySound('test3.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

    xEarth = 250
    yEarth = -100

    for i in range(0,300):
        Earth = screen.create_image(xEarth,yEarth, image = earth) 

        yEarth = yEarth + 3

        screen.update()
        sleep(0.04)

        if i != 299:
            screen.delete(Earth)

    for i in range(0,50):
        x = randint(1,3)
        if x == 1:
            Thanks = screen.create_image(250,100,image = thanks1)
        elif x == 2:
            Thanks = screen.create_image(250,100,image = thanks2)
        elif x == 3:
            Thanks = screen.create_image(250,100,image = thanks3)

        screen.update()
        sleep(0.1)
        screen.delete(Thanks)

    root.destroy()
        
#Run Program
def startProgram():
    global xPlayer, yPlayer, xSpeed, ySpeed
    global score, frame, gameRunning, bulletlist, generatorlist
    global currentLevel, previousLevel
    global titlePic, wordLevel
    global shipLives, timesSymbol, l1, paused
    global helpMenuCheck, currentLives, levelSelectCheck, levelSelect

    if levelSelectCheck == True:
        x = 1
        screen.delete(levelSelect)
    else:
        x = 0
    
    deleteButtons1()

    deleteButtons2()

    setInitialValues()

    screen.delete(titlePic)

    drawBackground()

    drawLevelCounter()

    drawLives()

    drawWordLevel()

    drawLivesImage()

    if x == 1:
        levelSelectCheck = True

    if levelSelectCheck == True:
        winsound.PlaySound('test.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    else:
        winsound.PlaySound('test2.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

        currentLevel = 0

    while gameRunning == True:
        if paused == False:
            frame = frame + 1

            if previousLevel != currentLevel:
                previousLevel = currentLevel
                deleteLives()
                drawLevelCounter()
                drawLives()

            updatePlayer()

            drawPlayer()

            playLevels()       

            screen.update()

            checkHit()

            updateGeneratorList()
            
            updateBulletList()

            deleteBullets()

            drawBullets()
                   
            sleep(0.005)
        else:
            screen.update()
            sleep(0.005)
        
    screen.delete(wordLevel, shipLives, timesSymbol, l1)

    if levelSelectCheck != True or levelSelectCheck == True and currentLives == 0:
        drawGameOver()
        

root.after(0, start)

screen.bind("<Key>", keyPressHandler)
screen.bind("<Motion>", mouseMoveHandler)
screen.pack()
screen.focus_set()
root.mainloop()
#1246
