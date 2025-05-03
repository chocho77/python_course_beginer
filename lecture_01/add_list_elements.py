my_list  = []
number = int(input("Enter number of elements in array = "))
for i in range(number):
    n = int(input(f"mylist[{i}] = "))
    my_list.append(n)

for el in my_list:
    print(f"el = {el}")

print(my_list)

