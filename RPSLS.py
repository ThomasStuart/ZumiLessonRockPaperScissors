# generate random integer values
from random import seed
from random import randint
from zumi.util.screen import Screen
screen = Screen()

MyHand   = ""
ZumiHand = ""
# seed random number generator
seed(1)

# Map: 
R  = 'rock'
P  = 'paper'
SC = 'scissors'
L  = 'lizard'
SP = 'spock'
menuString = "Enter a hand [1-rock, 2-paper, 3-scissors, 4-lizard, 5-spock]"
I = "I Won"
Z = "Zumi Won"

# returns a string based on numberic value generated.
def generateRandomHand():
    randomNum = randint(1,5)
    
    if   randomNum == 1:
        return R
    elif randomNum == 2:
        return P
    elif randomNum == 3:
        return SC
    elif randomNum == 4:
        return L 
    else:
        return SP
    
def getUserChoice():
    userString = input(menuString)
    userNum    = int(userString)

    if   userNum == 1:
        return R
    elif userNum == 2:
        return P
    elif userNum == 3:
        return SC
    elif userNum == 4:
        return L 
    else:
        return SP
    
# TODO: break ties correctly (redo or just say tie).  
# right now we just say that Zumi won
def determineWinner(MyHand, ZumiHand):
    if   MyHand == R  and (ZumiHand == L or ZumiHand == SC):
        return I
    elif MyHand == P  and (ZumiHand == R or ZumiHand == SP):
        return I
    elif MyHand == SC and (ZumiHand == P or ZumiHand == L):
        return I
    elif MyHand == SP and (ZumiHand == R or ZumiHand == SC):
        return I
    elif MyHand == L  and (ZumiHand == P or ZumiHand == SP):
        return I
    else:
        return Z  
    
# [X] ask for our choice via keyboard input [ rock, paper...]
MyHand   = getUserChoice()
# [X] generate a random choice for zumi 
ZumiHand = generateRandomHand()
# Print to console for debugging purposes
print("My   Hand: ", MyHand)
print("Zumi Hand: ", ZumiHand)

# [X] display the results on zumi's LCD screen
displayChoicesString = "M: " + MyHand + " vs. Z:" + ZumiHand
screen.print(displayChoicesString) # screen.draw_text(..)

# [X] determine the winner via a function 
print("Winner:", determineWinner(MyHand, ZumiHand))

# [] display Winner on zumi's LCD screen

# [ ] make zumi cry if we win else zumi is gonna showboat    
