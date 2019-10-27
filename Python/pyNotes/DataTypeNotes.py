#Data type notes 

splitter_length = 100 
splitter_character = '*'
section_splitter = '\n' + splitter_character * splitter_length + '\n'

a=11.9
print('When casting with the int function:')
print('int() will round down...')
print('a = ' + str(a) + ' and then int(a) = ' + str(int(a)) + ',if you don\'t believe me? Check the code homie...')

print(section_splitter)

#None
print('when assigned as a value None will not print in the REPL')
print('try it in the REPL')
print('>>> a = None')
print('>>>a')
print('See what happened?')

print(section_splitter)

#bool
x = 0
y = -1
print('bool will treat 0 as false, and any value as true')
print('x = ' + str(x) + ' and then bool(x) = ' + str(bool(x)) + ',if you don\'t believe me? Check the code homie...')
print('y = ' + str(y) + ' and then bool(y) = ' + str(bool(y)) + ',if you don\'t believe me? Check the code homie...')
