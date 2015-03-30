from tkinter import *


win = Tk()
count = 0
sn = []
sm1 = []
sm2 = []
st = []
sa =[]
noST = 2

while count < noST:
    e = Entry(win)
    e.pack()
    e.insert(0, "Student Name")

    name = input("Student Name ")
    marks = input(name + "'s First Test Marks ")
    marks2 = input(name + "'s Second Test Marks ")

    try:
        marks = int(marks);
    except:
        print("Data Type Wrong")
        count -= 1
    try:
        marks2 = int(marks2);
    except:
        print("Data Type Wrong")
        count -= 1

    try:
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
    except:
        continue


count = 0

while count < noST:
    print()
    print(sn[count] + " : " + str(sm1[count]) + " : " + str(sm2[count]) + " : " + str(st[count]) + " : " + str(sa[count]))
    print()
    count += 1

tk.mainloop()