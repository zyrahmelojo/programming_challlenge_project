def custom_rjust(s, width, fillchar=" "):
    if len(s) >= width:
        return s
    return (fillchar * (width - len(s))) + s

print(custom_rjust("42", 5))