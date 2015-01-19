count = 0
sn = []
sm = []

while count < 10:
    name = input("Student Name ")
    marks = int(input(name + "'s Marks "))
    if marks > 20 or marks < 0:
        print("Invalid Marks")
        exit("Error")
    sn.append(name)
    sm.append(marks)
    count += 1

count = 0

while count < 10:
    print(sn[count] + ":" + str(sm[count]))
    print()
    count += 1