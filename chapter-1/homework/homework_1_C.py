entered_list = input().split()
num_list = list(map(int, entered_list))

def get_unique_numbers(numbers):
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)
    return unique

list_unique = get_unique_numbers(num_list)
print(len(list_unique))



