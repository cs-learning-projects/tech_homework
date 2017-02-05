#_1 1.
# Реализовать класс Person, у которого должно быть два публичных поля: age и name. 
# Также у него должен быть следующий набор методов: know(person), который позволяет д
# обавить другого человека в список знакомых. И метод is_known(person), который возвращает знает ли знакомы ли два человека

class Person(object):
	

	def __init__(self, age, name, friend_list=None):
		self.age = age
		self.name = name
		self.friend_list = []
		
			
	def know(self, person, friend_list):
		self.friend_list.append(person)
		return friend_list
		

	def is_known(self, person, friend_list):
		for item in friend_list:
			if person == item:
				print(item, ' is friend of ', person)
			else:
				print(item, ' and ', person, ' isnt friends')
			return


p1 = Person(20, 'Mike')
p2 = Person(18, 'Mary')
p3 = Person(19, 'Bill')
p4 = Person(25, 'Helen')
p5 = Person(21, 'John')

#print(p1.age, p1.name)
#print(p2.age, p2.name)
#print(p3.age, p3.name)

print(p1.know(p2.name, p1.friend_list))
print(p1.know(p3.name, p1.friend_list))
p1.is_known(p2.name, p1.friend_list)
p1.is_known(p4.name, p1.friend_list)

