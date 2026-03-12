numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-number to stop): "))
        numbers.append(num)
    except ValueError:
        print("Invalid input detected. Program stopped.")
        break

if numbers:
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
else:
    print("No valid numbers were entered.")
