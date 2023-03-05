def calc_price(price, percent):
    return round(price * (1 + percent/100), 2)


price = [1, 2, 3, 4, 5, 6, 7]
price_one_percent = int(input('Повышение на первый год: '))
price_two_percent = int(input('Повышение на второй год: '))


one_price = [calc_price(i_price, price_one_percent) for i_price in price]
two_price = [calc_price(i_price, price_two_percent) for i_price in price]


print(f'Повышение на первый год: {one_price}')
print(f'Повышение на второй год: {two_price}')

print(f'Сумма цен за каждый год: {sum(price)}  {sum(one_price)}  {sum(two_price)}')
