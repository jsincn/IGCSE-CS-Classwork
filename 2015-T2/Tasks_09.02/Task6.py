no1 = int(input("Player 1 Number: "))
a = 0
preNo = 0
tries = 1
while a == 0:
    no2 = int(input("Player 2 Guess: "))
    if no2 > no1:
        print("Larger")
    elif no2 < no1:
        print("Smaller")
    elif no2 == no1:
        print("You won, you took " + str(tries) +  " tries!")
        exit("Game Over")
    else:
        pass
    if no2 != preNo:
        tries += 1
    no2 = preNo
