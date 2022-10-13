entered_list = input().split()
num_list = list(map(int, entered_list))

counter = 0

for i in num_list:
    if (i >= 0):
        counter += 1

print(counter)
