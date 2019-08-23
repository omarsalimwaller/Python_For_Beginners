import random
word_bank = ["Musician", "Trending", "Power", "Rage", "Winning", "Run", "Love", "Construction", "Destruction"]

user_guess = ''
attempts = 3
score = 0
on = True

print('Enter x to exit.')

while on and attempts > 0:
    word = word_bank[random.randrange(len(word_bank))]
    word_list = list(word)
    for i in range(0,15):
        random_num1 = random.randrange(len(word_list))
        random_num2 = random.randrange(len(word_list))

        if random_num1 != random_num2:
            temp = word_list[random_num1]
            word_list[random_num1] = word_list[random_num2]
            word_list[random_num2] = temp
    
       
    print("".join(word_list).lower())

    while ((user_guess.lower() != word.lower()) and (attempts > 0) and on):

        user_guess = input("Guess the word: ")

        if user_guess.lower() == word.lower():
            print("Correct")
            score += 1
            print("Your score: %s" %(score))
            

        elif user_guess.lower() == 'x':
            on = False
            print("Exiting")
        else:
            print("Incorrect")
            attempts -= 1
            print("Attempts left: %s" %(attempts))


