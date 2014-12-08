totl = int(input('Enter the total amount of marks: '))
mrks = int(input('Enter how many marks you got: '))

if (totl < mrks):
    print ("You entered false data!")
    exit()


perc = mrks/totl * 100

if(perc > 100):
    print ("You entered false data!")
    exit()

if(perc < 0):
    print ("You entered false data!")
    exit()

if perc >= 86:
    grade = "A*"
elif perc >= 75:
    grade = "A"
elif perc >= 64:
    grade = "B"
elif perc >= 54:
    grade = "C"
elif perc >= 46:
    grade = "D"
elif perc >= 38:
    grade = "E"
elif perc >= 30:
    grade = "F"
elif perc >= 22:
    grade = "G"
elif perc >= 0:
    grade = "U"
else:
    print("An error Occured")

perc = str(int(perc))




print("Your have approximately " + perc + "%")
print("This means you got an " + grade)