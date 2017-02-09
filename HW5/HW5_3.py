class Stack(object):

    def __init__(self):
        self.list = []

    def push_method(self, value):
        self.list.append(value)

    def pop_method(self):
        if self.list == []:
            raise IndexError('The stack is empty!')
        else:
            stack_index = len(self.list) - 1
            self.list.pop(stack_index)


# данные для проверки работы программы:
object1 = Stack()
object1.push_method(3)
object1.push_method('five')
object1.push_method(5)
object1.push_method('six')

print(object1.list)
object1.pop_method()
print(object1.list)

object2 = Stack()
print(object2.list)
object2.pop_method()
print(object2.list)


'''
Написать класс Stack, у которого есть два метода push(value) и pop(). Если мы
пытаемся сделать pop из пустого стека, нужно выбрасывать исключение
IndexError. Подробнее про стек: https://ru.wikipedia.org/wiki/LIFO
'''
