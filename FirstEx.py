#create Category class with name,code and number of products
class category:
    def __init__(self,name,code,no_of_products):
        self.name=name
        self.code=code
        self.no_of_products=no_of_products
    def info_cat(self):
        print(self.name,self.code,self.no_of_products)
#create product class with name,code,category and price
class product:
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.category=category
        self.price=price
    def __repr__(self):
        return repr((self.name, self.code, self.category,self.price))
    def info(self):
        print(self.name,self.code,self.category,self.price)
#Create 3 different category
cat=[
    category("Tom",1111,5),
    category("Jerry",2222,55),
    category("Nobita",3333,40),
]
#Create 10 products
prods=[
       product("Laptop",101,"Electric",35000),
       product("Mobile",102,"Electric",15000),
       product("AC",103,"Electric",45000),
       product("Gold",104,"Metals",65000),
       product("Silver",105,"Metals",72000),
       product("Harmonium",106,"Toys",5000),
       product("Ball",107,"Toys",50),
       product("Cap",108,"Cloths",150),
       product("Mouse",109,"Accessories",200),
       product("Keyboard",110,"Accessories",500)
]
print("----------Category Info With Number Of Products----------")
for c in cat:
    print(c)
c.info_cat()
print("\n")
print("----------Sorted By Price From High To Low----------")
print("\n")
low_to_high=sorted(prods,key=lambda Products : Products.price,reverse=True)
for i in low_to_high:
    print(i)
print("\n")
print("----------Sorted By Price From Low To High----------")
print("\n")
high_to_low=sorted(prods,key=lambda Products : Products.price,reverse=False)
for i in high_to_low:
    print(i)
print("\n")
print("----------Search Product----------")
found_prod=[x for x in prods if x.code==103]
for x in found_prod:
    x.info()    
