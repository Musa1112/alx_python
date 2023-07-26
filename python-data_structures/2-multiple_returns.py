def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char

result1 = multiple_returns("Hello")
print(result1)  # Output: (5, 'H')

result2 = multiple_returns("")
print(result2)  # Output: (0, None)
