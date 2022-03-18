import random
score_history = {'wins': 0, 'losses': 0, 'drawn': 0}

def user_selection():
    user_input = input('Choose R, P or S: ').upper()
    user_dictionary = {'R': 'Rock,', 'P': 'Paper', 'S': 'Scissors'}
    choice_as_word = user_dictionary[user_input]
    if user_input == 'R':
        user_input = 0
    elif user_input == 'P':
        user_input = 1
    elif user_input == 'S':
        user_input = 2
    else:
        print('Unrecognised character entered')
    print('You have chosen: ', choice_as_word)
    return user_input

def computer_selection():
    number = random.randint(0, 2)
    choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    computer_choice_as_word = choices[number]
    print('The computer chose: ', computer_choice_as_word)
    return number

def result(user, computer):
    if user == computer:
        print('You have drawn')
        score_history['drawn'] += 1
    elif (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
        print('You have lost')
        score_history['losses'] += 1
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print('You have won')
        score_history['wins'] += 1
    else:
        print('rps code is broken')

def rps():
    user_input = user_selection()
    computer_input = computer_selection()
    game_result = result(user_input, computer_input)
    return game_result

while True:
    rps()
    replay = input('Would you like to play again? Enter yes or no: ').upper()
    print("You have won ", score_history['wins'], " games.", "\nYou have lost ", score_history['losses'], " games.", "\nYou have drawn ", score_history['drawn'], " games.")
    if replay != "YES":
        print('Have a nice day')
        break



