user_input = input("Please enter your input: ")
#print(user_input)

def reverse(input):
    reverse_list = input.split(" ")
    reverse_list.reverse()
    reverse_string = " ".join(reverse_list)
    return reverse_string

print(reverse(user_input))