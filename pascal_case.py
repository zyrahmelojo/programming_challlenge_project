fullname = input("Enter your fullname in incorrect casing: ")
pascal = ''.join(word.capitalize() for word in fullname.split())
print(pascal)
