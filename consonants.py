text = "I love python"
vowels = "aeiouAEIOU"
consonants = ""

for ch in text:
    if ch.isalpha() and ch not in vowels:
        consonants += ch

print(consonants)
