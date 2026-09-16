from random import randint, shuffle
from collections import Counter, deque
fq = Counter()
doubleStreak = 0
currSquare = 0
FACES = 4
NUMTILES = 40
JAILDOUBLES = 3
GOSQUARE = 0
JAILSQUARE = 10
GTJSQUARE = 30
commCards =   deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
chanceCards = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
shuffle(commCards)
shuffle(chanceCards)
def roll(faces):
    x, y = randint(1, faces), randint(1, faces)
    return (x+y,x==y)

def isChance():
    return currSquare in [7, 22, 36]

def isComm():
    return currSquare in [2,17,33]

def goToJail():
    global currSquare, doubleStreak
    fq[10] += 1
    currSquare = 10
    doubleStreak = 0

def newSquareComm():
    card = commCards[0]
    commCards.rotate(1)
    if card == 1: return GOSQUARE
    if card == 2: return JAILSQUARE
    return currSquare

def newSquareChance():
    card = chanceCards[0]
    chanceCards.rotate(1)
    if card == 1: return GOSQUARE
    if card == 2: return JAILSQUARE
    if card == 3: return 11
    if card == 4: return 24
    if card == 5: return 39
    if card == 6: return 5
    if card == 7: return nextRail()
    if card == 8: return nextRail()
    if card == 9: return nextUtil()
    if card == 10: return (currSquare - 3) % NUMTILES
    return currSquare

def nextRail():
    if currSquare == 36: return 5
    elif currSquare == 7: return 15
    elif currSquare == 22: return 25
    else:
        raise Exception(f"Sent to rail from non-chance square {currSquare}")

def nextUtil():
    if currSquare == 36: return 12
    elif currSquare == 7: return 12
    elif currSquare == 22: return 28
    else:
        raise Exception(f"Sent to utility from non-chance square {currSquare}")

def modal():
    return [x[0] for x in fq.most_common(3)]

numRolls = 0
while True:
    numRolls += 1
    if numRolls%1000000==0: print(modal())
    diceRoll, isDouble = roll(FACES)
    if isDouble: doubleStreak += 1
    else: doubleStreak = 0
    
    if doubleStreak == JAILDOUBLES:
        goToJail()
        continue
        
    
    currSquare = (currSquare + diceRoll) % NUMTILES
    if isChance(): currSquare = newSquareChance()
    if isComm(): currSquare = newSquareComm()
    if currSquare==GTJSQUARE or currSquare == JAILSQUARE:
        goToJail()
        continue
    else:
        fq[currSquare] += 1
