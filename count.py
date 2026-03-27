def custom_count(s, sub):
    count = 0
    sub_len = len(sub)

    for i in range(len(s) - sub_len + 1):
        if s[i:i + sub_len] == sub:
            count += 1

    return count

text = "banana"
pattern = "ana"
print(f"'{pattern}' appears {custom_count(text, pattern)} times in '{text}'")
