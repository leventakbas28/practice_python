input_list = [5, 10, 15, 20, 25]

def list_ends(input_list):
    new_list = []
    new_list.append(input_list[0])
    new_list.append(input_list[-1])
    return new_list

print(list_ends(input_list))