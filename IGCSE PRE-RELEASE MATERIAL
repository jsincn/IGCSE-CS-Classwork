def bagCheck (id_letter, weight):
    if id_letter == "G" or id_letter == "S": #case letter G or S, check that weight is appropriate (49.9 - 50.1)
        if weight < 49.9 or weight > 50.1:
            print ("The bag was rejected due to out of spec weight") #Error message if weight is incorrect
            return "rejected"; #return to main function, informs main function whether the input was accepted or rejected
        else:
            print (id_letter + " " + str(weight))
            return "accepted"; #return to main function, informs main function whether the input was accepted or rejected
    elif id_letter == "C": #case letter C, check that weight is appropriate (24.9 - 25.1)
        if weight < 24.9 or weight > 25.1:
            print ("The bag was rejected due to out of spec weight") #Error message if weight is incorrect
            return "rejected"; #return to main function, informs main function whether the input was accepted or rejected
        else:
            print (id_letter + " " + str(weight))
            return "accepted"; #return to main function, informs main function whether the input was accepted or rejected
    else:
        print("The identification letter " + str(id_letter) + "was not recognised") #Error message if the letter is not recognised. This should not occur, only for testig purposes.
        return "rejected"; #return to main function, informs main function whether the input was accepted or rejected


#Function to calcualte the price of the order        
def calcPrice(no_gravel,no_sand,no_cement):
    dicount_packs = 0 #number of discount packs in the order
    #Finds the remainder when the number of bags is divided by the number required for special packs
    remainder_gravel = no_gravel % 2
    remainder_sand = no_sand % 2
    remainder_cement = no_cement % 1
        
    #mak numbers divisible by number of bags required for special packs
    gravel_div_2 = no_gravel - remainder_gravel
    sand_div_2 = no_sand - remainder_gravel
    cement_div_1 = no_gravel - remainder_gravel
    
    #finds number of times special pack fits in sand/gravel. Not required for cement since divide by 1
    sand_div_2 = sand_div_2 / 2
    gravel_div_2 = gravel_div_2 / 2
    
    #Find the lowest of cement_div_1. sand_div_2, gravel_div_2 in order to find the number of packs that fit into the order
    if sand_div_2 <= gravel_div_2:
        if sand_div_2 <= cement_div_1:
            discount_packs = sand_div_2
        elif cement_div_1 <= sand_div_2:
            discount_packs = cement_div_1
    elif cement_div_1 <= gravel_div_2:
        if sand_div_2 <= cement_div_1:
            discount_packs = sand_div_2
        elif cement_div_1 <= sand_div_2:
            discount_packs = cement_div_1
    else:
        discount_packs = gravel_div_2
    
    #calculates the extra bags of sand leftover from the discount packs
    extra_sand = no_sand - (discount_packs * 2)
    extra_cement = no_cement - (discount_packs * 1)
    extra_gravel = no_gravel - (discount_packs * 2)
    
    original_price = (no_sand * 2) + (no_cement * 3) + (no_gravel * 2) #Finds the original price by multiplying the number of bags of each type by the appropriate price
    new_price = (discount_packs * 10) + (extra_sand * 2) + (extra_gravel * 2) + (extra_cement * 3) #Finds the discounted price by multipying the number of discount_packs by 10 and then multiplying the extra bags by the appropriate price
    
    #output the subtotal and total (original_price and new_price)
    print("Subtotal (No discount): " + str(original_price))
    print("Total (With discount): " + str(new_price))
#End of calculating price function.
        
#main function, conttaining the main program operation        
def main():
    totalWeight = 0 #initialize the total Weight for the order
    totalRejects = 0 #initialize the total number of rejected entries for the order
    
    # Input the number of sacks for each type (Gravel, Sand, Cement)
    no_gravel = input("Input number of gravel sacks (Positiv Integer): ")
    no_sand = input("Input number of sand sacks (Positiv Integer): ")
    no_cement = input("Input number of cement sacks (Positiv Integer): ")

    for i in range(no_sand): #input bags of sand
        check = "rejected" #default output for tha bagCheck
        while check == "rejected": # loop until a valid weight is entered
            weight = input("Enter weight of bag of sand: ")
            check = bagCheck("S", weight) #run check function and set the check variable to the output
            if check == "rejected":
                totalRejects += 1 #increase the total number of rejected bags when required
        totalWeight += weight #increment total weight
        
    for i in range(no_gravel): #input bags of gravel
        check = "rejected" #default output for tha bagCheck
        while check == "rejected": # loop until a valid weight is entered
            weight = input("Enter weight of bag of gravel: ")
            check = bagCheck("G", weight) #run check function and set the check variable to the output
            if check == "rejected":
                totalRejects += 1 #increase the total number of rejected bags when required
        totalWeight += weight #increment total weight
        
    for i in range(no_cement): #input bags of cement
        check = "rejected" #default output for tha bagCheck
        while check == "rejected": # loop until a valid weight is entered
            weight = input("Enter weight of bag of cement: ")
            check = bagCheck("C", weight) #run check function and set the check variable to the output
            if check == "rejected":
                totalRejects += 1 #increase the total number of rejected bags when required
        totalWeight += weight #increment total weight
    
    print("Total Weight of this order: " + str(totalWeight)) #output the total weight of the order
    print("Total rejected bags of this order: " + str(totalRejects)) #output the total number of rejected bags
    
    calcPrice(no_gravel,no_sand,no_cement) # run the calculate price function
    
#run program
main()
