import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		current = self.items[0]
		for item in self.items:
			if item.stock > current.stock:
				current = item
		return current
		

		pass
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		
		current = self.items[0]
		for item in self.items:
			if item.price > current.price:
				print(item.price)
				current = item
		return current



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)
		self.w1 = Warehouse()
	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a('aaaaa'), 5, "testing count a" )
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):

		self.assertEqual(self.w1.items,[],"testing add item before")
		self.w1.add_item(self.item1)
		self.assertEqual(self.w1.items,[self.item1],"testing add item before")
		
		pass


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.assertEqual(self.w1.items,[],"testing add item before")
		self.w1.add_item(self.item1)
		self.assertEqual(self.w1.items,[self.item1],"testing add item before")
		self.w1.add_item(self.item2)
		self.assertEqual(self.w1.items,[self.item1,self.item2],"testing add item before")
		self.w1.add_item(self.item3)
		self.assertEqual(self.w1.items,[self.item1,self.item2,self.item3],"testing add item before")

		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.w1.add_item(self.item1)
		self.w1.add_item(self.item2)
		self.w1.add_item(self.item3)
		self.w1.get_max_price()
		self.assertEqual(self.w1.get_max_price(),self.item1,"testing that item1 is returned")

		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()