import re
from datetime import datetime

class customer:
    def __init__(self,name,email,phone,street,city,state,country,company=None,type=None):
        self.name=self.validate_name(name)
        self.email=self.validate_email(email)
        self.phone=self.validate_phone(phone)
        self.street=street
        self.city=self.validate_city(city)
        self.state=self.validate_state(state)
        self.country=self.validate_country(country)
        self.company=company
        self.type=type
        
    def __str__(self):
        return f"{self.name}  {self.email}  {self.phone}  {self.street}  {self.city}  {self.state}    {self.country}  {self.company}   {self.type}"
    
    def validate_state(self,state):
        if re.match("^[A-Za-z]+$",state):
            return state
        else:
            raise ValueError("Invalid State")

    def validate_city(self,city):
        if re.match("^[A-Za-z]+$",city):
            return city
        else:
            raise ValueError("Invalid City")

    def validate_country(self,country):
        if re.match("^[A-Za-z]+$",country):
            return country
        else:
            raise ValueError("Invalid Country")

    def validate_name(self,name):
        if re.match("^[A-Za-z]+$",name):
            return name
        else:
            raise ValueError("Invalid Name")

    def validate_email(self, email):
        # Basic email validation using a regular expression
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            raise ValueError("Invalid email address")

    def validate_phone(self, phone):
        # Basic phone number validation using a regular expression
        if re.match(r"\d{10}", phone):
            return phone
        else:
            raise ValueError("Invalid phone number")
    @staticmethod
    def info(self):
        print(self) 
           
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"  product:{self.name}  price:{self.price} "

class order:
    def __init__(self,number,date,company,billing,shipping,order_lines=None):
        
        
        if date < datetime.today():
            raise ValueError("Order date must be today or in the future.")
        
        self.number=number
        self.date=date
        self.company=company
        self.billing=billing
        self.shipping=shipping
        self.order_lines=order_lines
        
    def __str__(self):
        return f"Order Number : {self.number} , Date : {self.date} ,\n Company : {self.company} , \nBilling : {self.billing} ,\n Shipping : {self.shipping}"
    
    @staticmethod
    def calculate_total_amount():
        total_amount = sum(order_line.subtotal for order_line in orderLine_lst)
        return total_amount
        
    @staticmethod
    def display_order():
        for order_line in orderLine_lst:
            print(f"{order_line}")
        print(f"\nTotal:{orderone.calculate_total_amount()} ")
    
    def display_prod_list(self, product):
        orders_for_product = [order_line.order for order_line in orderLine_lst if product in order_line.product]
        if orders_for_product:
            print(f"{product.name}:")
            for order_for_product in orders_for_product:
                print(f"Order {order_for_product.number} ")
            print()

    @staticmethod
    def order_by_date(order_lst):
        n=len(order_lst)
        for i in range(n):
            for j in range(i + 1, n):
                if order_lst[j].date < order_lst[i].date:
                    order_lst[i], order_lst[j] = order_lst[j], order_lst[i]
        for i in order_lst:
            print(f"Order Number: {i.number}   date: {i.date}  company:  {i.company}   billing:  {i.billing}   shipping: {i.shipping} ")
            print()
    
    def is_current_month(self):
        current_date = datetime.today()
        return self.date.month == current_date.month and self.date.year == current_date.year

    @classmethod
    def current_month_list(cls, order_lst):
        current_month_orders = [order for order in order_lst if order.is_current_month()]
        return current_month_orders

    def search_number(self,order_lst):
        search=int(input("Enter the number of order:"))
        for i in order_lst:
            if i.number == search:
                print(f"Order number: {i.number}   date: {i.date}  company:  {i.company}   billing:  {i.billing}   shipping: {i.shipping} ")

    # def order_details():
    #     for i in order_lst:
    #         print(i.number,i.date,i.company,i.billing,i.shipping)
    #         print()
        
class orderLine:
    def __init__(self,order,product,quantity,price):
        self.order=order
        self.product=product
        self.quantity=quantity
        self.price=price
        self.subtotal=self.calculate_subtotal()
    
    def __str__(self):
        product_str = "\n".join(str(product) for product in self.product)
        return f"{self.order} \n  {product_str} \n Quantity: {self.quantity} \n Subtotal: {self.subtotal} "

    def calculate_subtotal(self):
            return self.quantity*self.price     
    
    # def orderline_details():
    #       for i in orderLine_lst:
    #           print(i.order,i.product,i.quantity,i.price)


company_customer = customer("ABCompany","company@example.com","1234567890","123 Main","Cityville","Stateville","Countryland",None,"company")

# Creating a contact customer
contact_customer = customer("JohDoe","john.doe@example.com","9876543210","456 Side Street","Townsville","Stateland","Countryland",company_customer,"contact")  # Linking the contact customer to a company

# Creating a billing customer
billing_customer = customer("BillCustomer","billing@example.com","5555555555","789 Billing Street",
"Billington","Billingstate", "Countryland",company_customer,"billing")

# Creating a shipping customer
shipping_customer = customer("ShippCustomer","shipping@example.com","9999999999","987 Shipping Street","Shipville","Shippingstate","Countryland",company_customer,"shipping")

cust_lst=[company_customer,contact_customer,billing_customer,shipping_customer]

#product Objects
pro1=Product("product1",50)
pro2=Product("product2",60)
pro3=Product("product3",60)
pro4=Product("product4",40)
pro5=Product("product5",10)

product_list=[pro1,pro2,pro3,pro4,pro5]

#customer.info()

#create object for order class

orderone = order(12346,datetime(2024,1,25),company_customer,billing_customer ,shipping_customer)

ordertwo = order(789456,datetime(2024,2,22),company_customer,billing_customer ,shipping_customer)

orderthree = order(101112,datetime(2024,1,30),company_customer,billing_customer ,shipping_customer)

order_lst=[orderone,ordertwo,orderthree]

#Create objects for order_line

orderline1=orderLine(orderone,[pro1,pro2],10,5000)

orderline2=orderLine(ordertwo,[pro3,pro4],5,1000)

orderline3=orderLine(orderthree,[pro2,pro5],15,50000)

orderLine_lst=[orderline1,orderline2,orderline3]

print("\n-------Display Order Details--------\n")
order.display_order()

print("\n---------------Order By Date-------------\n")
order.order_by_date(order_lst)

print("---------list of all order by specific product-------------")
products_to_search = [pro1, pro2,pro3,pro4,pro5]

for product in products_to_search:
    for order in order_lst:
        order.display_prod_list(product)

print("---------------current_month-------------------------")

current_month_orders = order.current_month_list(order_lst)
for order in current_month_orders:
    print(f"  number: {order.number}   date: {order.date}  company:  {order.company}   billing:  {order.billing}   shipping: {order.shipping} ")
    print("\n")
print("\n")

print("-----------Search By Order Number------------")
order.search_number(order_lst)