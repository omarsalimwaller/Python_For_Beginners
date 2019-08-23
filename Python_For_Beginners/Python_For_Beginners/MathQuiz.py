import random
level = ''
user_input = ''
number1 = 0
number2 = 0
score = 0

difficulty = {1:[0,9], 2:[0,99], 3:[0,999], 4:[0,9999]}
print("Choose difficulty level.")
print("Enter 1 for easy.")
print("Enter 2 for intermediate.")
print("Enter 3 for hard.")
print("Enter 4 for I need a calculator.")
level = input('')
level = int(level)
print("Enter your answer")

#10 question Test
for i in range(1,11):

    #Choose number based on difficulty.
    number1 = random.randrange(difficulty[level][0], difficulty[level][1])
    number2 = random.randrange(difficulty[level][0], difficulty[level][1])

    print("%s) %s + %s = " %(i,number1,number2))
    user_input = input("")
    if user_input == '':
        user_input = 0

    #Check the answer
    if int(user_input) == (number1+number2):
        print("Correct")
        score +=10
    else:
        print("Incorrect")
        print("Correct answer is %s" %(number1 +number2))

print("Final score: %s" %(score))

