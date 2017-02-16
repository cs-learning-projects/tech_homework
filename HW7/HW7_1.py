# 1
''' Прочитать теорию (ссылки в материалах) о работе с файлами в python. 
И реализовать две функции: write_to_file(data) и read_file_data(). Которые 
соотвественно: пишут данные в файл и читают данные из файла.
'''
def write_to_file(data):
	input_file = open('HW7_text_file.txt', 'a')
	input_file.write(data)
	input_file.close()
	

def read_file_data(file_to_read):
	contents_of_file = open('file_to_read', 'r')
	print(contents_of_file.read())

write_to_file('add some text to the file \n')
write_to_file('add some additional text to the file \n')

read_file_data('/Users/nepogoda/tceh_homeworks/HW7_text_file.txt')
'''
FileNotFoundError: [Errno 2] No such file or directory: 'file_to_read'
Как сделать, чтобы файл был найден? Как правильно написать путь к этому
файлу, чтобы он находился? Как указано не работает
'''