user_input = input("Please enter your input: ")

with open("new_input_file.txt", "w") as open_file:
    open_file.write(user_input)
    