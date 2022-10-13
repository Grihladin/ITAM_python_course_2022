string = input()
new_string = 'string'
index = 0

for i in range(len(string)):
    if (string[i].isupper() == True):
        new_string = string[i]
        index = i
        break
while i != '.':
    index += 3
    i = string[index]
    new_string += i

print(new_string)