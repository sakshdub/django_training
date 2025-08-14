def sum_of_digits(num):
    total = 0
    num = abs(num)   
    while num > 0:
        total += num % 10   
        num //= 10         
    return total

 
number = 12345
print(sum_of_digits(number))
