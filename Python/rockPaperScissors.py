import random

comp_score = 0
player_score = 0

def game_logic():
  possible_moves  = ['rock', 'paper', 'scissors']
  rock_win = "scissors"
  paper_win = "rock"
  scissors_win = "paper"
  comp_move = random.choice(possible_moves)
  
  player_move = input('Do You Choose Rock, Paper, or Scissors?\n').lower()
  if player_move in possible_moves:
    print(f"\nComputer Chose {comp_move.title()}\n")
  else:
    print("Ivalid Entry, Try Again...\n")
    game_logic()

  if player_move == comp_move:
    win_lose_message("tie")
  elif player_move == 'rock' and comp_move == rock_win:
    win_lose_message("win")
  elif player_move == 'paper' and comp_move == paper_win:
    win_lose_message("win")
  elif player_move == 'scissors' and comp_move == scissors_win: 
    win_lose_message("win")
  else:
    win_lose_message("lose")


def win_lose_message(status):
  if status == "win":
    print(f"You Win!\n")
  elif status == "tie":
    print(f"You Tied!\n")
  else:
    print(f"You Lose!\n")
  
  current_score(status)


def current_score(status):
  global player_score, comp_score

  if status == "win":
    player_score += 1
  elif status == "lose":
    comp_score += 1

  print(f'Player: {player_score} | Comp: {comp_score}\n')

  replay_game()


def replay_game ():
  replay = input('Try Again? [y/n]\n').lower()
  if replay == 'y' or replay == 'yes':
    game_logic()
  elif replay == 'n' or replay == 'no':
    quit()
  elif replay != 'y' or replay != 'n' or replay != 'yes' or replay != 'no':
    print("Please enter yes or no")
    replay_game()

  
game_logic()