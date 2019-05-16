
		
class Coffee(object):
	def __init__(self):
		self.prepare(self)
		
	def prepare():
		print('Heat water')


class CoffeeMachine(object): 
	def make_coffee(self, coffee_name):
		if coffee_name == 'Espresso': return Espresso()
		if coffee_name == 'Latte':    return Latte()
		assert 0, "Bad shape creation: " + type


class Espresso(Coffee):
	def __init__(self):
		self.prepare()
		
	def prepare(self):
		Coffee.prepare()
		print('Pressurize water')
		print('Compact coffee powder inside capsule')
		print('Place small cup on holder')
		print('Jet hot water throught capsule grid to cup')


class Latte(Coffee):
	def __init__(self):
		self.prepare()
		
	def prepare(self):
		Coffee.prepare()
		print('Heat milk')
		print('Put coffee powder inside filter')
		print('Place big cup on holder')
		print('Brew hot water throught filter to cup')
		print('Pour hot milk into cup')
		
		
coffeeMachine = CoffeeMachine()
coffee1 = coffeeMachine.make_coffee('Espresso')
print()
coffee2 = coffeeMachine.make_coffee('Latte')