for i in range(1, 101):  # 1 to 100
    if (i % 3 == 0) ^ (i % 5 == 0):  # XOR: only one condition true
        print(i, end=" ")
