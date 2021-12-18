"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculator():
    operand_1 = input('Input the first operand: ')
    operand_2 = input('Input the second operand: ')
    operation = input('Input operator (+, -, *, / or 0 to exit): ')
    if operation not in '/+-*0':
        print('You inputted a wrong operator!')
        return calculator()
    if not operand_1.isdigit() or not operand_1.isdigit():
        print('You inputted not a number(s)')
        return calculator()
    if operation == '/' and operand_2 == '0':
        print('You cannot divide on zero')
        return calculator()
    result = eval(f'{int(operand_1)}{operation}{int(operand_2)}')
    if operation == '0':
        return result
    print(f'Result: {result}')
    return calculator()


if __name__ == '__main__':
    calculator()
