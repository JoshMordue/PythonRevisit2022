low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press Enter to start")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}, should I guess higher or lower? " 
                     "Enter H or L or C if my guess was correct:"
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. the low end of the range becomes one greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess + 1

    elif high_low == "c":
        print("I got it in {} Guesses!".format(guesses))
        break

    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} Guesses!".format(guesses))