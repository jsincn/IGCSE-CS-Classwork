n, nn, s = int(input("n ")), 1, 0
while nn<= n:
    if nn%3==0:
        s += nn
    elif nn%5==0:
        s += nn
    nn += 1;
print(s)