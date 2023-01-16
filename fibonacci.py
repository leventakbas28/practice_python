user_input = int(input("How many Fibonacci numbers? "))

def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci_list = [fibonacci(n) for n in range(user_input)]
print(fibonacci_list)




    