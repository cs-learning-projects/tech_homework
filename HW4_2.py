
# 2.
# Есть класс, который выводит информацию в консоль: `Printer`, у него есть метод: log(*values). 
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Printer(object):
	text_to_print = 'some text' 
	#text_to_print = input('Please input your text: ')

	def log(self, *text_to_print):
		print_str = print(self.text_to_print)
		return 

class FormattedPrinter(Printer):


	def log_with_stars(self, *text_to_print):
		str_len = len(self.text_to_print)
		star_str = '*' * (str_len + 4)
		print(star_str)
		print('*', self.text_to_print, '*')
		print(star_str)
		return


text1 = Printer()
text1.log(text1.text_to_print)

print('\n')

text2 = FormattedPrinter()
text2.log_with_stars(text2.text_to_print)

