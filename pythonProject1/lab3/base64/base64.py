def encode_to_base64(input_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_data = ''.join(format(ord(c), '08b') for c in input_string)

    padding = (6 - len(binary_data) % 6) % 6
    binary_data += '0' * padding

    encoded = ''.join(base64_chars[int(binary_data[i:i+6], 2)] for i in range(0, len(binary_data), 6))

    encoded += '=' * ((4 - len(encoded) % 4) % 4)

    return encoded


def decode_from_base64(base64_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_string = base64_string.rstrip('=')

    binary_data = ''.join(format(base64_chars.index(c), '06b') for c in base64_string)

    byte_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ''.join(chr(int(byte, 2)) for byte in byte_chunks if len(byte) == 8)

    return decoded


original_text = "Example"
encoded_text = encode_to_base64(original_text)
print("Закодированный текст:", encoded_text)

decoded_text = decode_from_base64(encoded_text)
print("Декодированный текст:", decoded_text)
