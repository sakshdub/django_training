def reverse_words(sentence):
    rev = ""
    word = ""
    for char in sentence:
        if char != " ":
            word += char
        else:
            if word:
                rev = word + " " + rev
                word = ""
    if word:
        rev = word + " " + rev
    return rev.strip()

sentence = "Python is fun"
print(reverse_words(sentence))
