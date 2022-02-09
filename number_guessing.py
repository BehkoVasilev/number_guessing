from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo = """ 
_   _       _                 _____                     _       
| \ | |     | |               |  __ \                   (_)      
|  \| |_   _| |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __  
| . ` | | | | '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ 
| |\  | |_| | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | |
\_| \_/\__,_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|


               _____   ___  ___  ___ _____                       
              |  __ \ / _ \ |  \/  ||  ___|                      
              | |  \// /_\ \| .  . || |__                        
              | | __ |  _  || |\/| ||  __|                       
              | |_\ \| | | || |  | || |___                       
               \____/\_| |_/\_|  |_/\____/ """


def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while True:
        if level == "easy" or level == 'hard':
            if level == "easy":
                return EASY_LEVEL_TURNS
            else:
                return HARD_LEVEL_TURNS
        else:
            level = input("Invalid difficulty! Type 'easy' or 'hard': ")

def game():
  print(logo)

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    try:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
    except ValueError:
        print("Type a valid number.")


game()
