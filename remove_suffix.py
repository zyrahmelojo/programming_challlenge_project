def custom_removesuffix(s, suffix):
    if s[len(s)-len(suffix):] == suffix:
        return s[:len(s)-len(suffix)]
    return s

print(custom_removesuffix("filename.txt", ".txt"))