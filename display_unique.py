numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-number to stop): "))
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.append(num)
    except ValueError:
        print("Invalid input detected. Program stopped.")
        break
