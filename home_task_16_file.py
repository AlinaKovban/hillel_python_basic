line_1 = input('Write 1:')
line_2 = input('Write 2:')
line_3 = input('Write 3:')
line_4 = input('Write 4:')

file = open('file.txt', 'w')
file.write(line_1 + '\n')
file.write(line_2 + '\n')
file.close

file = open('file.txt', 'a')
file.write(line_3 + '\n')
file.write(line_4 + '\n')
file.close

