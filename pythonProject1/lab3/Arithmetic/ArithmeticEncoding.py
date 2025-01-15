from decimal import Decimal, getcontext
getcontext().prec = 50


class ArithmeticEncode:
    def __init__(self, data):
        self.data = data
        self.left = Decimal(0.0)
        self.right = Decimal(1.0)

    def define_alph(self):
        alphabet = {}
        for char in self.data:
            if char not in alphabet:
                alphabet[char] = 1
            else:
                alphabet[char] += 1
        return alphabet

    def define_frequency(self):
        frequencies = {}
        length = len(self.data)
        alphabet = self.define_alph()
        for letter, count in alphabet.items():
            frequencies[letter] = count / length
        return frequencies

    def define_additional_frequencies(self):
        additional_frequencies = {}
        cumulative_sum = 0.0
        freq_s = self.define_frequency()

        for letter, freq in freq_s.items():
            additional_frequencies[letter] = cumulative_sum
            cumulative_sum += freq

        return additional_frequencies

    def encode(self):
        freq_s = self.define_frequency()
        add_freqs = self.define_additional_frequencies()

        for char in self.data:
            add_left_freq = Decimal(add_freqs[char])
            add_right_freq = Decimal(add_left_freq) + Decimal(
                freq_s[char])

            current_range = self.right - self.left
            self.right = self.left + current_range * add_right_freq
            self.left = self.left + current_range * add_left_freq

        return (self.left + self.right) / 2


with open('text.txt', 'r', encoding='utf-8') as file:
    data = file.read()

code = ArithmeticEncode(data)
encoded_value = code.encode()
print(encoded_value)