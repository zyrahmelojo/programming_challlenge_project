numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-number to stop): "))
        numbers.append(num)
    except ValueError:
        print("Invalid input detected. Program stopped.")
        break

if numbers:
    max_count = 0
    most_duplicate = None
    for num in set(numbers):
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            most_duplicate = num

    if max_count > 1:
        print("The number with the most duplicates is:", most_duplicate)
        print("It appeared", max_count, "times.")
    else:
        print("No duplicates were entered.")
else:
    print("No valid numbers were entered.")
