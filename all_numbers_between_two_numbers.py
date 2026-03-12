first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

if first_num < second_num:
    for i in range(first_num + 1, second_num):
        print(i)
else:
    for i in range(second_num + 1, first_num):
        print(i)