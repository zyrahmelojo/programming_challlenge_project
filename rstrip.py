def custom_rstrip(s):
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    return s[:i+1]

print(custom_rstrip("Hello World   "))