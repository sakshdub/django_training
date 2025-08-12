def longest_word(sentence):
    maxWord = ""
    for word in sentence.split():
        if len(word) > len(maxWord):
            maxWord = word
    print(maxWord)

longest_word("My name is saksham")
