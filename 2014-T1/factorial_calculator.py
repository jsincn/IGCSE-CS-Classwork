inp = int(input("Calculate the factorial of:"))
res = 1

while inp > 0:
    res *= inp
    inp -= 1

print(res)

