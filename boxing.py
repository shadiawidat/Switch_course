import random

print("1 - 2 = Jab – Cross ,3 - 4 = Lead Hook – Rear Hook ,5 - 6 = Lead Uppercut – Rear Uppercut")
while True:
    try:
        opponent_move = int(input("enter a number representing a boxing move from 1 to 6: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while type(opponent_move) != int or opponent_move not in range(1,7):
    print("illegal move try again")
    while True:
        try:
            opponent_move = int(input("enter a number representing a boxing move from 1 to 6: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
opponent_move = int(opponent_move)
my_move = random.randrange(1,5)
result = True
if opponent_move in [3,4]:
    opponent_move = 3
elif opponent_move in [5,6]:
    opponent_move = 4


moves = {
    "1": "The Jab",
    "2": "The Cross",
    "3": "The Hook",
    "4": "The Uppercut"
}
print("your move is :", moves[str(opponent_move)])
print("my move is :",moves[str(my_move)])
if opponent_move == my_move:
    print("Draw")
elif my_move == 1 and opponent_move == 4 or opponent_move < my_move:
    print("You lose")
elif my_move == 4 and opponent_move == 1 or opponent_move > my_move:
    print("You win")

