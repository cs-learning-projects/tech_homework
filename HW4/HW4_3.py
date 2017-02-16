# 3.
# Написать класс Animal и Human, сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые). 
# Другие - нет. За что будет отвечать метод is_dangerous(animal)


class Human(object):
	def __init__(self, name):
		self.name = name
		

class Animal(object):
	dangerous_animal = True
	def __init__(self, name):
		self.name = name
	def is_dangerous(self, dangerous):
		if self.dangerous_animal == True:
			print(self.name, 'is dangerous animal')
		else:
			print(self.name, 'is not dangerous animal')
		return


class Lion(Animal):
	pass

class Scorpion(Animal):
	pass

class Mosquito(Animal):
	dangerous_animal = False

lion1 = Lion('lion1')
#print(lion1.name)
#print(lion1.dangerous_animal)
lion1.is_dangerous(lion1.dangerous_animal)

mosquito1 = Mosquito('mosquito1')
mosquito1.is_dangerous(mosquito1.dangerous_animal)

