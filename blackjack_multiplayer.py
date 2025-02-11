from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   Win (wins), L(loses), P (pushes)
def print_card_name(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  if card_rank == 8 or card_rank == 1:
    print('Drew an ' + str(card_name))
  elif card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print('Drew a ' + str(card_name))

# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
  card_rank = randint(1, 13)
  print_card_name(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  return card_value

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
  print('-----------')
  print(message)
  print('-----------')

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
  print_header(name + "'s" + ' TURN')
  return draw_card() + draw_card()

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
  print('Final hand: ' + str(hand_value) + '.')

  if hand_value == 21:
    print('BLACKJACK!')
  elif hand_value > 21:
    print('BUST.')

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
  if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
    return "W"
  elif user_hand > 21 or (dealer_hand <= 21 and dealer_hand > user_hand):
    return "L"
  else:
    return "P"
  
# Use randint to generate random cards. 

#user-turn
def user_turn(name):
  user_hand = draw_starting_hand(name.upper())
  should_hit = 'y'
  while user_hand < 21:
    should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
    if should_hit == 'n':
      break
    elif should_hit != 'y':
      print("Sorry I didn't get that.")
    else:
      user_hand = user_hand + draw_card()
  print_end_turn_status(user_hand)
  return user_hand

#dealer-turn   
def dealer_turn():
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)
  return dealer_hand
  

number_of_players = int(input("Welcome to Blackjack! How many players? "))
users = []  # Stores a 2D list of each player's [Name, Hand Value, Score]

if number_of_players:

  # Loop to gather player names and initialize hand value (0) and score (3)
  for index in range(1, number_of_players + 1):
      player_name = input(f"What is player {index}'s name? ")
      users.append([player_name, 0, 3])  # Each player starts with a score of 3

  again = 'y'  # Used to control the continuation of rounds
  number_of_eliminated = 0  # Tracks the number of players eliminated from the game

  # Main game loop; runs as long as the user wants to continue ('again' is 'y')

  name = 0
  hand = 1
  score = 2

  while again == 'y':

      # Loop over each player to handle their turn
      for rows in users:

          # Check if player is still in the game (score is not 0)
          if rows[score] != 0:
              # Call user_turn function to handle the player's hand, and update their hand value
              user_hand_value = user_turn(rows[0])
              rows[hand] = user_hand_value

      # Dealer plays their turn after all players have played
      dealer_hand_value = dealer_turn()

      # Display the result header for this round
      print_header("GAME RESULT")


      # Loop through each player's result after the dealer's turn
      for rows in users:
          if rows[score] != 0:  # Only process players who are not eliminated
              # Call function to determine the result of the game (win, lose, or push)
              result = print_end_game_status(rows[hand], dealer_hand_value)
              
              # Update the player's score based on the game result
              if result == "W":  # Player wins
                  rows[score] += 1
                  print(f"{rows[name]} wins! Score: {rows[score]}")
              elif result == "L":  # Player loses
                  rows[score] -= 1
                  print(f"{rows[name]} loses! Score: {rows[score]}")
              else:  # It's a push (tie)
                  print(f"{rows[name]} pushes. Score: {rows[score]}")
              
              # Eliminate the player if their score reaches 0
              if not rows[score]:
                  print(f"{rows[name]} eliminated!")
                  number_of_eliminated += 1

      # If all players are eliminated, the game ends
      if number_of_eliminated == number_of_players:
          print("All players eliminated!")
          break

      # Ask if players want to play another round
      again = input("Do you want to play another hand (y/n)? ")