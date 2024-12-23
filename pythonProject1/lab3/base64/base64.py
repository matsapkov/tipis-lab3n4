# Простейшая реализация кодирования и декодирования Base64

def encode_to_base64(input_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_data = ''.join(format(ord(c), '08b') for c in input_string)  # Двоичное представление строки

    # Дополняем до кратности 6 битам
    padding = (6 - len(binary_data) % 6) % 6
    binary_data += '0' * padding

    # Группируем по 6 бит и преобразуем в символы Base64
    encoded = ''.join(base64_chars[int(binary_data[i:i+6], 2)] for i in range(0, len(binary_data), 6))

    # Добавляем '=' для выравнивания длины до кратности 4
    encoded += '=' * ((4 - len(encoded) % 4) % 4)

    return encoded

def decode_from_base64(base64_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_string = base64_string.rstrip('=')  # Удаляем выравнивающие символы '='

    # Преобразуем символы Base64 в двоичное представление
    binary_data = ''.join(format(base64_chars.index(c), '06b') for c in base64_string)

    # Группируем по 8 бит (1 байт) и преобразуем в символы
    byte_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ''.join(chr(int(byte, 2)) for byte in byte_chunks if len(byte) == 8)

    return decoded

# Пример использования
original_text = "Example"
encoded_text = encode_to_base64(original_text)
print("Закодированный текст:", encoded_text)

decoded_text = decode_from_base64(encoded_text)
print("Декодированный текст:", decoded_text)
