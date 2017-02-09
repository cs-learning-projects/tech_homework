import random

'''
Написать списковые выражения, которые:
a. создают список из строк всех нечетных чисел от 1 до 100
b. создают список из объектов другого списка, кроме итерируемых
c. создают список из фразы 'The quick brown fox jumps over the lazy dog',
где каждый объект списка - кортеж из: слова в верхнем регистре, слова
в случанйном регистре (qUIcK) и длины слова
'''

odd_numbers = [str(x) for x in range(1, 100, 2)]
print(odd_numbers)


input_list = [123, 'abc', [0, 1, 2], ('a', 'b'), 456]
not_iter_items = [x for x in input_list if not hasattr(x, '__iter__')]
print(not_iter_items)

phrase = 'The quick brown fox jumps over the lazy dog'
formatted_phrase = [(x.upper(), ''.join([random.choice([y.upper(), y.lower()])
                    for y in x]), len(x)) for x in phrase.split()]
print(formatted_phrase)
