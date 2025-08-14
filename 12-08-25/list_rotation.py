def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # handle cases where k > n
    return lst[-k:] + lst[:-k]
input_list = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(input_list, k))