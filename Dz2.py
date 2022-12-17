i = input("Введите текст: ")
if i.isdigit():
    i = int(i)
    if i % 2 == 0:
        print("Вы ввели парное число")
    else:
        print("Вы ввели не парное число")
else:
    print(f'Вы ввели слово длинною в {len(i)} символа(ов)')