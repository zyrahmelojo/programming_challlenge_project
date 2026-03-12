numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers (duplicates only shown once):")
seen = set()
for num in numbers:
    if num not in seen:
        print(num)
        seen.add(num)
