#Check if two strings are anagrams

s1 = "Indian"
s2 = "AIDNI"

def anagrams(s1,s2):
    l1=set()
    l2=set()
    for i in s1.lower():
        l1.add(i)
    for i in s2.lower():
        l2.add(i)
    if l1==l2:
        print("Anagrams")
    else:
        print("Not Anagrams")    
anagrams(s1,s2)