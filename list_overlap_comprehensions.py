import random

list_a = random.sample(range(1,30),11)
print(list_a)
list_b = random.sample(range(1,30),15)
print(list_b)

final_list = [n for n in list_a if n in list_b]

print(final_list)