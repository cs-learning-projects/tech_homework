#1. ------------------------------------------------------------------------------------------------------------------------
# Написать функцию, которая выбрасывает одно из трех исключений:ValueError, 
# TypeError или RuntimeError случайным образом. В месте вызова функции обрабатывать все три исключения

# TypeError: This is TypeError??? и как с этим бороться?

# вариант 1
def raise_exception():
	random_exception = random.choice(['value', 'type', 'runtime'])
	if random_exception == 'value':
		raise ValueError('This is ValueError')
	elif random_exception == 'type':
		raise TypeError('This is TypeError')
	else:
		raise RuntimeError('This is RuntimeError')


raise_exception()

# вариант 2
import random 
exception_list = [ValueError, TypeError, RuntimeError]

print(random.choice(exception_list))

#2. ------------------------------------------------------------------------------------------------------------------------
#Написать функцию, которая принимает на вход список, 
#если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError

#не получается сделать с ValueError, т.к. ValueError raised when a built-in 
# operation or function receives an argument that has the right type but an inappropriate value.
# а тут нам не важно value, но если тип не int, то должно срабатывать исключение.
# Или я что-то не поняла...?

# вариант 1
def sort_function(*args):
    try:        
        print(sorted(args))
    except TypeError: 
        print('Non-numeric data found in the list.')

       
sort_function(10, 5, 3, 'str')
sort_function(10, 5, 3)

# вариант 2
def sort_function(*args):
    try:        
        print(sorted(args))
    except TypeError: 
        raise ValueError('Non-numeric data found in the list.')

       
sort_function(10, 5, 3, 'str')
sort_function(10, 5, 3)
#3. ------------------------------------------------------------------------------------------------------------------------
# Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь

# вариант 1

def key_to_string(my_dict):    
    output_dict = {}
    for key,value in my_dict.items():
        output_dict.update({str(key): value})
    return output_dict

input_dict = {'key1': 1, 2: 'two'}
print(key_to_string(input_dict))

# вариант 2
# переводит все str ключи в int ключи. Как все-таки передать ключ в виде int

def key_to_string2(**kwargs):
	output_dict = {}
	for key, value in kwargs.items():
	    output_dict[int(key)] = value
	return output_dict

input_dict2 = {'1': 'one', '2': 'two'}
print(key_to_string2(**input_dict2))

# 4. ------------------------------------------------------------------------------------------------------------------------
# Написать функцию, которая принимает список чисел и возвращает их произведение

def multiplication(*args):
    result = 1
    for item in args:
        result = result * item
    return result
    
print(multiplication(1, 5, 10))


# 5. ------------------------------------------------------------------------------------------------------------------------
# Написать три функции: do_work, handle_success, handle_error. do_word(my_list, success_callback, error_callback) 
# принимает на вход три аргумента: список, функцию для обработки успеха и функцию для обработки ошибки. 
# Ее задача проверить, что все значения в списке идут по-возрастанию. Если все верно: вызываем success_callback, 
# иначе: error_callback. Функция handle_success пишет в консоль информацию об успешном выполнении. 
# Функция handle_error выбрасывает ValueError

def do_work(my_list, success_callback, error_callback):
	if my_list == sorted(my_list):
	   return handle_success()
	else:
	   return handle_error()

def handle_success():
    print("Working fine, list is sorted!")

def handle_error():
    raise ValueError("List wast sorted.")

list1 = [1, 5, 7, 9]
print(do_work(list1, handle_success, handle_error))
# выдает TypeError: '<' not supported between instances of 'str' and 'int'
# почему не срабатывает else в данном случае??
list2 = [1, 5, 7, 9, 'str']
print(do_work(list2, handle_success, handle_error))
