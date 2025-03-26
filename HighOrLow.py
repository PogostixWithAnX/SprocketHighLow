import thumby
import time
import math
import random
thumby.display.fill(0)
thumby.display.setFPS(5)

#Pogostix_With_An_X 2025
#My second ever project. Looking to play more with sprites. This was not meant to be more ambitious than Rock Paper Scissors, but it wound up that way anyway lol.
#Maybe next time I'll do something that isn't a stupid math game.

#Title Sprite
# BITMAP: width: 69, height: 28
titleMap = bytearray([255,1,1,239,238,239,1,1,255,254,0,255,1,1,255,254,0,254,131,1,125,125,109,137,11,254,252,0,255,1,1,239,238,239,1,1,255,254,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           1,3,3,3,3,1,3,3,3,3,0,1,3,3,3,3,0,0,1,3,3,3,243,11,11,11,241,0,249,75,75,75,179,1,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,253,4,4,252,249,0,0,0,0,248,12,4,244,244,244,4,12,248,240,0,252,4,4,124,56,124,4,4,252,248,0,56,108,228,116,52,180,132,204,248,112,
           0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,12,12,13,13,13,15,14,0,3,6,12,13,13,13,12,14,15,7,0,7,12,12,14,7,6,4,12,15,15,0,0,0,7,13,13,15,15,1,0,0])

#Sprocket sprites
#Facing Left
# BITMAP: width: 22, height: 16
sprocketMap1 = bytearray([224,16,28,26,245,255,199,139,131,199,255,242,2,4,248,128,128,76,50,130,68,56,
           1,3,231,7,127,215,247,59,219,235,179,252,104,60,195,255,249,217,127,0,0,0])

#Facing Right (His spots are assymetrical so really he shouldn't be mirrored but WHATEVER)
# BITMAP: width: 22, height: 16
sprocketMap2 = bytearray([56,68,130,50,76,128,128,248,4,2,242,255,199,131,139,199,255,245,26,28,16,224,
           0,0,0,127,217,249,255,195,60,104,252,179,235,219,59,247,215,127,7,231,3,1])

#Happy
# BITMAP: width: 22, height: 16
sprocketHappyMap = bytearray([224,16,22,25,245,255,215,139,147,199,255,250,1,1,2,252,128,70,57,129,66,60,
           1,3,229,5,125,214,247,59,219,235,179,252,104,56,196,255,249,217,127,0,0,0])
#Sad
# BITMAP: width: 22, height: 16
sprocketSadMap = bytearray([128,64,112,40,212,252,28,76,140,28,252,200,8,16,224,128,128,64,56,132,68,56,
           7,12,212,20,79,223,223,46,206,239,175,243,96,48,207,255,249,217,127,0,0,0])

#Luna Sprites (yes she's in here too)
# BITMAP: width: 25, height: 18
lunaMap1 = bytearray([14,81,169,5,2,26,66,66,26,2,5,169,81,14,0,0,64,160,160,16,32,16,32,64,128,
           0,0,0,1,250,134,6,14,254,142,7,0,241,1,2,4,8,240,80,145,78,128,64,41,22,
           0,0,0,0,1,3,3,3,1,3,3,3,1,2,2,2,2,1,0,0,0,0,0,0,0])

# BITMAP: width: 25, height: 18
lunaMap2 = bytearray([14,81,169,5,2,26,66,66,26,2,5,169,81,14,20,20,34,196,2,4,40,208,0,0,0,
           0,0,0,1,250,134,6,14,254,142,7,0,241,1,2,6,10,241,16,8,5,2,0,0,0,
           0,0,0,0,1,3,3,3,1,3,3,3,1,2,2,2,2,1,0,0,0,0,0,0,0])
#YOU sprite
# BITMAP: width: 31, height: 10
youMap = bytearray([31,49,225,15,15,225,241,63,62,0,254,131,1,125,125,125,1,131,254,252,0,255,129,1,127,126,127,1,129,255,254,
           0,0,1,3,3,3,1,0,0,0,0,1,3,3,3,3,3,3,3,1,0,0,1,3,3,3,3,3,3,3,1])

#WIN sprite
# BITMAP: width: 33, height: 10
winMap = bytearray([255,1,1,159,206,159,1,1,255,254,0,255,1,1,255,254,0,255,1,1,243,230,207,1,1,255,254,0,255,65,241,255,30,
           1,3,3,3,1,1,1,3,3,3,0,1,3,3,3,3,0,1,3,3,3,1,1,3,3,3,3,0,1,3,3,3,0])

#LOSE sprite
# BITMAP: width: 41, height: 10
loseMap = bytearray([255,1,1,127,126,64,64,192,128,0,254,131,1,125,125,125,1,131,254,252,0,238,179,33,109,109,109,9,155,254,252,0,255,1,1,109,109,109,125,255,142,
           1,3,3,3,3,3,3,3,3,0,0,1,3,3,3,3,3,3,3,1,0,0,1,3,3,3,3,3,3,3,1,0,1,3,3,3,3,3,3,3,3])

#Intro Screen
introScreen = True
while(introScreen):
    thumby.display.fill(0)
    print("HIGH or LOW?")
    print("A: Start")
    print("B: How to Play")
    titleSpr = thumby.Sprite(69, 28, titleMap, 1, 1)
    thumby.display.drawSprite(titleSpr)
    thumby.display.update()
    time.sleep(0.25)
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    thumby.display.drawText("A: Start", 0, 29, 1)
    thumby.display.drawText("B: How to Play", 0, 35, 1)
    thumby.display.update()
    waiting = True
    while(waiting):
        if thumby.buttonA.justPressed():
            waiting = False
            introScreen = False
            gameLoop = True
        elif thumby.buttonB.justPressed(): #How to Play (aka the dreadful IF layer cake)
            waiting = False
            howToPlay = True
            print("Sprocket will pick a number between 1 and 9.")
            print("You guess if the next number he picks will be HIGHER or LOWER.")
            print("Press A if you think it will be higher.")
            print("Press B if you think it will be lower.")
            print("There are 5 rounds. If you guess 3 or more right, you win! :)")
            print("Press B to go back.")
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("How to Play:", 0, 0, 1)
            thumby.display.update()
            time.sleep(0.25)
            sprocketSpr1 = thumby.Sprite(22, 16, sprocketMap1, 50, 24)
            thumby.display.drawSprite(sprocketSpr1)
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("Sprocket will pick", 0, 8, 1)
            thumby.display.drawText("a number between", 0, 14, 1)
            thumby.display.drawText("1 and 9.", 0, 20, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.drawText("A: Next", 0, 35, 1)
            thumby.display.update()
            while(howToPlay):
                if thumby.buttonA.justPressed():
                    thumby.display.fill(0)
                    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                    thumby.display.drawSprite(sprocketSpr1)
                    thumby.display.drawText("You have to guess", 0, 0, 1)
                    thumby.display.drawText("if the next number", 0, 6, 1)
                    thumby.display.drawText("will be HIGHER", 0, 12, 1)
                    thumby.display.drawText("or LOWER.", 0, 18, 1)
                    thumby.display.update()
                    time.sleep(0.25)
                    thumby.display.drawText("A: Next", 0, 35, 1)
                    thumby.display.update()
                    waiting2 = True
                    while(waiting2):
                        if thumby.buttonA.justPressed():
                            thumby.display.fill(0)
                            thumby.display.drawSprite(sprocketSpr1)
                            thumby.display.drawText("If you guess it's", 0, 0, 1)
                            thumby.display.drawText("HIGHER, press A.", 0, 6, 1)
                            thumby.display.drawText("If you guess it's", 0, 12, 1)
                            thumby.display.drawText("LOWER, press B.", 0, 18, 1)
                            thumby.display.update()
                            time.sleep(0.25)
                            thumby.display.drawText("A: Next", 0, 35, 1)
                            thumby.display.update()
                            waiting3 = True
                            while(waiting3):
                                if thumby.buttonA.justPressed():
                                    thumby.display.fill(0)
                                    sprocketSprHappyStill = thumby.Sprite(22, 16, sprocketHappyMap, 50, 24)
                                    thumby.display.drawSprite(sprocketSprHappyStill)
                                    thumby.display.drawText("There are 5 rounds.", 0, 0, 1)
                                    thumby.display.drawText("If you guess 3 or", 0, 6, 1)
                                    thumby.display.drawText("more correctly,", 0, 12, 1)
                                    thumby.display.drawText("You win the game!", 0, 18, 1)
                                    thumby.display.update()
                                    time.sleep(0.24)
                                    thumby.display.drawText("B: Back", 0, 35, 1)
                                    thumby.display.update()
                                    waiting4 = True
                                    while(waiting4):
                                        if thumby.buttonB.justPressed():
                                            howToPlay = False
                                            waiting2 = False
                                            waiting3 = False
                                            waiting4 = False
                                            introScreen = True
                                            break

#Game Loop
gameRound = 1
playerScore = 0
while(gameLoop):
    time.sleep(0.25)
    thumby.display.fill(0)
    print("Round ", gameRound)
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
    thumby.display.drawText("Round " +str(gameRound), 18, 1, 1) #print round number to screen
    thumby.display.update()
    time.sleep(0.25)
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Sprocket picks some numbers
    #print(list1) #debug option, uncomment to allow
    sprocketChoice1 = random.choice(list1)
    #print("The first number is ", sprocketChoice1) #debug
    thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
    thumby.display.drawText(str(sprocketChoice1), 10, 16, 1)
    thumby.display.drawText("?", 54, 16, 1) #draw question mark
    list1.remove(sprocketChoice1)
    #print(list1) #debug
    sprocketChoice2 = random.choice(list1)
    print("The second number is ", sprocketChoice2) #debug
    waiting = True
    frameCount = 0
    thumby.display.setFPS(2)
    while(waiting): #Waiting for player to guess
        sprocketSprTurn = thumby.Sprite(22, 16, sprocketMap1+sprocketMap2, 25, 16)
        sprocketSprTurn.setFrame(frameCount)
        thumby.display.drawSprite(sprocketSprTurn) #Draw Sproket to the screen
        frameCount += 1
        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
        thumby.display.drawText("A: Higher B: Lower", 0, 34, 1)
        thumby.display.update()
        if thumby.buttonA.justPressed():#Player thinks it's higher...
            if int(sprocketChoice1) < int(sprocketChoice2):#.. And it is!
                print("correct!")
                thumby.display.fill(0)
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("Round " +str(gameRound), 18, 1, 1)
                thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
                thumby.display.drawText(str(sprocketChoice1), 10, 16, 1)
                thumby.display.drawText(str(sprocketChoice2), 54, 16, 1)#Reveal the second number
                sprocketSpr2 = thumby.Sprite(22, 16, sprocketMap2, 25, 16)
                thumby.display.drawSprite(sprocketSpr2)
                thumby.display.update()
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Continue", 15, 34, 1)
                thumby.display.update()
                gameRound = int(gameRound) + 1
                playerScore = int(playerScore) + 1
                waiting2 = True
                while(waiting2):
                    if thumby.buttonA.justPressed():
                        waiting3 = True
                        frameCount = 0
                        thumby.display.fill(0)
                        while(waiting3):
                            thumby.display.setFPS(2)
                            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                            thumby.display.drawText("Correct! :)", 5, 1, 1) #Hooray!
                            #Placeholder for a happy noise to play
                            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                            thumby.display.drawText("A: Continue", 15, 34, 1)
                            sprocketHappySpr = thumby.Sprite(22, 16, sprocketMap1+sprocketHappyMap, 25, 16)
                            sprocketHappySpr.setFrame(frameCount)
                            thumby.display.drawSprite(sprocketHappySpr) #Draw Sprocket to the screen
                            frameCount += 1
                            thumby.display.update()
                            if thumby.buttonA.justPressed():
                                waiting2 = False
                                waiting3 = False
                if int(gameRound) <= 5:
                    gameLoop = True
                    waiting = False
                elif int(gameRound) > 5:
                    gameLoop = False
                    waiting = False
                    
            elif int(sprocketChoice1) > int(sprocketChoice2):#.. but it isn't
                thumby.display.fill(0)
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("Round " +str(gameRound), 18, 1, 1)
                thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
                thumby.display.drawText(str(sprocketChoice1), 10, 16, 1)
                thumby.display.drawText(str(sprocketChoice2), 54, 16, 1)#Reveal the second number
                sprocketSpr2 = thumby.Sprite(22, 16, sprocketMap2, 25, 16)
                thumby.display.drawSprite(sprocketSpr2)
                thumby.display.update()
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Continue", 15, 34, 1)
                thumby.display.update()
                gameRound = int(gameRound) + 1
                waiting2 = True
                while(waiting2):
                    if thumby.buttonA.justPressed():
                        waiting3 = True
                        frameCount = 0
                        thumby.display.fill(0)
                        while(waiting3):
                            thumby.display.setFPS(2)
                            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                            thumby.display.drawText("Incorrect :(", 0, 1, 1) #Awwww...
                            #Placeholder for a sad noise to play
                            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                            thumby.display.drawText("A: Continue", 15, 34, 1)
                            sprocketSadSpr = thumby.Sprite(22, 16, sprocketMap1+sprocketSadMap, 25, 16)
                            sprocketSadSpr.setFrame(frameCount)
                            thumby.display.drawSprite(sprocketSadSpr) #Draw Sprocket to the screen
                            frameCount += 1
                            thumby.display.update()
                            if thumby.buttonA.justPressed():
                                waiting2 = False
                                waiting3 = False
                if int(gameRound) <= 5:
                    gameLoop = True
                    waiting = False
                elif int(gameRound) > 5:
                    gameLoop = False
                    waiting = False
                    
        if thumby.buttonB.justPressed():#Player thinks it's lower...
            if int(sprocketChoice1) > int(sprocketChoice2):#.. And it is!
                print("correct!")
                thumby.display.fill(0)
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("Round " +str(gameRound), 18, 1, 1)
                thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
                thumby.display.drawText(str(sprocketChoice1), 10, 16, 1)
                thumby.display.drawText(str(sprocketChoice2), 54, 16, 1)#Reveal the second number
                sprocketSpr2 = thumby.Sprite(22, 16, sprocketMap2, 25, 16)
                thumby.display.drawSprite(sprocketSpr2)
                thumby.display.update()
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Continue", 15, 34, 1)
                thumby.display.update()
                gameRound = int(gameRound) + 1
                playerScore = int(playerScore) + 1
                waiting2 = True
                while(waiting2):
                    if thumby.buttonA.justPressed():
                        waiting3 = True
                        frameCount = 0
                        thumby.display.fill(0)
                        while(waiting3):
                            thumby.display.setFPS(2)
                            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                            thumby.display.drawText("Correct! :)", 5, 1, 1) #Hooray!
                            #Placeholder for a happy noise to play
                            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                            thumby.display.drawText("A: Continue", 15, 34, 1)
                            sprocketHappySpr = thumby.Sprite(22, 16, sprocketMap1+sprocketHappyMap, 25, 16)
                            sprocketHappySpr.setFrame(frameCount)
                            thumby.display.drawSprite(sprocketHappySpr) #Draw Sprocket to the screen
                            frameCount += 1
                            thumby.display.update()
                            if thumby.buttonA.justPressed():
                                waiting2 = False
                                waiting3 = False
                if int(gameRound) <= 5:
                    gameLoop = True
                    waiting = False
                elif int(gameRound) > 5:
                    gameLoop = False
                    waiting = False
                    
            elif int(sprocketChoice1) < int(sprocketChoice2):#.. but it isn't
                thumby.display.fill(0)
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("Round " +str(gameRound), 18, 1, 1)
                thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
                thumby.display.drawText(str(sprocketChoice1), 10, 16, 1)
                thumby.display.drawText(str(sprocketChoice2), 54, 16, 1)#Reveal the second number
                sprocketSpr2 = thumby.Sprite(22, 16, sprocketMap2, 25, 16)
                thumby.display.drawSprite(sprocketSpr2)
                thumby.display.update()
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Continue", 15, 34, 1)
                thumby.display.update()
                gameRound = int(gameRound) + 1
                waiting2 = True
                while(waiting2):
                    if thumby.buttonA.justPressed():
                        waiting3 = True
                        frameCount = 0
                        thumby.display.fill(0)
                        while(waiting3):
                            thumby.display.setFPS(2)
                            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                            thumby.display.drawText("Incorrect :(", 0, 1, 1) #Awwww...
                            #Placeholder for a sad noise to play
                            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                            thumby.display.drawText("A: Continue", 15, 34, 1)
                            sprocketSadSpr = thumby.Sprite(22, 16, sprocketMap1+sprocketSadMap, 25, 16)
                            sprocketSadSpr.setFrame(frameCount)
                            thumby.display.drawSprite(sprocketSadSpr) #Draw Sprocket to the screen
                            frameCount += 1
                            thumby.display.update()
                            if thumby.buttonA.justPressed():
                                waiting2 = False
                                waiting3 = False
                if int(gameRound) <= 5:
                    gameLoop = True
                    waiting = False
                elif int(gameRound) > 5:
                    gameLoop = False
                    waiting = False
                
    if int(gameRound) > 5: #Game ends after 5 rounds
        print("You won ", int(playerScore), "out of 5 rounds.")
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("You got", 12, 0, 1)
        thumby.display.drawText(str(playerScore) + " out of 5", 5, 8, 1)
        thumby.display.drawText("correct.", 11, 16, 1)
        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
        thumby.display.drawText("A: Continue", 15, 34, 1)
        thumby.display.update()
        waiting2 = True
        while(waiting2):
            if thumby.buttonA.justPressed():
                if int(playerScore) >= 3: #WINNER WINNER CHICKEN DINNER
                    print("YOU WIN! :)")
                    thumby.display.fill(0)
                    youSpr = thumby.Sprite(31, 10, youMap, 21, 0)
                    thumby.display.drawSprite(youSpr)
                    winSpr = thumby.Sprite(33, 10, winMap, 20, 12)
                    thumby.display.drawSprite(winSpr)
                    #Win Tune goes here
                    thumby.display.update()
                    waiting3 = True
                    frameCount = 0
                    while(waiting3):
                        sprocketHappySpr2 = thumby.Sprite(22, 16, sprocketMap1+sprocketHappyMap, 50, 23)
                        sprocketHappySpr2.setFrame(frameCount)
                        thumby.display.drawSprite(sprocketHappySpr2) #Draw Sprocket to the screen
                        frameCount += 1
                        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                        thumby.display.drawText("A: Next", 0, 35, 1)
                        thumby.display.update()
                        if thumby.buttonA.justPressed():
                            waiting3 = False
                            waiting2 = False
                    
                elif int(playerScore) < 3: #Better luck next time.
                    print("You Lost :(")
                    thumby.display.fill(0)
                    youSpr = thumby.Sprite(31, 10, youMap, 21, 0)
                    thumby.display.drawSprite(youSpr)
                    loseSpr = thumby.Sprite(41, 10, loseMap, 16, 12)
                    thumby.display.drawSprite(loseSpr)
                    #Sad music goes here
                    thumby.display.update()
                    waiting3 = True
                    frameCount = 0
                    while(waiting3):
                        sprocketSadSpr2 = thumby.Sprite(22, 16, sprocketMap1+sprocketSadMap, 50, 23)
                        sprocketSadSpr2.setFrame(frameCount)
                        thumby.display.drawSprite(sprocketSadSpr2) #Draw Sprocket to the screen
                        frameCount += 1
                        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                        thumby.display.drawText("A: Next", 0, 35, 1)
                        thumby.display.update()
                        if thumby.buttonA.justPressed():
                            waiting3 = False
                            waiting2 = False
                playerScore = 0
                gameRound = 1
        print("Play Again? A:Y B:N")
        stillWaiting = True
        while(stillWaiting):
            thumby.display.fill(0)
            thumby.display.setFPS(15)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("Play Again?", 0, 1, 1)
            thumby.display.setFont("lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A:Yes! B:No thanks", 0, 9, 1)
            thumby.display.drawText("Down: Credits", 0, 16, 1)
            sprocketSpr1 = thumby.Sprite(22, 16, sprocketMap1, 50, 23)
            thumby.display.drawSprite(sprocketSpr1)
            thumby.display.update()
            time.sleep(0.5)
            if thumby.buttonA.justPressed():
                stillWaiting = False
                waiting = False
                gameLoop = True
            elif thumby.buttonB.justPressed():
                thumby.reset()
            elif thumby.buttonD.justPressed():
                stillWaiting = False
                credits = True
                frameCount = 1
                while(credits):
                    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                    thumby.display.fill(0)
                    thumby.display.drawText("CREDITS", 0, 0, 1)
                    thumby.display.drawText("Code and Sprites", 0, 6, 1)
                    thumby.display.drawText("by Pogostix", 0, 12, 1)
                    thumby.display.drawText("A: Next", 0, 35, 1)
                    thumby.display.update()
                    waiting2 = True
                    thumby.display.setFPS(5)
                    while(waiting2):
                        lunaSpr = thumby.Sprite(25, 18, lunaMap1+lunaMap2, 47,22)
                        lunaSpr.setFrame(frameCount)
                        thumby.display.drawSprite(lunaSpr)
                        frameCount += 1
                        thumby.display.update()
                        if thumby.buttonA.justPressed():
                            waiting3 = True
                            while(waiting3):
                                thumby.display.fill(0)
                                lunaSpr = thumby.Sprite(25, 18, lunaMap1+lunaMap2, 47,22)
                                lunaSpr.setFrame(frameCount)
                                thumby.display.drawSprite(lunaSpr)
                                frameCount += 1
                                thumby.display.drawText("SPECIAL THANKS", 0, 1, 1)
                                thumby.display.drawText("Sprocket,", 0, 12, 1)
                                thumby.display.drawText("Siren,", 0, 18, 1)
                                thumby.display.drawText("and Luna.", 0, 24, 1)
                                thumby.display.drawText("B: Go back", 0, 35, 1)
                                thumby.display.update()
                                waiting4 = True
                                while(waiting4):
                                    lunaSpr = thumby.Sprite(25, 18, lunaMap1+lunaMap2, 47,22)
                                    lunaSpr.setFrame(frameCount)
                                    thumby.display.drawSprite(lunaSpr)
                                    frameCount += 1
                                    thumby.display.update()
                                    if thumby.buttonB.justPressed():
                                        credits = False
                                        waiting2 = False
                                        waiting3 = False
                                        waiting4 = False
                                        stillWaiting = True
                    
