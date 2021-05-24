######################################################################
#
#                MIT OCW 6.S095
#          Programming for the Puzzled
# "Tact is after all a kind of mind reading. – Sarah Orne Jewett"
######################################################################
#          Assignment #3
#  https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/puzzle-3-you-can-read-minds/
######################################################################
#     Guess the hidden card 
######################################################################
# Programming constructs and algorithmic paradigms covered
# in this puzzle: reading input from a user, and control
# flow for case analysis.  Encoding and decoding 
# information.
######################################################################
# 5 cards, 4 are known, last one is not.  
# order the cards first
# 52 cards total, we show 4 - then what can the 5th one be? 
# The 5th card could be 1 of the 48 
# during the demonstration, Billy had to 
# 2 ^ 4 bits of information?  No, there are 4 types of cards (hearts, spades, diamonds, clubs)
######################################################################
# if you have 4 cards, how many possibilities are there with  cards? 
# 
# 4! => 24     
# Why 4 factorial?  
# because the first time you pick a card to complete 4, you have 4 choices.  
# the 2nd time, you have 3 choices
# the 3rd time, you have 2 choices
# and then one choice, so 4x3x2x1 => 24
#==========================================
# 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K, A Numbers 
# 1 2  3 4 types   
# 4 x 12 => 48 
##############################################
### Billy put up 4 cards;  how could he communicate to Professor something about the cards? 
# 1. Order the cards by lowest-to-highest ?
# 2. 

# first lets build the deck of cards programmatically.  The format is "card_suit".  For example
# A card with a king of spades, would be "K_S".  An Ace of hearts would be "A_H".
# Order of a 52-card deck from lowest to highest is: 
# A♣ A♦ A♥ A♠ 2♣ 2♦ 2♥ 2♠ . . . Q♣ Q♦ Q♥ Q♠ K♣ K♦ K♥ K♠

import random


def GetCardAbbr(argument):
    switcher = { 
        "hearts":"H",
        "clubs":"C",
        "diamonds":"D",
        "spades":"S", 
        1:"H",
        2:"C",
        3:"D",
        4:"S", 
        "H":"hearts",  # allows for reverse-lookup
        "C":"Clubs",
        "D":"Diamonds",
        "S":"Spades",
    }
    return (switcher.get(argument, "bad"))


def MapCards(argument):
    switcher = {
        0: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
        "A":0,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6, 
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "J":11, 
        "Q":12, 
        "K":13
    }

    return (switcher.get(argument, "bad"))

def MakeDeck():
   
    deckList = []
    
    cards = ['clubs', 'hearts', 'spades', 'diamonds']
    for types in cards:
        card = GetCardAbbr(types)
        #print(card)
        for i in [x for x in range( deckStart, deckEnd + 1 ) if x != 1]:
            #print (i)
            str_deck = MapCards(i) + "_" + card
            deckList.append(str_deck)
    return deckList
    

def PickCards(currentList): 
    theList = ''
    card = GetCardAbbr(random.randint(1, 3))
    type = MapCards(random.randint( deckStart, deckEnd + 1 ))
    tuple =  type + "_" + card
    if(tuple in [x for x in currentList if x != 1]) or 'bad' in tuple:
        while( tuple in [x for x in currentList if x != 1] or 'bad' in tuple ):
            card = GetCardAbbr(random.randint(1, 3))
            type = MapCards(random.randint(deckStart, deckEnd + 1))
            tuple =  type + "_" + card
    return tuple

# Now its time to do some arithmetic and determine the closest neighbor for this card game.  
# The algorithm is as follows: 
# Largest  |  Smaller   |   mod   | divisor   |  
# Number   |   Number   |         |   divisor | direction
#---------------------------------------------------------------
#  13           4           1          3         CW
#  13           6           1          2         CW
#  13           7           6          0         CCW
#  12           7           5          0         CCW                7-5 = 2, therefore CCW
#   7           6           1          1         CCW                7-6 = 1, therefore CCW
#  10           4           2          2         CCW               10-4=6, 13-10 = 3, 4-2+1, 3 ==>6 CW works or CCW would work
#  11           4           *3         *2         CW                 
#  10           3           *1         *3         CW   
#   8           3           *2         *2        CCW             
# 
###################################################################

def DoTheMathAndFindLeastDistance():
    #dosomething
    print ("doing something")
    
def DoCardsThingy(theSuit):
    index=0 
    for acard in theSuit: 
        (card, suit) = acard.split("_")
        print (card)
        mappedCard = MapCards(card)
        if(index>0):
            print ("stuff: ", card, suit)
            if(mappedCard==0 or mappedLastCard==0):
                print("Modulus of 0 is itself or ", mappedCard)
            else:
                print( "Modulus:" , max(MapCards(lastCard), mappedCard) % min(MapCards(lastCard) , mappedCard))
            print( "divisor:" , int(max(MapCards(lastCard), mappedCard) / min(MapCards(lastCard) , mappedCard)))
            print( (MapCards(lastCard) - mappedCard))    
            print( mappedCard - MapCards(lastCard)) 
            lastCard = MapCards(max(MapCards(lastCard), mappedCard))
            mappedLastCard = mappedCard
        else:
            lastCard = card
            mappedLastCard = mappedCard
        index+=1


def FindDupeSuitAndHiddenCard(theList):
    dSuitCard = ''
    suit = ''
    card = ''
    hearts= [i for i in theList if "_H" in i]
    clubs = [i for i in theList if "_C" in i]
    diamonds = [i for i in theList if "_D" in i]
    spades = [i for i in theList if "_S" in i]
    

    if len(hearts)>1: 
        print (hearts)
        DoCardsThingy(hearts)

    elif len(diamonds)>1: 
        print  (diamonds)
        DoCardsThingy(diamonds)
    elif len(spades)>1: 
        print (spades)
        DoCardsThingy(spades)

    elif len(clubs)>1: 
        print (clubs)
        DoCardsThingy(clubs)
    return dSuitCard;

# the meat and the potatoes
def SelectHiddenCard(pickedList):
    suitCard = FindDupeSuitAndHiddenCard(pickedList) 
    
    hiddenCard = suitCard   
    return hiddenCard

##################################################
# main() code starts here 
##################################################
deckStart = 0
deckEnd = 13
pickedList =[]
numCards=5   # 5 cards

deckList = MakeDeck()
for i in range(0,numCards):
    pickedList.append(PickCards(pickedList))

print(pickedList)   

SelectHiddenCard(pickedList)

# Now we have the list, the first 4 we know so we have to do something to display it where the last 
# one will be guessed.  
# The order in which the last three cards are revealed communicates the number 
# WE USE THE CARD TYPE AND SUIT. E.G., CDHS => CLUBS, DIAMONDS, HEARTS, SPADES
# according to the following scheme:
#                           A 
#                        K     2
#                      Q         3
#                     J           4
#                     10          5
#                       9       6
#                         8   7
#
#
# One of these two cards is revealed first, and the other becomes the secret card. 
# The card that is revealed is the card from which we can reach the other card 
# clockwise in 6 or fewer hops
#=============================================================================
# ( small, medium, large ) = 1          SML    If you have 2 or 3 cards with same value, you can fall back on the suit order
# ( small, large, medium ) = 2          SLM 
# ( medium, small, large ) = 3          MSL
# ( medium, large, small ) = 4          MLS
# ( large, small, medium ) = 5          LSM
# ( large, medium, small ) = 6          LMS
#=============================================================================
##################################################################################################




