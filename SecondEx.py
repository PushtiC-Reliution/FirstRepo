# new data members “parent”, “display_name”, and “products” (list of product objects)
class category:

    def __init__(self,name,code,parent=None):
        self.name=name
        self.code=code
        self.parent=parent        
        self.product_count = 0  # Initialize product count to 0
        self.display_name=self.generate_display_name()
        self.product=[]

    def __str__(self):
        return f"Category Name: {self.name} , Code: {self.code} ,Number of Products : {self.product_count} , Display Name : {self.display_name}"
        
    def generate_display_name(self):
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.display_name} > {self.name}"
    @staticmethod
    def display_details():
        for c in cat_list:
            print(f"Category Code: {c.code} , Category Name : {c.name}")
            print(f"Display Name: {c.display_name}")
            print(f"No. of products: {c.product_count}")
            print()
            for p in prod_list:
                    if p.category.name==c.name:
                        print(f"  name:  {p.name}  code:  {p.code}  price:  {p.price} ")
            print()
   
    def add_prod(self,product):
        self.product.append(product)      
    
#create product class with name,code,category and price
class product:
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.price=price
        self.category=category
        category.product_count += 1
    def sorting_by_category_name(prod_list):

        n=len(prod_list)
        
        for i in range(n-1):
            for j in range(n-1):
                if prod_list[j].name>prod_list[j+1].name:
                    prod_list[j],prod_list[j+1]=prod_list[j+1],prod_list[j]
            
        for pro in prod_list:
            print(f"Name:  {pro.name}     Code:  {pro.code}    Category:  {pro.category}    price:    {pro.price}")
            print()

#Create different category

vehicle=category("vehicle",6666)
car=category("Car",7777,parent=vehicle)
petrol=category("petrol",5555,parent=car)
cloth=category("cloth",8888)
tsrt=category("T-shirt",9999,parent=cloth)

#product objects for each category

sedan=product("Sedan", "S001", vehicle, 25000)
suv=product("SUV", "S002", vehicle, 35000)
motorcycle=product("Motorcycle", "M003", vehicle, 12000)

regular=product("Regular Petrol", "R007", petrol, 3.5)
premium=product("Premium Petrol", "P008", petrol, 4.0)
super=product("Super Petrol", "S009", petrol, 4.5)

compact=product("Compact Car", "C004", car, 18000)
sedan_car=product("Sedan Car", "S005", car, 22000)
electric=product("Electric Car", "E006", car, 30000)

tshirt=product("T-shirt", "T010", cloth, 15)
dress=product("Dress Shirt", "D011", cloth, 25)
jeans=product("Jeans", "J012", cloth,40)

casual=product("Casual Shirt", "C013", tsrt, 30)
formal=product("Formal Shirt", "F014",tsrt, 35)
printed=product("Printed Shirt","P015",tsrt,28)

print("\n")

cat_list=[vehicle,petrol,car,cloth,tsrt]

prod_list=[sedan,suv,motorcycle,regular,premium,super,compact,sedan_car,electric,tshirt,dress,jeans,casual,formal,printed]

category.display_details()
product.sorting_by_category_name(prod_list)

