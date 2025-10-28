#Implement a simple calculator using arithmetic operators

class calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        return a/b
    def percentage(self, a, b):
        return (a/b)*100

    def select_option(self, number,a,b) -> int:
        match(int(number)):
            case 1: print(self.add(a,b))
            case 2: print(self.sub(a,b))
            case 3: print(self.multiply(a,b))
            case 4: print(self.divide(a,b))
            case 5: print(self.percentage(a,b))


number = input("Select below options:" \
"       1. Addition" \
"       2. Subtraction" \
"       3. Multiplication" \
"       4. Division" \
"       5. Percentage" \
"       6. Quit: " \
"" \
"")

a = int(input("what is value of first number: "))
b = int(input("what is value of second number: "))
calc = calculator()
calc.select_option(number,a,b)

    
