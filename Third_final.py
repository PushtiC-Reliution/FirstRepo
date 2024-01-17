class Product:
    def __init__(self, name, code, category, price, stock_at_locations):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        self.stock_at_locations = stock_at_locations

    def __str__(self):
        locations_str = [f"{location.name} ({location.code}): {quantity}" for location, quantity in self.stock_at_locations.items()]
        return f"Product name: {self.name}  Code: {self.code}  Category: {self.category}  Price: {self.price}  Stock at Locations: {locations_str}"

    def movement(self, from_location, to_location, quantity):
        try:
            if self.stock_at_locations[from_location] >= quantity:
                # Create a new movement instance
                new_movement = Movement(from_location, to_location, self, quantity)
                # Append the new movement to the 'movements_list'
                Movement.movements_list.append(new_movement)
               # Update product stock at locations
                self.stock_at_locations[from_location] -= quantity
                # Check if 'to_location' is present in 'stock_at_locations'
                if to_location in self.stock_at_locations:
                    # If present, update the stock quantity by adding the new quantity
                    self.stock_at_locations[to_location] += quantity
                else:
                    # If not present, initialize 'to_location' with the new quantity
                    self.stock_at_locations[to_location] = quantity

                print(f"Moved {quantity} items of {self.name} from {from_location.name} to {to_location.name}")
            else:
                # Raise an exception if there is insufficient stock at 'from_location'
                raise ValueError(f"stock is not avilable")
        except ValueError:
            raise ValueError(f"stock is not avilable")

    def display_details(self):
        print(f"Product Name: {self.name} ({self.code})")
        print(f"Category: {self.category}")
        print(f"Price: {self.price}")
        print(f"Stock at Locations: {self}")
        print()

    @classmethod
    def print_stock_information(self,location_list, product_list):
        for location in location_list:
            print(f"{location.name}:")
            location_products = [product for product in product_list if location in product.stock_at_locations]
            for product in location_products:
                print(f"  {product.name} ({product.code}): {product.stock_at_locations[location]}")
            print()


class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.name} {self.code}"


class Movement:
    movements_list = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        Movement.movements_list.append(self)

    def __str__(self):
        return f"{self.from_location}  {self.to_location}  {self.product}  {self.quantity}"

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in Movement.movements_list if movement.product == product]

    @classmethod
    def print_product_movements(self,product):
        for product in product_list:
            movements = set(Movement.movements_by_product(product))
            print(f"Product: {product.name} ({product.code})")
            for movement in movements:
                print(f" {movement}")
            print()


# Creating location object
loc1 = Location("Rajkot", 100)
loc2 = Location("Surat", 200)
loc3 = Location("Baroda", 300)
loc4 = Location("Ahm", 400)

# Creating product obj
prod1 = Product("Car", 1038,"electric", 500, {loc1: 10})
prod2 = Product("Bike", 1039,"electric", 600, {loc2: 80})
prod3 = Product("AC", 1040,"electric", 300, {loc3: 58})
prod4 = Product("Tv", 1041,"electric", 100, {loc4: 44})
prod5 = Product("laptop", 1042, "electric", 900, {loc1: 35})

product_list= [prod1,prod2,prod3,prod4]

location_list=[loc1,loc2,loc3,loc4]
#product details
print("Details")
for product in product_list:
    product.display_details()

# Moving products from one location to another
prod1.movement(loc1, loc2,1)
prod2.movement(loc2, loc3, 5)
prod3.movement(loc3, loc4, 15)
prod4.movement(loc4, loc1, 9)
prod5.movement(loc1, loc3, 8)

# Displaying movements of each product
print("Updated stock")
print()

Product.print_stock_information(location_list,product_list)
print("Movement details")
print()
Movement.print_product_movements(product)
