from decimal import Decimal, getcontext
getcontext().prec = 50  # Устанавливаем точность Decimal до 500 знаков после запятой для точных вычислений с плавающей запятой.


class ArithmeticEncode:
    def __init__(self, data):
        self.data = data  # Сохраняем входные данные (строку, которую нужно закодировать).
        self.left = Decimal(0.0)  # Начальное значение левой границы интервала.
        self.right = Decimal(1.0)  # Начальное значение правой границы интервала.

    def define_alph(self):
        '''
        Функция для формирования алфавита (словаря) фразы и подсчета количества использований каждого символа.
        '''
        alphabet = {}  # Создаем пустой словарь для хранения символов и их частот.
        for char in self.data:  # Проходим по каждому символу строки.
            if char not in alphabet:  # Если символ еще не встречался, добавляем его в словарь.
                alphabet[char] = 1  # Инициализируем его количество как 1.
            else:
                alphabet[char] += 1  # Если символ уже встречался, увеличиваем счетчик.
        return alphabet  # Возвращаем словарь, содержащий частоту каждого символа.

    def define_frequency(self):
        '''
        Функция для формирования словаря, содержащего частоту каждого символа.
        '''
        frequencies = {}  # Создаем пустой словарь для хранения частот символов.
        length = len(self.data)  # Получаем длину строки для вычисления относительных частот.
        alphabet = self.define_alph()  # Получаем алфавит с частотой каждого символа.
        for letter, count in alphabet.items():  # Проходим по символам и их количествам.
            frequencies[letter] = count / length  # Рассчитываем частоту как количество / общая длина строки.
        return frequencies  # Возвращаем словарь с частотами символов.

    def define_additional_frequencies(self):
        '''
        Функция для вычисления накопительных вероятностей для каждого символа.
        '''
        additional_frequencies = {}  # Создаем пустой словарь для хранения накопительных вероятностей.
        cumulative_sum = 0.0  # Инициализируем начальную накопительную сумму как 0.
        freq_s = self.define_frequency()  # Получаем частоты символов.

        for letter, freq in freq_s.items():  # Проходим по каждому символу и его частоте.
            additional_frequencies[letter] = cumulative_sum  # Назначаем текущую накопленную вероятность.
            cumulative_sum += freq  # Обновляем накопленную сумму, добавляя текущую частоту.

        return additional_frequencies  # Возвращаем словарь с накопительными вероятностями для каждого символа.

    def encode(self):
        freq_s = self.define_frequency()  # Получаем частоты символов.
        add_freqs = self.define_additional_frequencies()  # Получаем накопительные вероятности.

        for char in self.data:  # Проходим по каждому символу строки.
            add_left_freq = Decimal(add_freqs[char])  # Получаем накопленную вероятность для символа (левая граница).
            add_right_freq = Decimal(add_left_freq) + Decimal(
                freq_s[char])  # Вычисляем правую границу (накопленная + частота).

            current_range = self.right - self.left  # Вычисляем текущий диапазон (разницу между правой и левой границами).
            self.right = self.left + current_range * add_right_freq  # Обновляем правую границу интервала.
            self.left = self.left + current_range * add_left_freq  # Обновляем левую границу интервала.

        return (self.left + self.right) / 2  # Возвращаем среднее значение между левой и правой границами как результат кодирования.

# Чтение фразы из файла
with open('../text.txt', 'r', encoding='utf-8') as file:
    data = file.read()

code = ArithmeticEncode(data)
encoded_value = code.encode()
print(encoded_value)