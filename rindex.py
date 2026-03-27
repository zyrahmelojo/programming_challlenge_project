def custom_rindex(s, sub):
    for i in range(len(s) - len(sub), -1, -1):
        if s[i:i+len(sub)] == sub:
            return i
    raise ValueError("substring not found")

print(custom_rindex("banana", "na"))