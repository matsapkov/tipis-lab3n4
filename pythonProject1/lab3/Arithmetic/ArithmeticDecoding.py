from decimal import Decimal, getcontext
from pythonProject1.lab3.Arithmetic.ArithmeticEncoding import ArithmeticEncode  # Импортируем класс ArithmeticEncode для кодирования строки.
getcontext().prec = 350  # Устанавливаем точность вычислений для Decimal на 350 знаков.


class ArithmeticDecode:
    def __init__(self, value, end_symbol, frequencies):
        self.encoded_value = value  # Сохраняем закодированное значение, которое нужно декодировать.
        self.end_symbol = end_symbol  # Длина исходной строки.
        self.frequencies = frequencies  # Частоты символов (как словарь).
        self.right = Decimal(1.0)  # Начальная правая граница интервала для декодирования.
        self.left = Decimal(0.0)  # Начальная левая граница интервала для декодирования.

    def define_additional_frequencies(self):
        additional_frequencies = {}  # Создаем пустой словарь для хранения накопительных вероятностей.
        cumulative_sum = 0.0  # Инициализируем накопленную сумму как 0.
        freq_s = self.frequencies  # Получаем словарь частот символов.

        for letter, freq in freq_s.items():  # Проходим по каждому символу и его частоте.
            additional_frequencies[letter] = cumulative_sum  # Присваиваем текущую накопленную сумму.
            cumulative_sum += freq  # Обновляем накопленную сумму, добавляя текущую частоту.

        return additional_frequencies  # Возвращаем словарь с накопительными вероятностями для символов.

    def decode(self):
        encoded_word = ''  # Строка, в которую будем записывать декодированные символы.
        add_frequencies = self.define_additional_frequencies()  # Получаем накопительные вероятности символов.
        freq_s = self.frequencies  # Получаем частоты символов.

        while True:
            current_range = Decimal(self.right) - Decimal(self.left) # Вычисляем текущий диапазон интервала.
            scaled_value = (self.encoded_value - self.left) / current_range  # Масштабируем закодированное значение в текущем интервале.
            for char, add_left_freq in add_frequencies.items():  # Проходим по символам и их накопительным вероятностям.

                add_right_freq = Decimal(add_left_freq) + Decimal(freq_s[char])  # Вычисляем правую границу для символа.

                # Если масштабированное значение попадает в интервал между левой и правой границами:
                if add_left_freq <= scaled_value < add_right_freq:
                    if char == self.end_symbol:
                        return encoded_word  # Возвращаем полностью декодированную строку.
                    else:
                        encoded_word += char  # Добавляем символ к декодированной строке.
                        # Обновляем левую и правую границы интервала для следующей итерации:
                        self.right = self.left + current_range * add_right_freq
                        self.left = self.left + current_range * Decimal(add_left_freq)


# Чтение фразы из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    data = file.read()


code = ArithmeticEncode(data)  # Создаем объект для кодирования с входной строкой.
print(f'Закодированное значение {code.encode()}')  # Кодируем строку и выводим закодированное значение.
decode = ArithmeticDecode(code.encode(), '☺', code.define_frequency())  # Создаем объект для декодирования, передаем закодированное значение, длину строки и частоты символов.
print(f'Раскодированное значение {decode.decode()}')  # Декодируем строку и выводим результат.