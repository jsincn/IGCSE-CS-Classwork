# Function Definition Exercises

# Exercise 1
# Define a function called "two" that always returns the number 2.
def two():
    return 2
    pass

# Exercise 2
# Define a function called "repeat" that, given 1 string,
# returns that string twice, separated by a space.
def repeat(string):
    print(string)
    print(" ")
    print(string)
    pass

# Exercise 3
# Define a function called "larger" that returns the larger
# of two input numbers.
def larger(x, y):
    if x > y:
        return x
    else:
        return y
    pass

# Exercise 4
# Define a function called "square" that returns the square
# of its one input.
def square(x):
    return x*x
    pass


# Exercise 6
# Define a function called "numbers" that returns all of the numbers
# from 1 to 10,000 , inclusive, separated by spaces.
def numbers():
    x=1
    while x < 10001:
        print(x)
        x += 1
    pass

numbers()