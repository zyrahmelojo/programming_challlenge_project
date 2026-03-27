def custom_zfill(s, width):
    if s.startswith(("+", "-")):
        sign = s[0]
        s = s[1:]
        return sign + ("0" * (width - len(s) - 1)) + s
    return ("0" * (width - len(s))) + s

print(custom_zfill("42", 5))   # "00042"
print(custom_zfill("-42", 5))  # "-0042"