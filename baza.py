import sys

from generate import generate
from check_pasword import check_password
from bace_password import base_password

a = int(input("генератор пороля : 1 \nпроверка проля:2 \n(1/2):"))

if a not in (1,2) :
    print("не правильный ввод автоматически переходим в (hard)")
    level = 3
if a == 1:
    print("=== УМНЫЙ ГЕНЕРАТОР ПАРОЛЕЙ ===")
    level = int(input("Ввыберите сложность (1-easy, 2-medium, 3-hard):" ))
    len_password = int(input("введите длинну пороля:"))
    password_gen = generate(level, len_password)
    print("\n=====================================")
    print(f"содержит {len_password} символов\n"
          f"Сложность: {level}\n"
          f"Ваш пороль: {password_gen}")

if a == 2:
    print("=== ПРОВЕРЬ СВОЙ ПАРОЛЬ ===")
    user_pas = input("Введи свой пароль:")
    bace = base_password(user_pas)
    if bace == 2:
        print(f"Пароль есть в базе:{user_pas} он не надежный")
        sys.exit(0)
    password , repeat = check_password (user_pas)
    print(f"\n=== Проверка пароля ==="
          f"\nДлина: {len(user_pas)}"
          f"\nЕсть ли повторяюшие элементы:{repeat}"
          f"\nНадежность пароля: {password}")
