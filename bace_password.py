def base_password(password: str) -> int:

    with open("common_passwords.txt", "r", encoding="utf-8") as file:
         common = file.read().splitlines()
    a = 1
    if password in common:
        a = 2

    return a