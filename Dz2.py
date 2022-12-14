i = (input("Введите текст: "))
if (i.isdigit()) == True:
    I = int(i)
    if I % 2 == 0:
        print("Вы ввели парное число")
    else:
        print("Вы ввели не парное число")
else:
    x = (len(i))
    print("Вы ввели слово длинною в " + str(x) + " символа(ов)")