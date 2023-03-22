
def func():
    while True:
        input_value = input('Нпиши число або заверши програму ("вихід", "exit", "quit", "e" або "q"):')
        if input_value.lower() in ['вихід', 'exit', 'quit', 'e', 'q']:
            break
        else: 
            func2(input_value)
        
def func2(value):
    if value.startswith('-') and value[1:].isdigit():
        print(f'Ви ввели целое отрицательное {value}')
    elif value.isdigit():
        if int(value) == 0:
            print(f'Ви ввели ноль {value}')
        else:
            int(value)
            print(f'Ви ввели целое число {value}')
    elif value.startswith('-') and '.' in value or ',' in value:
        try:
            float_value = value.replace(',', '.')
            float(float_value)
            print(f'Ви ввели отрицательное дробне число {float_value}')
        except ValueError:
            print(f'Ви ввели не число {value}')
    elif '.' in value or ',' in value and value.replace(',', '').isdigit() or value.replace('.', '').isdigit():
        try:
            float(value)
            print(f'Ви ввели дробне число {value}')
        except ValueError:
            print(f'Ви ввели не число {value}')
    else:
        print(f'Ви ввели не число {value}')
             

func()

