numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-number to stop): "))
        numbers.append(num)
    except ValueError:
        print("Invalid input detected. Program stopped.")
        break

if numbers:
    print("The highest number is:", max(numbers))
else:
    print("No valid numbers were entered.")
