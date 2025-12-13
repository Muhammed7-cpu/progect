def encoder(text = str, key = int ) -> str:
    """
    Шифрует строку с использованием операции XOR и возвращает результат в виде hex.

    Parameters
    ----------
    text : str
        Исходная строка, которую нужно зашифровать.
    key : int
        Целочисленный ключ для XOR-операции. Должен быть в диапазоне 0–255.
    """
    encrypted = []
    for char in text:
        encrypted_code = ord(char) ^ key
        encrypted.append(f"{encrypted_code:02x}")
    return "".join(encrypted)


def decoder(encoded_hex = str , key = int ) -> str:
    """
    Дешифрует hex-строку, зашифрованную функцией encoder, используя тот же XOR-ключ.

    Parameters
    ----------
    encoded_hex : str
        Строка hex-значений, где каждые два символа представляют один байт.
    key : int
        XOR-ключ, использованный при шифровании. Должен совпадать с ключом encoder.
    """
    decrypted = []
    for i in range(0, len(encoded_hex), 2):
        byte = int(encoded_hex[i:i+2], 16)
        decrypted.append(chr(byte ^ key))
    return "".join(decrypted)
