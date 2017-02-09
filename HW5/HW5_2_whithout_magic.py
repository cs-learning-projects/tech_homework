class IntToStr(object):

    def __init__(self, value):
        self.value = value

    def sum_function(self, value, input_value):
        if type(input_value) == int:
            sum = value + input_value
        elif type(input_value) == str:
            if ord(input_value) > 110:
                sum = input_value + str(value)
            else:
                sum = str(value) + input_value
        else:
            raise TypeError('You can sum only integers and/or strings')
        return sum


n1 = IntToStr(9.2)
input_int1 = 3
print(n1.sum_function(n1.value, input_int1))

input_str1 = 'a'
print(n1.sum_function(n1.value, input_str1))

input_str2 = 'z'
print(n1.sum_function(n1.value, input_str2))

# input_list = [1, 2, 3]
# print(n1.sum_function(n1.value, input_list))


'''вариант2 функции sum_function - как исправить "During handling of the above
exception, another exception occurred:"

def sum_function(self, value, input_value):
        try:
            if type(input_value) == int:
                sum = value + input_value
            else:
                sum = str(value) + input_value
        except:
            raise TypeError('You can sum only integers and/or strings')
        return sum
'''

'''
Написать класс IntToStr, у которого есть одно поле: value. А тип поля - число.
Его задачей должно быть реализация возможности сложения чисел и строк. Примеры:
obj = IntToStr(9.2)
print(obj + 3)  # 12.2
print('a' + obj)  # a9.2
print(obj + 'z')  # 9.2z
'''
