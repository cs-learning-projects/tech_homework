# 2
'''
Прочитать теорию о работе с json. Реализовать следующую логику: 
получать при помощи requests данные сайта 
https://jsonplaceholder.typicode.com/, выводить в консоль все 
пары "ключ-значение", сохранять полученный json в файл.
'''
import json
import requests

my_request = requests.get('https://jsonplaceholder.typicode.com/')
my_request_dict = my_request.headers
for key, value in my_request_dict.items():
	print(key, value)
output_file = open('output.txt', 'a')
# output_file.write(json.dumps(my_request_dict))
# TypeError: Object of type 'CaseInsensitiveDict' is not JSON serializable
# https://github.com/kennethreitz/requests/issues/1380
output_file.write(json.dumps(dict(my_request_dict)))
output_file.close()
# вроде как все работает, но output.txt пустой при этом??? 

