logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):

  """Take a list of cards and return the score calculated from the cards"""


  if sum(cards) == 21 and len(cards) == 2 :
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "draw"
    elif user_score==0:
        return "You win with a blacl jack"
    elif computer_score==0:
        return "you lose computer have a black jack"
    elif user_score>21:
        return "Lose you went over "
    elif computer_score>21:
        return "win computer went over"
    elif user_score>computer_score:
        return "you won"
    else:
        return "lost"
def play_game():

    user_cards = []
    computer_cards = []
    game=False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game:

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)



        print(f"user card{user_cards} current score {user_score}")
        print(f"computer first card {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            game=True
        else:
            x = input("do you want to draw a card ? yes or no : ")
            if x == 'yes':
                user_cards.append(deal_card())
            else:
                game=True


    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"your hand {user_cards}  your score {user_score} ")
    print(f"computer hand {computer_cards} computer score {computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play blackjack?? y or n :")=='y':
    print(logo)
    play_game()

