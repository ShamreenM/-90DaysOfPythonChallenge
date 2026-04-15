#Reverse a string manually without slicing

city = "Bangalore"
#print(city[::-1])
rev=""
for i in city:
    rev = i+rev
print(rev)