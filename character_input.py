name = input("What is your name? ")
age = int(input("What is your age? "))
repeat = int(input("How many repeats? "))
year = 2022 + (100 - age)
while (repeat > 0):
    print("You will 100 years old at {year}".format(year = year))
    repeat -= 1