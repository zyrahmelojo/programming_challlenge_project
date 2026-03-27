def custom_startswith(s, prefix):
    return s[:len(prefix)] == prefix

print(custom_startswith("hello world", "hello"))