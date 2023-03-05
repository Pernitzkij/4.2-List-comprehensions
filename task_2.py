syring = input('Введите строку: ')
simvol = input('Введите символ: ')






kvadro = [(x * 2) for x in list(syring)]
print(f'Список удвоенных символов: {kvadro}')

print(f'Склейка с дополнительным символом: {[y + str(simvol) for y in list(kvadro)]}')