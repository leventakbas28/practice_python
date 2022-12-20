while True:
    input_fp = str(input("First Player --> Rock, Paper or Scissors: "))
    input_fp = input_fp.lower()
    while True:
        if input_fp == "rock" or input_fp == "paper" or input_fp == "scissors":
            break
        else:
            input_fp = str(input("Invalid input! Try again: "))
    input_sp = str(input("Second Player --> Rock, Paper or Scissors: "))
    input_sp = input_sp.lower()
    while True:
        if input_sp == "rock" or input_sp == "paper" or input_sp == "scissors":
            break
        else:
            input_sp = str(input("Invalid input! Try again: "))

    if input_fp == "rock":
        if input_sp == "rock":
            print("Draw")
        elif input_sp == "paper":
            print("Second player wins")
        elif input_sp == "scissors":
            print("First player wins")
    elif input_fp == "paper":
        if input_sp == "rock":
            print("First player wins")
        elif input_sp == "paper":
            print("Draw")
        elif input_sp == "scissors":
            print("Second Player wins")
    elif input_fp == "scissors":
        if input_sp == "rock":
            print("Second player wins")
        elif input_sp == "paper":
            print("First player wins")
        elif input_sp == "scissors":
            print("Draw")
    input_continue = int(input("Continue 1, Stop 0: "))
    if input_continue == 0:
        break