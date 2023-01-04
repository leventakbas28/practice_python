import random

counter = 0
while True:
    random_number = random.randint(1,9)
    user_number = int(input("Guess the number: "))
    counter += 1
    if user_number < random_number:
        print("Too low")
    elif user_number > random_number:
        print("Too high")
    elif user_number == random_number:
        print("Right guess!")
        break
    user_input = input("Exit or Try Again? ").lower()
    if user_input == "exit":
        break
    else:
        continue
print("Total guess number: {counter}".format(counter = counter))
    