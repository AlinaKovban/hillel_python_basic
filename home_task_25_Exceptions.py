
class Negative_exponentiation(Exception):
    def __init__(self, massage='Negative_exponentiation'):
        super().__init__(massage)
        
class Calculator:
    def add(self, number_1, number_2):
        try:
            return(int(number_1) + int(number_2))
        except ValueError:
            return 'You did not input number'
    
    def subtract(self, number_1, number_2):
        try:
            return(int(number_1) - int(number_2))
        except ValueError:
            return 'You did not input number'
    
    def multiply(self, number_1, number_2):
        try:
            return(int(number_1) * int(number_2))
        except ValueError:
            return 'You did not input number'
    
    def divide(self, number_1, number_2):
        try:
            return(int(number_1) / int(number_2))
        except ValueError:
            return 'You did not input number'
        except ZeroDivisionError:
            return 'Can not divide by zero'
            
    
    def exponentiation(self, number_1, number_2):
        try:
            if int(number_1) < 0 or int(number_2) < 0:
                raise Negative_exponentiation
            else:
                return(int(number_1) ** int(number_2))        
        except ValueError:
            return 'You did not input number'
        except Negative_exponentiation:
            return 'Negative_exponentiation'
    
    def square_root(self, number_1, number_2):
        try:
            return(int(number_1) ** 0.5, int(number_2) ** 0.5)
        except ValueError:
            return 'You did not input number'
    
calculator = Calculator()

number_1 = input('Input number 1:')
number_2 = input('Input number 2:')
number_operation = input('Input number operation (+, -, *, /, **, sqrt):')
    

if number_operation == '+':
    add = calculator.add(number_1, number_2)
    print(add)
elif number_operation == '-':
    subtract = calculator.subtract(number_1, number_2)
    print(subtract)
elif number_operation == '*':
    multiply = calculator.multiply(number_1, number_2)
    print(multiply)
elif number_operation == '/':
    divide = calculator.divide(number_1, number_2)
    print(divide)
elif number_operation == '**':
    exponentiation = calculator.exponentiation(number_1, number_2)
    print(exponentiation)
elif number_operation == 'sqrt':
    square_root = calculator.square_root(number_1, number_2)
    print(square_root)
else:
    print('Incorrect operation')
    
    