def divisible(start, end):
    for num in range(start, end + 1):
        if (num % 3 == 0) ^ (num % 5 == 0):  # XOR: divisible by 3 or 5 but not both
            print(num, end=" ")

# Example usage
divisible(1, 15)
