def char_frequency(s):
    if s is None: 
        return {}
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


print(char_frequency("banana"))  
