def base_password(password: str) -> int:
    '''
    Проверка, есть ли пароль в базе популярных паролей.

    Аргументы:
    password -- пароль пользователя

    Возвращает:
    2 -- если пароль найден в базе (не надежный)
    1 -- если пароль не найден
    '''

    # Читаем файл со списком популярных паролей
    with open("common_passwords.txt", "r", encoding="utf-8") as file:
        common = file.read().splitlines()

    a = 1  # по умолчанию считаем пароль надёжным

    '''
    Если пароль есть в базе — считаем его слабым
    '''
    if password in common:
        a = 2

    return a
