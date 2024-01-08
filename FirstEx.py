#create Category class with name,code and number of products
class category:
    
    def __init__(self,name,code):
        self.name=name
        self.code=code
        self.product_count = 0  # Initialize product count to 0
        
    def __str__(self):
        return f"\nCategory Name: {self.name}, Code: {self.code} , Price :"

#create product class with name,code,category and price
class product:
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.price=price
        self.category=category
        category.product_count += 1

    @classmethod
    def Lowsort(self, k):
            n = len(k)
            for i in range(n):
                for j in range(i + 1, n):
                    if k[j].price < k[i].price:
                        k[i], k[j] = k[j], k[i]
    
    @classmethod
    def Highsort(self, h):
        n = len(h)
        for i in range(n):
            for  j in range(i + 1, n):
                if h[j].price > h[i].price:
                    h[i], h[j] = h[j], h[i]
    @classmethod
    def search(self,code):
        srch =  int(input("\nEnter Code ::"))
        for i in lst:
            if i.code == srch:
                # print("Product Found")
                print(i.name,i.code,i.category,i.price) 

#Create different category

cat1=category("Electrics",1111)
cat2=category("Metals",2222)
cat3=category("Toys",3333)
cat4=category("Accessories",4444)

print("\n")

#Create 10 products

prod1=product("Laptop",101,cat1,35000)
prod2=product("Mobile",102,cat1,15000)
prod3=product("AC",103,cat1,45000)
prod4=product("Gold",104,cat2,65000)
prod5=product("Silver",105,cat2,72000)
prod6=product("Harmonium",106,cat3,5000)
prod7=product("Ball",107,cat3,50)
prod8=product("Laptop light",108,cat4,150)
prod9=product("Mouse",109,cat4,200)
prod10=product("Keyboard",110,cat4,500)

lst=[prod1,prod2,prod3,prod4,prod5,prod6,prod7,prod8,prod9,prod10]

print("::Category Details With Product Counting::\n")

for category in [cat1,cat2,cat3,cat4]:
    print(category.name,category.product_count)

print()
    
# sorting low to high
product.Lowsort(lst)

print("::Product Sorting Low To High By Price::\n")

for pro in lst:
    print(pro.name, pro.code, pro.category, pro.price)

print("\n")

#sorting high to low
product.Highsort(lst)

print("::Product Sorting High To Low By Price::\n")

for pro in lst:
    print(pro.name, pro.code, pro.category, pro.price)

product.search(prod1)    
