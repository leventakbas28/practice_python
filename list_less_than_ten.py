initial_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
temp_list = []
check = int(input("Please enter check value: "))
for number in initial_list:
    if number < check:
        temp_list.append(number)
print(temp_list)
