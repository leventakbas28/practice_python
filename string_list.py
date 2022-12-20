input_string = input("Please enter your word: ")
backwards_string= input_string[::-1]
print(backwards_string)
if input_string == backwards_string:
    print("Palindrome!")
else:
    print("Not palindrome!")