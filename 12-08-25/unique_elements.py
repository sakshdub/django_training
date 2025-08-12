def unique_elements(lst):
    res=[]
    for i in lst:
        if i not in res:
            res.append(i)
    return res

list=[1,2,2,3,4,1,5]
print(unique_elements(list))