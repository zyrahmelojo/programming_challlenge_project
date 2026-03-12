numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers with duplicates (shown once):")
for num in set(numbers):
    if numbers.count(num) > 1:
        print(num)

