import random 
while True : 
    choices = ['rock' , 'paper' , 'scissor']
    computer = random.choice(choices)
    player = None
    while player not in choices  :
        player = input('choose a option rock , paper , scissor  :  ').lower()
        print ( 'player choose : '+ player)
        print('computer choose : '+ computer)
        if computer == player : 
            print("it's a tie !")
        elif player == 'scissor' :
            if computer == 'rock':
                print("player loose !") 
            else:
                print("player won!")
        elif player == 'paper' :
            if computer == 'scissor':
                print("player loose !") 
            else:
                print("player won!")
        elif player == 'rock' :
            if computer == 'paper':
                print("player loose !") 
            else:
                print("player won!")
    
    playagain = input("do you wanna play again? yes/no : ").lower()
    if playagain != 'yes' :
        break    
print('bye, have a great day !')


