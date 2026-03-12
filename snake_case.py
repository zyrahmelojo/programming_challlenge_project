fullname = input("Enter your fullname in incorrect casing: ")
snake = '_'.join(word.lower() for word in fullname.split())
print(snake)
