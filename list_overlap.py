import random
first_list = random.sample(range(1, 10), 5)
second_list = random.sample(range(1, 20), 10)
final_list = []

for item in first_list:
    if item in second_list:
        if item not in final_list:
            final_list.append(item)
print(final_list)