#Name: Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double(self):
            self.cost *= (2)
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
chocolate = Store(20, 5.47, 1)
popsicle = Store(25, 3.47, 1)
bananas= Store(20, 4.47, 2)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"The cost of Ramen is: {chocolate.cost}")
print(f"The cost of Rice is: {popsicle.cost}")
print(f"The cost of Beans is: {bananas.cost}")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
popsicle.double()
print("The doubled cost of item is:", popsicle.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
bananas.stock = 5
print("The new stock number of beans is:", bananas.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del chocolate

try:
    print(chocolate.weight)

except:
    print("Item not found")