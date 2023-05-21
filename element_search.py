import random

def number_search(number, number_list):
    if number in number_list:
        return True
    else:
        return False

def binary_search(number, number_list):
    while True:
        

while True:
    user_number = int(input("Enter the number:"))
    random_list = sorted(random.sample(range(1,100), 10))
    constant_list = [5, 10, 12, 36, 47, 65]
    print(random_list)
    print(number_search(user_number, random_list))
    print(number_search(user_number, constant_list))