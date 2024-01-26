import random

ch = ['Rock', 'Paper', 'Scissor']


run = True

while run:
    x = random.choice(ch)
    y = input("Rock or Paper or Scissor: ")
    print(f"Your choice: {y}")
    print(f"Computer choice: {x}")
    if x == 'Rock' and y == 'Scissor':
        print("Computer Wins")
    elif x == 'Rock' and y == 'Paper':
        print("You win")
    elif x == 'Paper' and y == 'Scissor':
        print("You Win")
    elif x == 'Scissor' and y == 'Rock':
        print("You Win")
    elif x == 'Scissor' and y == 'Paper':
        print("Computer Win")
    elif x == 'Paper' and y == 'Rock':
        print("Computer Win")

    r = input("Do you want to continue(y/n): ")
    if r == 'y':
        print('-'*20)
        continue
    else:
        run = False

print("Thanks for playing!")
