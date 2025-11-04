#Merge and flatten nested lists

l1 = [[1,2,3],[4,5],[6],7]
result=[]
for list in l1:
    if str(type(list))=="<class 'list'>":
        for ele in list:
            result.append(ele)
print(result)