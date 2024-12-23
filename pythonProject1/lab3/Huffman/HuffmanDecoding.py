def huffman_decoding(encoded_text, root):
    """
    Функция для декодирования строки, закодированной с помощью Хаффмана.

    :param encoded_text: Закодированная строка (битовая последовательность).
    :param root: Корень дерева Хаффмана.
    :return: Декодированная строка.
    """
    decoded_text = []  # Результирующая строка
    current_node = root  # Начинаем с корня дерева

    for bit in encoded_text:  # Проходим по каждому биту в закодированной строке
        if bit == '0':  # Если бит — 0, движемся влево
            current_node = current_node.left
        elif bit == '1':  # Если бит — 1, движемся вправо
            current_node = current_node.right

        # Если достигли листового узла
        if current_node.char is not None:
            decoded_text.append(current_node.char)  # Добавляем символ в результат
            current_node = root  # Возвращаемся в корень дерева для следующего символа

    return ''.join(decoded_text)  # Объединяем символы в строку
