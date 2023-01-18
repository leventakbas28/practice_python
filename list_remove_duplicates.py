import random
sample_list = random.sample(range(1,20),10)
print(sample_list)

def remove_duplicates(input_list):
    final_list =[]
    final_list = [n for n in input_list if n not in final_list]
    return final_list

print(remove_duplicates(sample_list))