class IntToStr(object):

    def __init__(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('You can sum only integers and/or strings')
        self.value = value

    def __add__(self, value):
        if isinstance(value, str):
            return str(self.value) + value
        else:
            return self.value + value

    def __radd__(self, value):
        if isinstance(value, str):
            return value + str(self.value)
        else:
            return value + self.value

n1 = IntToStr(9.2)
print(n1 + 3)
print('a' + n1)
print(n1 + 'z')

# n2 = IntToStr([1, 2, 3])
