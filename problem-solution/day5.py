#Count vowels, consonants, digits, and special characters
import re

class getCharacterTypes:
    def vowels(self,char):
        vow =['a','e','i','o','u']
        if char.lower() in vow:
            print(char)
            return 1
        else:
            return 0

    def consonants(self, char):
        vow =['a','e','i','o','u']
        if char.isalpha():
            if char not in vow:
                return 1
            return 0
        return 0

    def isDigits(self,char):
        if char.isdigit():
            return 1
        else:
            return 0
        
    def isSpecialCharacter(self,char):
        if not char.isalnum():
            return 1
        else:
            return 0
    

sentence = "India 1!"
sentence = sentence.lower()
vowels = 0
consonants = 0
isDigits = 0
isSpecialCharacter = 0
getCharList = getCharacterTypes()
for char in sentence:
    vowels = vowels + getCharList.vowels(char)
    consonants = consonants + getCharList.consonants(char)
    isDigits = isDigits + getCharList.isDigits(char)
    isSpecialCharacter = isSpecialCharacter + getCharList.isSpecialCharacter(char)

print("Number of Vowels: ",vowels)
print("Number of consonants: ",consonants)
print("Number of Digits: " ,isDigits)
print("Number of Special Characters: ",isSpecialCharacter)