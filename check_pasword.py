def check_password(user_password: str) -> tuple[str, bool]:
    '''
    Проверка надежности пароля.

    Аргументы:
    user_password -- пароль пользователя

    Возвращает:
    tuple:
        str -- оценка надежности ("очень слабый" … "очень хороший")
        bool -- True, если есть повторяющиеся символы подряд
    '''
    length = len(user_password)

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-'

    has_lower = has_upper = has_digit = has_symbol = False

    for char in user_password:
        if char in lower:
            has_lower = True
        elif char in upper:
            has_upper = True
        elif char in digits:
            has_digit = True
        elif char in symbols:
            has_symbol = True

    # Проверка повторяющихся символов подряд
    has_repeat = 'нет'
    for i in range(length):
        if user_password[i] in user_password[i - 1]:
            has_repeat = 'есть'

    # Количество возможных символов
    charset_size = 0
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_symbol:
        charset_size += len(symbols)

    combinations = charset_size ** length
    time_to_crack_sec = combinations / 10000000  # примерное время взлома

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

    return strength, has_repeat
