import random

def compare(input):
    random_number = str(random.randint(1000, 9999))
    #random_number = "1234"
    cow = 0
    bull = 0
    for i in range(4):
        if random_number[i] == input[i]:
            cow += 1
        else:
            bull += 1
    #print(random_number)
    print("{cow} cows, {bull} bulls".format(cow = cow, bull = bull))
    return cow

while True:
    while True:
        user_input = input("Please guess the number: ") 
        if user_input.isdigit():
            if len(user_input) == 4:
                break
            else:
                print("Wrong input. Try again!")
                continue                
        else:
            print("Wrong input. Try again!")
            continue
    cows = compare(user_input)
    if cows == 4:
        print("Success!")
        break
    else:
        run_input = input("Try again or exit? ").lower()
        if run_input == "exit":
            break
        else:
            continue

    
