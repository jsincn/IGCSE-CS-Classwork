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

perc = round(perc, 5)
if(perc <= 0.1):
    die(10)
pe_str = str(perc)

print("Your have approximately " + pe_str + "%")