#Convert between int, float, string, and boolean

# converting int to float
a = 10
b = float(format(a,".2f"))
print(f"Int to float: {b:.3f}") 

# converting int to boolean
a = 10
b = bool(a)
print("Int to Bool: ",b)

# converting int to string
a = 10
b = str(a)
print("Int to string: ",b)

# converting int to string
a = 10
b = str(a)
print("Int to string: ",b)

# converting float to int
a = 10.124
b = int(a)
print("Float to int: ",b)

# converting float to string
a = 10.124
b = str(a)
print("Float to string: ",b)

# converting float to bool
a = 0
b = bool(a)
print("Float to Boolean: ",b)

'''# converting string to int - Not Allowed
a = "10.124"
b = int(a)
print("String to int: ",b)'''

'''# converting string to float - Not Allowed
a = "10.124"
b = float(a)
print("String to float: ",b)'''

# converting string to bool
a = "0"
b = bool(a)
print("String to Boolean: ",b)

# converting Bool to int
a = bool(10.124)
b = int(a)
print("Bool to int: ",b)

# converting bool to string
a = bool(10.124)
b = str(a)
print("Bool to string: ",b)

# converting bool to float
a = bool(12.56)
b = float(a)
print("Bool to Float: ",b)