even_numbers = 0

for i in range(10):
    num  = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_numbers += 1

print("The number of even numbers is:", even_numbers)