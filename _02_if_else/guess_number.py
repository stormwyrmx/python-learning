import random

randint = random.randint(1,10)
question="Guess the _00_number between 1 and 10:"
message_small="too small,please try again"
message_large="too large,please try again"
congratulation="Congratulations! You guess the right _00_number!"
message_sorry=f"Sorry, you have used up all the chances, the correct _00_number is:{randint}"
result= False

for i in range(3):
    guess_number = int(input(question))
    if guess_number<randint:
        print(message_small)
    elif guess_number>randint:
        print(message_large)
    elif guess_number==randint:
        result=True
        break

if result:
    print(congratulation)
elif result:
    print(message_sorry)
