import random

card_deck = (['Ace Spades','2 Spades','3 Spades','4 Spades','5 Spades','6 Spades','7 Spades','8 Spades','9 Spades','10 Spades','Jack Spades','Queen Spades','King Spades'] + ['Ace Hearts','2 Hearts','3 Hearts','4 Hearts','5 Hearts','6 Hearts','7 Hearts','8 Hearts','9 Hearts','10 Hearts','Jack Hearts','Queen Hearts','King Hearts']
+ ['Ace Clubs','2 Clubs','3 Clubs','4 Clubs','5 Clubs','6 Clubs','7 Clubs','8 Clubs','9 Clubs','10 Clubs','Jack Clubs','Queen Clubs','King Clubs']
+ ['Ace Diamonds','2 Diamonds','3 Diamonds','4 Diamonds','5 Diamonds','6 Diamonds','7 Diamonds','8 Diamonds','9 Diamonds','10 Diamonds','Jack Diamonds','Queen Diamonds','King Diamonds'])

# for x in range(0,5):
#     print(card_deck[x])

player_1 = []
dealer = []

def deal_card():
    index = random.randint(0, len(card_deck) - 1 )
    return card_deck.pop(index)

def calc_score(hand):
    score = {"Ace1" : 0 , "AcesHigh" : 0 }
    for c in hand:
        if ( "Jack" in c
        or "Queen" in c
        or "King" in c ):
            score["Ace1"] += 10
            score["AcesHigh"] += 10
        elif ( "Ace" in c ):
            score["Ace1"] += 1
            score["AcesHigh"] += 11
        else:
#             score += int(c[:2])
#             print ( c, c[:2] )
            score["Ace1"] += int ( c[:2])
            score["AcesHigh"] += int ( c[:2])
    return score
            
def show_hand(hand):
    for c in hand:
        print(c)


for x in range(0,2):
    dealt = deal_card()
    player_1.append(dealt)
    dealt = deal_card()
    dealer.append(dealt)

score_dealer = {}
score_player1 = {}
results = {}
score_dealer["Ace1"] = calc_score(dealer)["Ace1"]
score_dealer["AcesHigh"] = calc_score(dealer)["AcesHigh"]
score_player1["Ace1"] = calc_score(player_1)["Ace1"]
score_player1["AcesHigh"] = calc_score(player_1)["AcesHigh"]
if ( score_dealer["Ace1"] > score_player1["Ace1"] ) :
    result = "Dealer Wins"
elif ( score_dealer["Ace1"] == score_player1["Ace1"]) :
    result = "Draw!"
else :
    result = "Player 1 Wins"
results["Ace1"] = result
if ( score_dealer["AcesHigh"] > score_player1["AcesHigh"] ) :
    result = "Dealer Wins"
elif ( score_dealer["AcesHigh"] == score_player1["AcesHigh"]) :
    result = "Draw!"
else :
    result = "Player 1 Wins"
results["AcesHigh"] = result

print ("Show Hands")
print ()
print ("Dealer")
show_hand(dealer)
print()
print("Player 1")
show_hand(player_1)
print ()
print ("Aces worth 1 scores : ")
print ( "Dealer Score : " + str(score_dealer["Ace1"]))
print ( "Player 1 Score : " + str(score_player1["Ace1"]))
print (results["Ace1"])
print()
print ("Aces High worth 11 scores : ")
print ( "Dealer Score : " + str(score_dealer["AcesHigh"]))
print ( "Player 1 Score : " + str(score_player1["AcesHigh"]))
print (results["AcesHigh"]) 
    