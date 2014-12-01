func = input('Mark or Age calculator? ')

def mark():
    totl = int(input('Enter the total amount of marks: '))
    mrks = int(input('Enter how many marks you got: '))

    if (totl < mrks):
        print ("You entered false data!")
        exit()


    perc = mrks/totl * 100

    if(perc > 100):
        print ("You entered false data!")
        exit()

    if(perc < 1):
        print ("You entered false data!")
        exit()

    perc = str(int(perc))

    print("Your have approximately " + perc + "%")

def age ():
    age = int(input("What is your age? "))
    dob = int(input("What day where you born on? "))
    mob = int(input("What month where you born in? "))

    if(age > 110):
        print ("You entered false data!")
        exit()

    if(age < 0):
        print ("You entered false data!")
        exit()

    if(dob > 31):
        print ("You entered false data!")
        exit()

    if(dob < 1):
        print ("You entered false data!")
        exit()

    if(mob > 12):
        print ("You entered false data!")
        exit()

    if(mob < 1):
        print ("You entered false data!")
        exit()

    day_age = ((12-mob)*31) + (age*365) - (31-dob)
    print ("Your age in days is approxiamtely: " + str(day_age))
    print ("Your age in hours is approxiamtely: " + str(day_age*24))




if(func == "mark"):
    mark()
else:
    age()