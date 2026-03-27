def custom_islower(s):
    for ch in s:
        if 'A' <= ch <= 'Z':
            return False
    return True

print(custom_islower("hello"))  # True
print(custom_islower("Hello"))  # False