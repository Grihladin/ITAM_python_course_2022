entered_list = input().split()
num_list = list(map(int, entered_list))
list_chet = []


for i in num_list:
    if (i % 2 == 0) :
        list_chet.append(i)

print (list_chet)