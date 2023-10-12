def f_addition(x, y):
    return x+y


def f_subtraction(x, y):
    return x-y


def f_multiplication(x, y):
    return x*y


def f_division(x, y):
    return round(x/y, 3)


def f_integer_division(x, y):
    return x//y


def f_remainder_of_division(x, y):
    return x % y


def f_factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result


def f_fibonacci(x):
    fib = [0, 1, 1]
    for i in range(3, x):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def main_menu():
    play = True
    while play:
        answer = input("1. Сложение\n"
                       "2. Вычитание\n"
                       "3. Умножение\n"
                       "4. Деление\n"
                       "5. Возведение в степень\n"
                       "6. Целочисленное деление\n"
                       "7. Остаток от деления\n"
                       "8. Факториал числа\n"
                       "9. Последовательность Фибоначчи\n"
                       "10. Выход\n")
        match answer:
            case "1":
                print(f_addition(int(input('Введите первое слагаемое: ')),
                      int(input('Введите второе слагаемое: '))))
            case "2":
                print(f_subtraction(int(input('Введите уменьшаемое: ')),
                      int(input('Введите вычитаемое : '))))
            case "3":
                print(f_multiplication(int(input('Введите первый множитель: ')),
                      int(input('Введите второй множитель: '))))
            case "4":
                print(f_division(int(input('Введите делимое: ')),
                      int(input('Введите делитель: '))))
            case "5":
                print(pow(int(input('Введите число: ')),
                      int(input('Введите степень: '))))
            case "6":
                print(f_integer_division(int(input('Введите делимое: ')),
                      int(input('Введите делитель: '))))
            case "7":
                print(f_remainder_of_division(int(input('Введите делимое: ')),
                      int(input('Введите делитель: '))))
            case "8":
                print(f_factorial(int(input('Введите число: '))))
            case "9":
                print(f_fibonacci(int(input('Введите длинну последовательности Фибоначчи: '))))
            case "10":
                play = False
            case _:
                print('Укажите операцию ')


main_menu()
