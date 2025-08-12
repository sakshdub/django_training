def rotate_list(lst,k):
    for i in range(k):
        lst.insert(0,lst.pop())
    print(list)
list=[1,2,3,4,5]
k=2
rotate_list(list,k)