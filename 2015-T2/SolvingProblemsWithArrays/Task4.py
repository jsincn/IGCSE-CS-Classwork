count = 0
sn = []
sm1 = []
sm2 = []
st = []
sa =[]

while count < 10:
    name = input("Student Name ")
    marks = int(input(name + "'s First Test Marks "))
    marks2 = int(input(name + "'s Second Test Marks "))

    if marks > 20 or marks < 0:
        print("Invalid Marks")
        count -= 1
    elif marks2 > 25 or marks2 < 0:
        print("Invalid Marks")
        count -= 1
    else:
        sn.append(name)
        sm1.append(marks)
        sm2.append(marks)
        st.append(marks + marks2)
        av = (marks + marks2)/2
        sa.append(av)
    count += 1

count = 0

while count < 10:
    print()
    print(sn[count] + " : " + str(sm1[count]) + " : " + str(sm2[count]) + " : " + str(st[count]) + " : " + str(sa[count]))
    print()
    count += 1