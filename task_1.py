left_gran = int(input('Левая граница: '))
ring_gran = int(input('Правая граница: '))

kvadro = [x ** 2 for x in range(left_gran, ring_gran + 1)]
print(f'Список квадратов чисел в диапазоне от {left_gran} до {ring_gran}: {kvadro}')
kubo = [x ** 3 for x in range(left_gran, ring_gran + 1)]
print(f'Список кубов чисел в диапазоне от {left_gran} до {ring_gran}: {kubo}')