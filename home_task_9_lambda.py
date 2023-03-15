number = int(input('Напиши число:'))


even_or_odd = lambda number: 'It is zero' if number == 0 else 'Even' if number % 2 == 0 else 'Odd'

    
print(even_or_odd(number))
