import random

card_deck = (['Ace Spades','2 Spades','3 Spades','4 Spades','5 Spades','6 Spades','7 Spades','8 Spades','9 Spades','10 Spades','Jack Spades','Queen Spades','King Spades'] + ['Ace Hearts','2 Hearts','3 Hearts','4 Hearts','5 Hearts','6 Hearts','7 Hearts','8 Hearts','9 Hearts','10 Hearts','Jack Hearts','Queen Hearts','King Hearts']
+ ['Ace Clubs','2 Clubs','3 Clubs','4 Clubs','5 Clubs','6 Clubs','7 Clubs','8 Clubs','9 Clubs','10 Clubs','Jack Clubs','Queen Clubs','King Clubs']
+ ['Ace Diamonds','2 Diamonds','3 Diamonds','4 Diamonds','5 Diamonds','6 Diamonds','7 Diamonds','8 Diamonds','9 Diamonds','10 Diamonds','Jack Diamonds','Queen Diamonds','King Diamonds'])

# for x in range(0,5):
#     print(card_deck[x])

players = []
dealer = []

def deal_card():
    index = random.randint(0, len(card_deck) - 1 )
    return card_deck.pop(index)

def calc_score(hand):
    score = {"Ace1" : 0 , "AcesHigh" : 0 }
    if is_natural(hand) :
        return -1
    else:
        for c in hand:
            if ( is_royal ( c) ) :
                score["Ace1"] += 10
                score["AcesHigh"] += 10
            elif ( is_ace ( c) ):
                score["Ace1"] += 1
                score["AcesHigh"] += 11
            else:
#             score += int(c[:2])
#             print ( c, c[:2] )
                score["Ace1"] += int ( c[:2])
                score["AcesHigh"] += int ( c[:2])
    return score

def is_royal ( card ):
    return ( "Jack" in card or "Queen" in card or "King" in card )

def is_ace (card ):
    return ( "Ace" in card )

def has_royal ( hand ) :
    for card in hand :
        if is_royal(card) :
            return True
    return False

def has_ace ( hand ) :
    for card in hand :
        if is_ace(card) :
            return True
    return False

def is_natural ( hand ):
    return has_royal(hand) and has_ace(hand)

def show_hand(hand):
    for c in hand:
        print(c)
        
        
# Main code to run...
scores = {}   
num_players = int(input("How many players?"))
scores["Dealer"] =  0
for x in range(1, num_players + 1 ):
    scores[str(x)] =  0
    players.append([])

for x in range(0,2):
    for p in players:
        # get a card
        dealt = deal_card()
        # put in players hand
        p.append(dealt)
    dealt = deal_card()
    dealer.append(dealt)


print("\nDealer")
show_hand(dealer)
score = calc_score(dealer)
scores["Dealer"] = score
scoreAce1 = score ["Ace1"]
scoreAceHigh = score ["AcesHigh"]
if ( scoreAce1 == scoreAceHigh ) :
    print("Score : " , scoreAce1)
else :
    print ("Aces Low Score", scoreAce1)
    print ("Aces High Score", scoreAceHigh)

player_num = 0
for p in players :
    player_num += 1
    print("\nPlayer " + str(player_num) )
    show_hand(p)
    score = calc_score(p)
    scores[str(player_num)] = score
    scoreAce1 = score ["Ace1"]
    scoreAceHigh = score ["AcesHigh"]
    if ( scoreAce1 == scoreAceHigh ) :
        print("Score : " , scoreAce1)
    else :
        print ("Aces Low Score", scoreAce1)
        print ("Aces High Score", scoreAceHigh)

print("\n")
result = {}
print("Scores...")
print (scores)
for player in scores :
    score = scores [ player ]
#     print(player)
#     print(score)
    ace1 = score["Ace1"]
    aceHigh = score ["AcesHigh"]
    result[player] = aceHigh
    
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_by_value = sorted(x.items(), key=lambda kv: kv[1])

results = sorted ( result.items(), key= lambda kv: kv[1])

results.reverse()

winners = {}
prevScore = 0
for result in results :
    if ( prevScore == result[1] or prevScore == 0 ) :
        prevScore = result[1]
        winner = result[0]
        if ( winner != "Dealer" ) :
            winner = "Player " + winner
        print ("Winner is {} with a score of {}".format(winner, result[1]))
        continue
    else:
        break
    
    
        
    
    
    
#     for x in result:
#         print(x)
#     winners.append(result)

# print ("Winner is {}".format(winner))
    
# result = sorted(result.values())
# result.reverse()
# 
# print("Results...")
# print(result)


#     print ("Winner is {} with a score of {}".format(r[0], r[1]))

# for item in sorted(result.items()) :
# #     print "%s: %s" % (key, value)
#     print ("item = {}".format(item))
# for key in sorted(result.keys()) :
# #     print "%s: %s" % (key, value)
#     print ("key = {}".format(key))
#     
# for value in sorted(result.values()) :
#     print ("value = {}".format(value))
#     if ( high_score > 0 ):
#         if (aceHigh > high_score ) :
#             high_score = aceHigh
#             top_score.append(player)
#         elif ( aceHigh == high_score ):
#             top_score.append(player)
#         if ( ace1 == aceHigh ):
#             print ("Player : {} scored {}".format(player, ace1))
#         else:
#             print ("Player : {} scored {} with Ace Low and {} with Ace High".format(player, ace1, aceHigh))
#     else:
#         high_score = aceHigh
#         high_score_player = player 
    #     print ("Ace 1 {} and Ace High {}".format(ace1, aceHigh))
    #    display winner
# print(high_score)
# print (top_score)
# if ( len(top_score) > 1 ) :
#     # we have more than 1 winner
#     print("We have {} Winners!".format(len(top_score)))
#     for player in top_score :
#         print ("Winner {}".format(player))
# else :
#     print ("Winner is {}".format(top_score[0]))
    


