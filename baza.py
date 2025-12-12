import sys

from generate import generate
from check_pasword import check_password
from bace_password import base_password
from encoder import encoder,decoder

def main():
    try:
        # Выбор режима работы программы
        mode = int(input("генератор пороля : 1 \nпроверка пороля: 2 \nшифратор/дешифратор: 3 \n(1/2/3): "))
    except ValueError:
        print("не правильный ввод автоматически переходим в генерацию пороля")
        mode = 1

    if mode == 1:
        # Режим генерации пароля
        print("=== УМНЫЙ ГЕНЕРАТОР ПАРОЛЕЙ ===")

        try:
            # Выбор сложности пароля
            level = int(input("Выберите сложность (1-easy, 2-medium, 3-hard): "))
            if level not in (1, 2, 3):
                print("не правильный ввод — выбран уровень hard")
                level = 3
        except ValueError:
            print("не правильный ввод — выбран уровень hard")
            level = 3

        try:
            # Ввод длины пароля и проверка минимальной длины
            length = int(input("Введите длину пароля: "))
            min_len = {1: 8, 2: 10, 3: 12}[level]
            if length < min_len:
                print(f"Слишком короткий пароль → автоматически {min_len}")
                length = min_len
        except ValueError:
            print("некорректный ввод → длина установлена 12")
            length = 12

        # Генерация пароля
        password, lenght = generate(level, length)
        text_level = {1: "easy", 2: "medium", 3: "hard"}[level]

        # Вывод информации о сгенерированном пароле
        print("\n=====================================")
        print(f"Длина: {length} символов")
        print(f"Сложность: {text_level}")
        print(f"Ваш пароль: {password}")

    elif mode == 2:
        # Режим проверки пароля
        print("=== ПРОВЕРЬ СВОЙ ПАРОЛЬ ===")
        user_pas = input("Введите пароль: ")

        # Проверка пароля по базе известных слабых паролей
        if base_password(user_pas) == 2:
            print(f"Пароль найден в базе: {user_pas}. Он небезопасный.")
            sys.exit(0)

        # Проверка надежности пароля и повторяющихся символов
        strength, repeated = check_password(user_pas)

        # Вывод результатов проверки
        print("\n=== Проверка пароля ===")
        print(f"Длина: {len(user_pas)}")
        print(f"Есть повторяющиеся символы: {repeated}")
        print(f"Надежность пароля: {strength}")
    elif mode == 3:
        try:
            a = int(input("1)шифровать/2)дешифровать"))
            if a not in (1, 2):
                print("некоректный ввод автоматически шифруем")
                a = 1
        except ValueError:
            print("некоректный ввод автоматически шифруем")
            a = 1

        user_pas_encoder = input("введите свой пороль:")
        keys = input("введите ключ для шифрации:")
        if a == 1:
            cipher_pas = encoder(user_pas_encoder, keys)
        if a == 2:
            cipher_pas = decoder(user_pas_encoder, keys)
        print(f"пороль:{cipher_pas}\n"
              f"ключь: {keys}")
if __name__ == "__main__":
    main()
