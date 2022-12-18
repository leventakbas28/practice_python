number = int(input("Please enter your number: "))
initial_divisors = range(1,number+1)
final_divisors = []
for divisor in initial_divisors:
    if number % divisor == 0:
        final_divisors.append(divisor)
print(final_divisors)
