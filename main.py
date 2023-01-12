from deck import *
from random import sample, shuffle

#Rules
#Usually two-player. Each player starts with an equal number of cards, until the deck is completely divided. In a move, each player places the card at the top of their deck down. The player whose card is a greater number (assuming jack = 11, queen = 12, king = 13, ace = 14, and joker = 15) keeps their card and takes the card of the other player. The game ends when one player has all the cards. 

# deck of cards
cards = [clubs2, diamonds2, hearts2, spades2, clubs3, diamonds3, hearts3, spades3, clubs4, diamonds4, hearts4, spades4, clubs5, diamonds5, hearts5, spades5, clubs6, diamonds6, hearts6, spades6, clubs7, diamonds7, hearts7, spades7, clubs8, diamonds8, hearts8, spades8, clubs9, diamonds9, hearts9, spades9, clubs10, diamonds10, hearts10, spades10, clubsJack, diamondsJack, heartsJack, spadesJack, clubsQueen, diamondsQueen, heartsQueen, spadesQueen, clubsKing, diamondsKing, heartsKing, spadesKing, clubsAce, diamondsAce, heartsAce, spadesAce, joker1, joker2]
print("Cards =", cards)
print("Length=", len(cards), "\n")
shuffledCards = sample(cards, len(cards))
print("Shuffled:", shuffledCards, "\n")
#print(shuffle(cards))
#shuffle the deck
# cards = shuffle(cards)
# print("Shuffled =", cards)

# #deal
player1 = []
player2 = []
# for i in range (0, len(cards) / 2):
#   player1.append(cards[i])
# for i in range(len(cards) / 2, len(cards)):
#   player2.append(cards[i])
for i in range(0, len(cards)):
  if i % 2 == 1:
    player1.append(shuffledCards[i])
  else:
    player2.append(shuffledCards[i])
print("Player 1 =", player1, "\n")
print("Player 2 =", player2, "\n")

#after playing this card, the player shuffles their deck
# player1LastCard = player1[len(player1) - 1]
# player2LastCard = player2[len(player2) - 1]

# #move counter
moves = 0

# #while both players still have cards 
while len(player1) != 0 and len(player2) != 0:
  #Each player puts down the card at the top of their deck. The player whose card is greater takes the other player's card.
  # if player1[0] == player1LastCard:
  #   player1 = shuffle(player1)
  # if player2[0] == player2LastCard:
  #   player2 = shuffle(player2)

  print("Player 1:", player1[0], "\n")
  print("Player 2:", player2[0], "\n")
    
  if player1[0] > player2[0]:
    print("Player 1 wins \n")
    #player 1's most recently played card goes at the bottom of their deck
  #player1[len(player1) - 1] = player1[0]
    player1.append(player1[0])
    player1.append(player2[0])
    player2.pop(0)
    for i in range(1, len(player1)):
      #the new card at the top of player 1's deck becomes the next card they play
      player1[i - 1] = player1[i] 
    player1.pop(len(player1) - 1)
    print("New Player 1 =", player1, "\n")
    print("New Player 2 =", player2, "\n")
  elif player1[0] < player2[0]:
    print("Player 2 wins \n")
    #player 2's most recently played card goes at the bottom of their deck
  #player2[len(player2) - 1] = player2[0]
    player2.append(player2[0])
    player2.append(player1[0])
    player1.pop(0)
    for i in range(1, len(player2)):
      #the new card at the top of player 2's deck becomes the next card they play
      player2[i - 1] = player2[i] 
    player2.pop(len(player2) - 1)
  else:
    player1.append(player1[0])
    player1.pop(0)
    player2.append(player2[0])
    player2.pop(0)
  print("New Player 2 =", player2, "\n")
  print("New Player 1 =", player1, "\n")
  moves += 1
  print("Moves:", moves, "\n")

#the winner has captured the full deck
if len(player1) == 0:
  print("Winner: Player 2")
else:
  print("Winner: Player 1")
  

    





