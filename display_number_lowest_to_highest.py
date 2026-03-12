numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-number to stop): "))
        numbers.append(num)
    except ValueError:
        print("Invalid input detected. Program stopped.")
        break

if numbers:
    numbers.sort()
    print("Numbers from lowest to highest:")
    for n in numbers:
        print(n)
else:
    print("No valid numbers were entered.")
