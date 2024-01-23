import random

def rps():
    user  = input("Enter your choice!, 'r' for rock , 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return "Its a tie"
    
    if is_win(user, computer):
        return f'You win! {user} beats {computer}'

    return f'You lost! {computer} beats {user}'
    
def is_win(player, opponent):
    #r>s p>r s>p  
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
     
print(rps())