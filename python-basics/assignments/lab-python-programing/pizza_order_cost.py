DELIVERY_FLAT_DISTANCE = 5 # miles

# PizzaOrderTaker provides the high level logic of processing a customer's
# pizza order
class PizzaOrderTaker:
    def run(self):
        order = PizzaOrderBuilder().add_size().add_toppings().add_delivery_distance().build()
        order.display()
        
# PizzaOrder is the data class that contains each piece of a single pizza order
class PizzaOrder:
    def __init__(self):
        self.size = ""
        self.num_toppings = 0
        self.delivery_dist = 0 # miles
        self.total_cost = 0.0 # $
        
    def display(self):
        order_str = f"\n== Order Details ==\nYour {self.size} pizza with {self.num_toppings} topping(s) will travel {self.delivery_dist} mile(s) to be delivered to you for a total cost of ${self.total_cost}."
        print(order_str)
        
# PizzaOrderBuilder prompts the user for each part of a pizza order, constructing the order
# as each input is received, and keeping a running total cost of the pizza order being built.
class PizzaOrderBuilder:
    def __init__(self):
        self.order = PizzaOrder()
        self.valid_sizes = ("Small", "Large")
        self.error_handle = "Sorry I didn't get that..."
        self.prices = {
            "Small": 8,
            "Large": 12,
            "Topping": 1,
            "Flat_Delivery": 2,
            f"Per_Mile_Past_{DELIVERY_FLAT_DISTANCE}": 1
        }
        print("== Welcome to Python Pizza! Let me take your order ==\n\n")
        
    def try_input_int(self, prompt):
        try:
            return int(input(prompt)),True 
        except ValueError:
            return 0,False 
        
    def add_size(self):
        order_prompt ="Select a size. We have 'Small' or 'Large': " 
        size = input(order_prompt)
        
        while size not in self.valid_sizes:
            size = input(f"{self.error_handle} {order_prompt}")
            
        self.order.size = size
        self.order.total_cost += self.prices[size]
        return self
        
    def add_toppings(self):
        order_prompt = "Enter the number of toppings on the pizza: "
        num_toppings,ok = self.try_input_int(order_prompt) 
        
        while not ok or num_toppings < 0:
            num_toppings,ok = self.try_input_int(f"{self.error_handle} {order_prompt}")
            
        self.order.num_toppings = num_toppings
        self.order.total_cost += (self.prices["Topping"] * num_toppings)
        return self
        
    def add_delivery_distance(self):
        delivery_prompt = "Enter the number of miles the delivery will take: " 
        delivery_dist,ok = self.try_input_int(delivery_prompt) 
        
        while not ok or delivery_dist < 0:
            delivery_dist = self.try_input_int(f"{self.error_handle} {delivery_prompt}")
            
        self.order.delivery_dist = delivery_dist
        self.order.total_cost += self.prices["Flat_Delivery"]
        
        remaining_chargeable_miles = delivery_dist - DELIVERY_FLAT_DISTANCE 
        if remaining_chargeable_miles > 0:
            self.order.total_cost += (self.prices[f"Per_Mile_Past_{DELIVERY_FLAT_DISTANCE}"] * remaining_chargeable_miles)
        return self

    def build(self):
        return self.order 

PizzaOrderTaker().run()