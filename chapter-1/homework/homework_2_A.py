
x = int(input())
Positive = 0
Negative = 0
entered_list = []

for i in range(x):
    entered_string = input().split()
    entered_list.append(entered_string)

for i in entered_list:
     if('True' in i):
        Positive += 1
     else: Negative += 1

print(Positive, end=' ')
print(Negative)