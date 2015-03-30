func, n, nn, p,s = input("Function: "), int(input("Number: ")), 1, 1, 0
if func == "sum":
    while nn<= n:
        s += nn
        nn += 1;
    print(s)
elif func == "product":
    while nn<= n:
        p *= nn
        nn += 1;
    print(p)
