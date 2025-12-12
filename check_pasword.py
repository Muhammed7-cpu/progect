def check_password(user_password: str) -> tuple[str, bool]:
    """
    Проверка надежности пароля и наличия повторяющихся символов.

    Аргументы:
        user_password (str): Пароль, который нужно проверить.

    Возвращает:
        tuple[str, bool]:
            - Надежность пароля как строка ("очень слабый", "слабый", "средний", "хороший", "очень хороший")
            - Строка "есть" или "нет", указывающая, есть ли повторяющиеся символы подряд
    """
    length = len(user_password)
    symbols = '!@#$%^&*()_+-'  # Специальные символы, учитываемые при проверке

    # Проверка наличия различных типов символов
    has_lower = any(c.islower() for c in user_password)
    has_upper = any(c.isupper() for c in user_password)
    has_digit = any(c.isdigit() for c in user_password)
    has_symbol = any(c in symbols for c in user_password)

    # Проверка наличия повторяющихся символов подряд
    has_repeat = any(user_password[i] == user_password[i - 1] for i in range(1, length))
    repeat_status = "есть" if has_repeat else "нет"

    # Определяем размер используемого набора символов
    charset_size = 0
    if has_lower: charset_size += 26
    if has_upper: charset_size += 26
    if has_digit: charset_size += 10
    if has_symbol: charset_size += len(symbols)

    # Вычисление количества возможных комбинаций пароля
    combinations = charset_size ** length

    # Приблизительное время взлома пароля в секундах (скорость 10_000_000 попыток в секунду)
    time_to_crack_sec = combinations / 10_000_000

    # Определение уровня надежности на основе времени взлома
    if time_to_crack_sec < 1:
        strength = "очень слабый"
    elif time_to_crack_sec < 60:
        strength = "слабый"
    elif time_to_crack_sec < 3600:
        strength = "средний"
    elif time_to_crack_sec < 86400:
        strength = "хороший"
    else:
        strength = "очень хороший"

    return strength, repeat_status
