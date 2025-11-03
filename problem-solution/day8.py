#Remove duplicates and sort a list without using set()

l1=[1,3,4,5,1,3,5,7,3,2,10]
result=list()
#remove duplicates
for ele in l1:
    if ele not in result:
        result.append(ele)

for i in range(0,len(result)):
    for j in range(i,len(result)-1):
        if result[i]>result[j]:
            result[i],result[j]=result[j],result[i]
print(result)