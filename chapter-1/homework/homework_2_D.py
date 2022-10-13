entered_list = input().split()
num_list = list(map(int, entered_list))

lenght = len(num_list)
y = num_list[lenght - 1]
del num_list[lenght - 1]
num_list.insert(0, y)
print(num_list)