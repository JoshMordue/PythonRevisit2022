answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher!")
    guess = int(input())
    if guess == answer:
        print("You got it the second time!")
elif guess > answer:
    print("Please guess lower!")
    guess = int(input())
    if guess == answer:
        print("You got it the second time!")
else:
    print("You got it first time!")