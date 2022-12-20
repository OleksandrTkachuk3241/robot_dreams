input_value = input("Введите текст: ")


for symbol in input_value:
    if symbol.isdigit():
        print(f"Это {symbol} 'число'")
        if int(symbol) % 2 == 0:
            print(f'Число "{symbol}" - парное')
        else:
            print(f'Это число "{symbol}" - не парное')

    elif not symbol.isalnum():
        print(f'Это "{symbol}" - символ')
    elif symbol.isalpha():
        print(f'Это "{symbol}" - буква')
        if symbol.upper() == symbol:
            print(f'Буква "{symbol}" большая')
        else:
            print(f'Буква "{symbol}" маленькая')