def longest_word(sentence):
    words = sentence.split()   
    longest = max(words, key=len)   
    return longest

 
sentence = "Python is an amazing programming language"
print(longest_word(sentence))
