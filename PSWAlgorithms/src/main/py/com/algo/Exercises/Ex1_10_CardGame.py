'''
Created on Jan 31, 2020

@author: goyalpushkar
'''

import random

class Card(object):
    '''
    classdocs
    '''
    
    def __init__(self, value, typeP):
        '''
        Constructor
        '''
        self.cardValue = value
        self.cardType = typeP
        
    def get_card(self):
        return self.cardValue, self.cardType
    
    def __str__(self):
        return str(self.cardValue) + " of " + self.cardType
    
class CardDeck():
    
    def __init__(self):
        self.cardTypes = ('HEART', 'DIAMOND', 'CLUB', 'SPADE')
        self.cardHigherValues = ('A', 'J', 'Q', 'K')
        self.cardLowerValues = ( index for index in range(2, 11, 1))
        self.deckOfCards = []
        
        for value in self.cardLowerValues:
            for cardType in self.cardTypes:
                card = Card( str(value), cardType)
                self.deckOfCards.append(card)
                
        for value in self.cardHigherValues:
            for cardType in self.cardTypes:
                card = Card( str(value), cardType)
                self.deckOfCards.append(card)
                
    def get_any_card(self):
        randomNum = random.randrange(0, 52)
        #print(randomNum)
        #print( len(self.deckOfCards) )
        #print( self.deckOfCards[randomNum] )
        return self.deckOfCards[randomNum]
        
    def get_card(self, cardP):
        for cards in self.deckOfCards:
            if cards.cardValue == cardP.cardValue and cards.cardType == cardP.cardType:
                return cards
    
    def get_number_card(self, numberP):
        for cards in self.deckOfCards:
            if cards.cardValue == numberP:
                return cards
       
    def get_type_card(self, typeP):
        for cards in self.deckOfCards:
            if cards.cardType == typeP.upper():
                return cards
            
    def pop(self):
        #value = self.deckOfCards[len(self.deckOfCards)-1].pop()
        #self.deckOfCards[len(self.deckOfCards)-1] = None
        #return value
        return self.deckOfCards.pop()
    
    def isEmpty(self):
        return len(self.deckOfCards) == 0 
    
    def shuffle_cards(self, numOfShuffles):
        shuffleNum = 26
        if not (numOfShuffles is None ):
            shuffleNum = numOfShuffles
            
        #shuffleTimes = random.randrange(1, shuffleNum)
        for shuffleTime in range(1, int(shuffleNum) ,1):
            randomNum1 = random.randrange(0, 52)
            randomNum2 = random.randrange(0, 52)
            self.deckOfCards[randomNum1], self.deckOfCards[randomNum2] = self.deckOfCards[randomNum2], self.deckOfCards[randomNum1]
            '''
            temp1 = self.deckOfCards[randomNum1]
            temp2 = self.deckOfCards[randomNum2]
            self.deckOfCards[randomNum1] = temp2
            self.deckOfCards[randomNum2] = temp1
            '''
        
    def print_cards(self):
        #for cards in self.deckOfCards:
        #     print( cards.__str__() )
        for index in range( 1, len(self.deckOfCards) + 1, 1 ):
            print( str(index) + " : " + self.deckOfCards[index-1].__str__() )   
        
def testCards( function, deckOfCardsP=None, cardValue=None, cardType=None, shuffleNumber=None ):
    
    #Get Deck of Cards #Reinitialize
    if function.upper() == 'GET_DECK' or function.upper() == 'REINITIALIZE_CARDS':
        deckCards = CardDeck()
        return deckCards
    
    #print initial cards
    if function.upper() == 'PRINT_CARDS':
        deckOfCardsP.print_cards()
        return deckOfCardsP
    
    #shuffle cards
    if function.upper() == 'SHUFFLE_CARDS':
        deckOfCardsP.shuffle_cards(shuffleNumber)
        deckOfCardsP.print_cards()
        return deckOfCardsP
    
        #Re shuffle cards
        #deckOfCardsP.shuffle_cards()
        #deckOfCardsP.print_cards()

    #get Specific Card
    if function.upper() == 'GET_SPECIFIC_CARD':
        card = Card(cardValue, cardType)
        card.__str__()
        receivedCard = deckOfCardsP.get_card(card)
        return receivedCard
        #receivedCard.__str__()
    
    #get any card 
    if function.upper() == 'GET_ANY_CARD':
        receivedCard = deckOfCardsP.get_any_card()
        #print( str(receivedCard.cardValue) + ":" + receivedCard.cardType )
        return receivedCard
        #receivedCard.__str__()
    
    #get number card
    if function.upper() == 'GET_NUMBER_CARD':
        receivedCard = deckOfCardsP.get_number_card(cardValue)
        return receivedCard
        #receivedCard.__str__()
    
    #get type card
    if function.upper() == 'GET_TYPE_CARD':
        receivedCard = deckOfCardsP.get_type_card(cardType)
        return receivedCard
        #receivedCard.__str__()
        

def set_operation(operationValue):
    if operationValue == "1":
        return "GET_DECK"
    elif operationValue == "2":
        return "PRINT_CARDS"
    elif operationValue == "3":
        return "REINITIALIZE_CARDS"
    elif operationValue == "4":
        return "SHUFFLE_CARDS"
    elif operationValue == "5":
        return "GET_ANY_CARD"
    elif operationValue == "6":
        return "GET_SPECIFIC_CARD"
    elif operationValue == "7":
        return "GET_NUMBER_CARD"
    elif operationValue == "8":
        return "GET_TYPE_CARD"
    elif operationValue == "9":
        return "PLAY_GAME"
    else:
        return "Q"
    
def playGame(numOfTimes):
  
    deckCards1 = CardDeck()
    deckCards2 = CardDeck()
    
    deckCards1.shuffle_cards(52)
    deckCards2.shuffle_cards(52)
    #deckCards1 = deckCards1.shuffle_cards(52)
    #deckCards2 = deckCards2.shuffle_cards(52)
   
    preference = {'HEART':4, 'DIAMOND':3, 'CLUB':2, 'SPADE':1}
    
    player1Count = 0
    player2Count = 0
    index = 1
    while ( ( not deckCards1.isEmpty() ) and ( not deckCards2.isEmpty() ) and index <= numOfTimes ):
        print("\n Turn Number: " + str(index) )
        card1 = deckCards1.pop() #pop()  get_any_card()
        card2 = deckCards2.pop()  #pop()  get_any_card()
        
        if preference[card1.get_card()[1]] > preference[card2.get_card()[1]]:
            print( "Player1 Card: " + card1.__str__())
            print( "Player2 Card: " + card2.__str__()) 
            print( "Player1 won" )
            player1Count += 1
        elif preference[card1.get_card()[1]] < preference[card2.get_card()[1]]:
            print( "Player1 Card: " + card1.__str__())
            print( "Player2 Card: " + card2.__str__()) 
            print( "Player2 won" )
            player2Count += 1        
        elif preference[card1.get_card()[1]] == preference[card2.get_card()[1]]:
            if card1.get_card()[0] > card2.get_card()[0]:
                print( "Player1 Card: " + card1.__str__())
                print( "Player2 Card: " + card2.__str__()) 
                print( "Player1 won" )
                player1Count += 1    
            elif card1.get_card()[0] < card2.get_card()[0]:
                print( "Player1 Card: " + card1.__str__())
                print( "Player2 Card: " + card2.__str__()) 
                print( "Player2 won" )
                player2Count += 1    
            else:
                print( "Player1 Card: " + card1.__str__())
                print( "Player2 Card: " + card2.__str__()) 
                print( "WAR!!!" )
                                      
        index += 1
        
    print("\n")
    if player1Count > player2Count:
        print( "Player1 won the whole game")
    elif player1Count < player2Count:
        print( "Player2 won the whole game")
    else:
        print( "Its Draw")
        
    print( "Player1 winning Count - " + str(player1Count) )
    print( "Player2 winning Count - " + str(player2Count) )
    print("\n")
    
def main(): 
    deckOfCards = testCards("GET_DECK")

    print( "Enter User input as following functions: " )
    print( "\t 1. GET_DECK" )
    print( "\t 2. PRINT_CARDS" )
    print( "\t 3. REINITIALIZE_CARDS" )
    print( "\t 4. SHUFFLE_CARDS" )
    print( "\t 5. GET_ANY_CARD" )
    print( "\t 6. GET_SPECIFIC_CARD" )
    print( "\t 7. GET_NUMBER_CARD" )
    print( "\t 8. GET_TYPE_CARD" )
    print( "\t 9. PLAY_GAME" )
    raw_user_input = raw_input("Tell operation you want to perform or Q to quit: ")
    user_input = set_operation(raw_user_input) 
    while user_input.upper() != 'Q':
        
        shuffleNum = None
        cardType = None
        cardValue = None            
            
        if user_input.upper() == 'SHUFFLE_CARDS':
            shuffleNumYN = raw_input("Do you want to pass shuffle numbers (Y/N): ")
            if not (shuffleNumYN == None) and shuffleNumYN.upper() == 'Y':
                shuffleNum = raw_input("Enter Shuffle Numbers or Q to quit: ")
                if shuffleNum.upper() == 'Q':
                    break
            
        if user_input.upper() == 'GET_SPECIFIC_CARD':
            cardValue = raw_input("Pass card Value or Q to quit: ")
            cardType = raw_input("Pass card Type or Q to quit: ")
            if cardValue == 'Q' or cardType == 'Q':
                break
            
        if user_input.upper() == 'GET_NUMBER_CARD':
            cardValue = raw_input("Pass card Value or Q to quit: ")
            if cardValue == 'Q':
                break
            
        if user_input.upper() == 'GET_TYPE_CARD':
            cardType = raw_input("Pass card Type or Q to quit: ")
            if cardType == 'Q':
                break
            
        if user_input.upper() in ('REINITIALIZE_CARDS', 'GET_DECK', 'PRINT_CARDS', 'SHUFFLE_CARDS'):
            deckOfCards = testCards( user_input, deckOfCards, cardValue, cardType, shuffleNum)
        elif user_input.upper() == 'PLAY_GAME':
            noOfTimes = raw_input("Number of times to play the game or Q to quit: ")
            if noOfTimes.upper() == 'Q':
                break
            
            playGame( int(noOfTimes) )
            
        else:
            individualCard = testCards( user_input, deckOfCards, cardValue, cardType, shuffleNum)
            #print( str(individualCard.cardValue) + ":" + individualCard.cardType )
            print( individualCard.__str__() )
            
        print( "Enter User input as following functions: " )
        print( "\t 1. GET_DECK" )
        print( "\t 2. PRINT_CARDS" )
        print( "\t 3. REINITIALIZE_CARDS" )
        print( "\t 4. SHUFFLE_CARDS" )
        print( "\t 5. GET_ANY_CARD" )
        print( "\t 6. GET_SPECIFIC_CARD" )
        print( "\t 7. GET_NUMBER_CARD" )
        print( "\t 8. GET_TYPE_CARD" )
        print( "\t 9. PLAY_GAME" )
        raw_user_input = raw_input("Tell operation you want to perform or Q to quit: ")
        user_input = set_operation(raw_user_input) 
            
            
            
main()