# fruits=["apple","banana","cherry","kiwi"]
# for i in fruits:
#     if(i=="banana"):
#         print(i)
#         break

# sum
# def sum_num(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
 
# num = int(input("Enter a number: "))
# print(sum_num(num))

# def count_vowels(word):
#     vowels = "aeiouAEIOU"
#     count = 0   
#     for char in word:
#         if char in vowels:
#             count +=1
#     return count

# word = input("Enter a word: ")
# print("Number of vowels in the word:", count_vowels(word))

# def reverse_string(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result

# print(reverse_string("python"))
# words_length = ["apple", "banana", "cherry", "kiwi"]

# for word in words_length:
#     print(f"The word '{word}' has {len(word)} characters.")

    
def factorial(n):
    if(n<0):
        print("Enter positive number")
        return None
    res = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(n, 1, -1):
            res *= i
        return res

print(factorial(5))  # Output: 120
