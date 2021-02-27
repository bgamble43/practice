from art import logo
import random

def add1():
  index = 0
  index = random.randint(0, 12)
  card = cards[index]
  # print(card)
  return card

def deal():
  player_cards = []
  dealer_cards = []
  for i in range(2):
    player_cards += [add1()]
    dealer_cards += [add1()]
  return dealer_cards, player_cards

# ----
# Player Functions
# ----
def player_score(player_cards):
  player_total = 0
  for i in player_cards:
    player_total += i
  if player_total > 21 and 11 in player_cards:
    player_total = 0  
    for i in range(len(player_cards)):
      if player_cards[i] == 11:
        player_cards[i] = 1
        print("*** Ace changed to 1. ***")
    for i in player_cards:
      player_total += i
  return player_total

def print_player(player_cards, player_total):
  print(f"Your cards: {player_cards}, total score: {player_total}")

def score_check(player_total, hit):
  if player_total < 22 and hit == "y":
    proceed = True
    return proceed
  if player_total < 22 and hit == "n":
    proceed = False
    return proceed
  else:
    print(f"Player busts with {player_total}")
    proceed = False
    return proceed

def player_turn(player_cards):
  hit = input("Hit? y/n: ")
  if hit == "y":
    player_cards += [add1()]
    return player_cards, hit
  else:
    return player_cards, hit

# ----
# Dealer Functions
# ----
def dealer_score(dealer_cards):
  # print(f"Dealer cards: {dealer_cards}")
  dealer_total = 0
  for i in dealer_cards:
    dealer_total += i
  if dealer_total > 21 and 11 in dealer_cards:
    dealer_total = 0  
    for i in range(len(dealer_cards)):
      if dealer_cards[i] == 11:
        dealer_cards[i] = 1
        print("*** Ace changed to 1. ***")
    for i in dealer_cards:
      dealer_total += i
  return dealer_total

def print_dealer(dealer_cards, dealer_total):
  print(f"Dealer cards: {dealer_cards}, total score: {dealer_total}")

def dealer_score_check(dealer_total):
  if dealer_total < 22 and dealer_total > 16:
    proceed = False
    return proceed
  if dealer_total < 17:
    proceed = True
    return proceed
  else:
    proceed = False
    return proceed

def dealer_turn(dealer_cards):
  dealer_cards += [add1()]
  return dealer_cards
  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 11, 11]

print(logo)

# Deal initial cards to dealer and player
dealer_cards, player_cards = deal()
# Print dealer cards, hide second card
print(f"Computer's first card: {dealer_cards[0]}")
# Calculate player total
player_total = player_score(player_cards)
# Print player cards and total
print_player(player_cards, player_total)

# Begin player sequence
print("-----------------------")
print("------ YOUR TURN ------")
print("-----------------------")
if player_total == 21:
  print("Blackjack!")
  proceed = False
else:
  proceed = True
while proceed == True:
  # If player is dealt 21 move to dealer sequence
  if player_total != 21:
    # Player takes a turn
    player_cards, hit = player_turn(player_cards)
    # Calculate player total
    player_total = player_score(player_cards)
    # Print player cards and total
    print_player(player_cards, player_total)
    # Check player score, set "proceed" to False if player busts
    proceed = score_check(player_total, hit)
  else:
    proceed = False

# Begin dealer sequence
if player_total < 22:
  print("---------------------------")
  print("------ DEALER'S TURN ------")
  print("---------------------------")
  dealer_total = dealer_score(dealer_cards)
  if dealer_total < 17:
    proceed = True
  else:
    proceed = False
    # Print dealer cards and total
    print_dealer(dealer_cards, dealer_total)
  while proceed == True:
    # Dealer takes a turn
    dealer_cards = dealer_turn(dealer_cards)
    # Calculate dealer total
    dealer_total = dealer_score(dealer_cards)
    # Print dealer cards and total
    print_dealer(dealer_cards, dealer_total)
    # Check dealer score, set "proceed" to False if dealer busts
    proceed = dealer_score_check(dealer_total)
  print("==========================")
  print(f"Dealer total: {dealer_total}")
  print(f"Player total: {player_total}")
  print("==========================")
  if dealer_total > 21:
    print(f"Dealer busts with {dealer_total}")
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print(f"          You win!")
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
  elif dealer_total > player_total:
    print(":( :( :( :( :( :( :( ")
    print("      House wins.")
    print(":( :( :( :( :( :( :( ")
  elif player_total > dealer_total:
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("           You win!")
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
  else:
    print("- - - - - ")
    print("  Push.")
    print("- - - - - ")
else:
  print(":( :( :( :( :( :( :( ")
  print("      House wins.")
  print(":( :( :( :( :( :( :( ")
