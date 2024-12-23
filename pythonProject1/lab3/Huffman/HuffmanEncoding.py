from HuffmanDecoding import huffman_decoding


class Node: # Узел дерева
    def __init__(self, char, freq):
        self.char = char      # Символ (если узел является листом)
        self.freq = freq      # Частота символа (или сумма частот для внутренних узлов)
        self.left = None      # Левый дочерний узел (по пути '0')
        self.right = None     # Правый дочерний узел (по пути '1')


def build_huffman_tree(frequencies): # Построение дерева Хаффмана

    nodes = [Node(char, freq) for char, freq in frequencies.items()]  # Инициализируем список узлов для всех символов

    while len(nodes) > 1:  # Пока в списке больше одного узла, объединяем два с минимальной частотой

        nodes = sorted(nodes, key=lambda node: node.freq)  # Сортируем список узлов по частоте

        # Берем два узла с наименьшей частотой
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Создаем новый объединенный узел
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged) # Добавляем новый узел в список

    return nodes[0] # Корень дерева — последний оставшийся узел


def generate_codes(node, prefix="", codebook={}): # Генерация кодов Хаффмана

    if node.char is not None: # Если узел является листом (содержит символ)
        codebook[node.char] = prefix
        return

    # Рекурсивно идем влево и вправо
    generate_codes(node.left, prefix + "0", codebook) # Рекурсивно идем влево
    generate_codes(node.right, prefix + "1", codebook) # Рекурсивно идем вправо

    return codebook


def huffman_encoding(text): # Функция для кодирования строки

    frequencies = {} # Инициализация пустого словаря для частот символов

    # Подсчет частот символов
    for char in text:  # Проходим по каждому символу строки.
        if char not in frequencies:  # Если символ еще не встречался, добавляем его в словарь.
            frequencies[char] = 1  # Инициализируем его количество как 1.
        else:
            frequencies[char] += 1  # Если символ уже встречался, увеличиваем счетчик.

    root = build_huffman_tree(frequencies) # Построение дерева Хаффмана

    huffman_codes = generate_codes(root) # Генерация кодов

    encoded_text = ''.join([huffman_codes[char] for char in text]) # Кодирование текста

    return encoded_text, huffman_codes, root # Возвращаем закодированную строку и таблицу кодов

# Чтение фразы из файла

with open('text.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Пример использования
encoded_text, codes, root = huffman_encoding(data)
print(f"Закодированная строка: {encoded_text}") # Вывод закодированной строки
print(f"Таблица кодов Хаффмана: {codes}") # Вывод таблицы кодов
print(len(encoded_text)) # Вывод длины закодированной строки
print('-------------------------------------------')
print(huffman_decoding(encoded_text, root))
