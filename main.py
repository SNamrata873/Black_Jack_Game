import os
import art
import random
def initial_cards():
  number_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  get_card=random.choice(number_list)
  return get_card

def sum_of_cards(cards):
   
  
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards) 

def compare(user_score, computer_score):
 
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"    



def main():
    from art import logo
    print(logo)
    user_cards=[]
    computer_cards=[]

    for i in range(2):
        user_cards.append(initial_cards())
        computer_cards.append(initial_cards())

    user_score=sum_of_cards(user_cards)
    print(f"Your cards are:{user_cards}, Your current score:{user_score}")
    print(f"Computer's first card is:{computer_cards[0]}")  
    is_yes=False
    while not is_yes:  
        choice_two=input("Do you want to take another card press 'y' and if want to pass press 'n':")
        if choice_two=="y":
            user_cards.append(initial_cards())
            user_score=sum_of_cards(user_cards)
            print(f"Your cards are:{user_cards},Your new score is:{user_score}")
            print(f"Computer's first card is:{computer_cards[0]}")
        elif choice_two=="n":
            print(f"Your final cards are:{user_cards},Your final score:{user_score}") 
            computer_score=sum_of_cards(computer_cards)   
            if computer_score==21 or computer_score>17:
                print(f"Computer's final cards:{computer_cards},It's final score is:{computer_score}")
            elif computer_score<17:
                computer_cards.append(initial_cards())
                computer_score=sum_of_cards(computer_cards)
                print(f"Computer's final cards:{computer_cards},It's final score:{computer_score}")
                
            print(compare(user_score,computer_score))
            break

want_to_play=False
while not want_to_play:       
    choice_one=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice_one=="y":
      os.system("cls")
      main()
    else:
      break      