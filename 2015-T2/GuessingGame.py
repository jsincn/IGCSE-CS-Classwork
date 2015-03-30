correct = int(input("Player 1 enter your number: "))

def check(val):
    if val == correct:
        return True
    else:
        return False

def turn():
    val = int(input("Player 2 enter your guess: "))
    correct2 = bool(check(val))
    if correct2 == True:
        print("Player 2 won")
        exit("Game Over")
    else:
        return False

no = 0
x = True
while x == True:
    if no == 9:
        print("Player 1 won")
        exit("Game Over")
    if turn() == True:
        x = False
    no += 1