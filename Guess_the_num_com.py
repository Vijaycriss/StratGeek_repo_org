import random
list = []
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    step_count = 0
    while(guess != random_number):
        guess = int(input(f"Guess a number between 1 to {x}: "))
        list.append(guess)
        if guess > random_number:
            print(f"Oops! you are so close but {guess} is too high..")
        elif guess < random_number:
            print(f"Oh! As you are high but {guess} is too low..")
        step_count+=1
        
    print(f"Hah Finally You have guessed the number {guess} in {step_count} times")
    print(f"The numbers you have entered are {list}")
    

guess(20)

