#Print all prime numbers between 1–100

def primeNumbers(n):
    for i in range(2,n):
        prime=1
        for j in range(2,i):
            if i%j==0:
                prime=0
        if prime==1:
            print(i,end=" ")

primeNumbers(100)
            
        