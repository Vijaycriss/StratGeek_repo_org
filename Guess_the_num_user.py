import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    step_count = 0
    list = []
    while feedback != 'c':
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ".lower())
        list.append(guess)
        if feedback == 'h':
            high = guess -1
            print(f"compy the {guess} is too high")
        elif feedback == 'l':
            low = guess + 1
            print(f"compy the {guess} is too low")
        step_count+=1
    
    print(f"Ooh! compy you guessed the number {guess}, correctly in {step_count} times")
    print(list)


computer_guess(10)
    