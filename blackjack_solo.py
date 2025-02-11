from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
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
  print_header(name + ' TURN')
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
  print_header('GAME RESULT')

  if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
    print('You win!')
  elif user_hand > 21 or (dealer_hand <= 21 and dealer_hand > user_hand):
    print('Dealer wins!')
  else:
    print('Push.')


# USER'S TURN
user_hand = draw_starting_hand("YOUR")
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
  
# DEALER'S TURN
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  print("Dealer has {}.".format(dealer_hand))
  dealer_hand = dealer_hand + draw_card()
print_end_turn_status(dealer_hand)

# GAME RESULT
print_end_game_status(user_hand, dealer_hand)


import io
import unittest
from unittest.mock import patch
import sys

def __run_function(func, func_input=None, func_input_more=None):
  """
  Runs given function with given inputs

  Args:
    func - function to run
    func_input - optional function input if provided function requires input
  """
  if func_input_more != None:
    return func(func_input, func_input_more)
  if func_input != None:
    return func(func_input)
  else:
    return func()

def get_print(func, func_input=None, func_input_more=None):
  """
  Saves printed statements and returns

  Args:
    func - function to run
    func_input - optional function input if provided function requires input
  """
  old_stdout = sys.stdout
  new_stdout = io.StringIO()
  sys.stdout = new_stdout
  __run_function(func, func_input, func_input_more)
  output = new_stdout.getvalue()
  sys.stdout = old_stdout
  return output

def mock_random(mocked_ints, func, func_input=None):
  """
  Runs given function with mocked out random numbers

  Args:
    func - function to run
    func_input - optional function input if provided function requires input
  """
  with patch("blackjack_helper.randint") as randint_mock:
    randint_mock.side_effect = mocked_ints
    return __run_function(func, func_input)


import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 3), "Drew a 3\n")
    self.assertEqual(get_print(print_card_name, 9), "Drew a 9\n")

    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")

    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")

    self.assertEqual(get_print(print_card_name, -7), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")


  def test_draw_card(self):
    self.assertEqual(mock_random([5], draw_card), 5)
    self.assertEqual(mock_random([8], draw_card), 8)
    self.assertEqual(mock_random([10], draw_card), 10)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)

  def test_print_header(self):
    self.assertEqual(get_print(print_header, "YOUR"), "-----------\nYOUR\n-----------\n")
    self.assertEqual(get_print(print_header, "DEALER"), "-----------\nDEALER\n-----------\n")
    self.assertEqual(get_print(print_header, "JAKE"), "-----------\nJAKE\n-----------\n")
    self.assertEqual(get_print(print_header, "3"), "-----------\n3\n-----------\n")
        


  def test_draw_starting_hand(self):
    output = mock_random([3, 6], draw_starting_hand, "DEALER")
    self.assertEqual(output, 9)
    output2 = mock_random([1, 9], draw_starting_hand, "YOUR")
    self.assertEqual(output2, 20)
    output3 = mock_random([1, 11], draw_starting_hand, "DEALER")
    self.assertEqual(output3, 21)
    output4 = mock_random([12, 13], draw_starting_hand, "YOUR")
    self.assertEqual(output4, 20)
    output5 = mock_random([8, 1], draw_starting_hand, "DEALER")
    self.assertEqual(output5, 19)
    output6 = mock_random([11, 5], draw_starting_hand, "YOUR")
    self.assertEqual(output6, 15)

  def test_print_end_turn_status(self):
    expected_output_1 = "Final hand: 28.\nBUST.\n"
    self.assertEqual(get_print(print_end_turn_status, 28), expected_output_1)
    expected_output_2 = "Final hand: 21.\nBLACKJACK!\n"
    self.assertEqual(get_print(print_end_turn_status, 21), expected_output_2)
    expected_output_3 = "Final hand: 15.\n"
    self.assertEqual(get_print(print_end_turn_status, 15), expected_output_3)
        
  def test_print_end_game_status(self):
    expected_output_1 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 23, 26), expected_output_1)
    expected_output_2 = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 17, 17), expected_output_2)
    expected_output_3 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 19, 21), expected_output_3)
    expected_output_4 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 24, 18), expected_output_4)
    expected_output_5 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 15, 17), expected_output_5)
    expected_output_6 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 21, 17), expected_output_6)
    expected_output_7 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 18,25), expected_output_7)
    expected_output_8 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 18, 15), expected_output_8)
    expected_output_9 = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 21, 21), expected_output_9)






    
    
    
    
    


if __name__ == '__main__':
    unittest.main()