user_input = int(input("Please enter your number: "))
divisors = range(2, user_input)
prime = True
for number in divisors:
    if user_input % number == 0:
        print("Not a prime number")
        prime = False
        break
if prime is True:
    print("Prime number")