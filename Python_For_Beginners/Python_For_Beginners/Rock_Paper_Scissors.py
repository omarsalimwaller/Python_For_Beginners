import random

human_input = ''
computer_score = 0
human_score = 0
input_options = ['r','p','s','q']

while human_input != 'q':
    computer_choice = input_options[random.randrange(0,3)]
    human_input = input("Make your selection, R for rock, P for paper, and S for scissors. ")
    human_input = human_input.lower()
    if human_input not in input_options:
        print("Invalid Entry")
    else:
        if human_input == 'q':
            print("Exiting game..")

        elif computer_choice == human_input:
            print("Tie")
            computer_score += 1
            human_score += 1
            print("Score")
            print("Human: %s Computer: %s", human_score, computer_score)

        elif ((computer_choice == 'r' and human_input == 'p') or
             (computer_choice == 'p' and human_input == 's') or 
             (computer_choice == 's' and human_input == 'r')):
            print("You won that round")
            human_score += 1
            print("Score")
            print("Human: %s Computer: %s" %(human_score, computer_score))

        else:
            print("PC won that round")
            computer_score += 1
            print("Score")
            print("Human: %s Computer: %s" %(human_score, computer_score))

        if ((computer_score == 2 and human_score < 2) or (computer_score == 3 and human_score == 2)):
            print("Computer wins!")
            human_input ='q'
        
        elif ((human_score == 2 and computer_score < 2) or (human_score == 3 and computer_score == 2)):
            print("You win!")
            human_input ='q'


    


