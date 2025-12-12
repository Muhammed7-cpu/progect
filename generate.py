import secrets
import string

# Специальные символы, используемые для сложного пароля
SPECIAL_CHARS = "!@#$%^&*()_+-"

def generate(level: int, length: int) -> tuple[str, int]:
    """
    Генерация случайного пароля заданной сложности и длины.

    Аргументы:
        level (int): Уровень сложности пароля:
                     1 - easy (только строчные буквы)
                     2 - medium (строчные + заглавные буквы + цифры)
                     3 - hard (medium + специальные символы)
        length (int): Длина пароля (количество символов)

    Возвращает:
        tuple[str, int]: Сгенерированный пароль и его длину
    """
    # Наборы символов для разных уровней сложности
    chars_easy = string.ascii_lowercase
    chars_medium = string.ascii_lowercase + string.ascii_uppercase + string.digits
    chars_hard = chars_medium + SPECIAL_CHARS

    # Выбор набора символов в зависимости от уровня
    if level == 1:
        chars = chars_easy
    elif level == 2:
        chars = chars_medium
    else:
        chars = chars_hard

    # Генерация пароля случайным образом
    password = [secrets.choice(chars) for _ in range(length)]

    # Гарантируем наличие хотя бы одной заглавной буквы для medium и hard
    if level >= 2 and not any(c.isupper() for c in password):
        password[secrets.randbelow(length)] = secrets.choice(string.ascii_uppercase)

    # Гарантируем наличие хотя бы одного специального символа для hard
    if level == 3 and not any(c in SPECIAL_CHARS for c in password):
        password[secrets.randbelow(length)] = secrets.choice(SPECIAL_CHARS)

    # Перемешивание пароля для дополнительной случайности
    secrets.SystemRandom().shuffle(password)

    return "".join(password), length
