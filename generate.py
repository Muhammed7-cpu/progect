import random

def generate(level: int, length: int) -> str:
    '''
    Генератор безопасного пароля.

    Аргументы:
    level -- уровень сложности (1=легкий, 2=средний, 3=сложный)
    length -- длина пароля (минимум зависит от уровня сложности)

    Возвращает:
    Сгенерированный пароль (str)
    '''
    # Наборы символов
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-'

    # Комбинации по уровню сложности
    easy = lower + digits
    medium = lower + upper + digits
    hard = lower + upper + digits + symbols

    password = ''

    # Гарантируем наличие хотя бы одного символа каждого типа
    password += random.choice(lower)
    password += random.choice(digits)
    extra_chars = 2

    if level != 1:
        password += random.choice(upper)
        extra_chars += 1
        if level == 3:
            password += random.choice(symbols)
            extra_chars += 1

    # Остальные символы
    for _ in range(length - extra_chars):
        if level == 1:
            password += random.choice(easy)
        elif level == 2:
            password += random.choice(medium)
        else:
            password += random.choice(hard)

    # Перемешивание символов, чтобы не было одинаковых подряд
    while True:
        shuffled = ''.join(random.sample(password, len(password)))
        has_repeat = True

        for j in range(len(shuffled)-1):
            if shuffled[j] == shuffled[j+1]:
                has_repeat = False
                break

        if has_repeat:
            return shuffled