def encoder(text, key) -> str:
    encrypted = []
    for char in text:
        encrypted_code = ord(char) ^ key
        encrypted.append(f"{encrypted_code:02x}")
    return "".join(encrypted)

def decoder(encoded_hex, key) -> str:
    decrypted = []
    for i in range(0, len(encoded_hex), 2):
        byte = int(encoded_hex[i:i+2], 16)
        decrypted.append(chr(byte ^ key))
    return "".join(decrypted)