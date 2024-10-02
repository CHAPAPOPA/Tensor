def subtract_large_numbers(num1: str, num2: str) -> str:
    """
    Функция для посимвольного вычитания одного длинного числа из другого.

    Args:
        num1 (str): Первое число, из которого вычитается.
        num2 (str): Второе число, которое вычитается.

    Returns:
        str: Результат вычитания (с учётом знака).
    """
    # Определяем, если второе число больше, то результат будет отрицательным
    negative = False
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        num1, num2 = num2, num1  # Меняем числа местами для правильного вычитания
        negative = True  # Отмечаем, что результат будет отрицательным

    # Приводим второе число к той же длине, что и первое, добавляя нули в начало
    num1 = list(num1)
    num2 = list(num2.zfill(len(num1)))

    result = []  # Список для хранения результата
    borrow = 0  # Переменная для хранения переноса при вычитании

    # Вычитание чисел посимвольно с конца
    for i in range(len(num1) - 1, -1, -1):
        digit1 = int(num1[i])  # Текущая цифра первого числа
        digit2 = int(num2[i]) + borrow  # Текущая цифра второго числа + перенос

        if digit1 < digit2:  # Если цифра первого числа меньше, добавляем 10 и занимаем
            digit1 += 10
            borrow = 1  # Фиксируем перенос для следующего разряда
        else:
            borrow = 0

        result.append(str(digit1 - digit2))  # Добавляем результат в список

    # Удаляем ведущие нули из результата
    while result and result[-1] == "0":
        result.pop()

    if not result:  # Если результат пустой (все нули), то результат 0
        return "0"

    # Собираем результат в строку и разворачиваем его (так как добавляли цифры с конца)
    result = "".join(reversed(result))

    if negative:  # Если результат отрицательный, добавляем минус
        result = "-" + result

    return result


# Пример использования
print(subtract_large_numbers("5", "5"))  # 0
print(subtract_large_numbers("100", "3"))  # 97
print(subtract_large_numbers("3", "100"))  # -97
print(subtract_large_numbers("100000000000001234567", "12345"))  # 100000000000001222222
