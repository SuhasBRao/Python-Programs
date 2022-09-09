
from collections import deque


class Order:
    def __init__(self, dish, order_no, table_no):
        self.order_no = order_no
        self.dish = dish
        self.table_no = table_no
        

class ORMsystem:
    available_dishes = ["Masala dosa", "Idly vada", "Upma"]
    order_queue = deque()
    
    def __init__(self, name):
        # write your attriburtes here.
        self.name = name
    
    def create_new_order(self, waiter_id):
        dish = input("Enter order name: ")
        order_no = waiter_id
        table_no = input("Enter table no : ")
        
        order = Order(dish, order_no, table_no)
        
        if (self.order_available(dish)):
            ORMsystem.order_queue.append(order)
            # print("New order received")
            
        else:
            print("Order Not available")
        
    def order_available(self,dish):
        return True if dish in ORMsystem.available_dishes else False
    
    # def notify_waiter_for_dish(self, waiter_no):

class Cook:
    def __init__(self, name, cook_id):
        # write your attriburtes here.
        self.name = name
        self.id = cook_id
        self.order = None
        
    
    def read_order(self, orm_system):
        self.order = orm_system.order_queue.popleft()
        print(f"{self.order.dish} Order received.")
        self.prepare_dish()
        return self.order_prepared()
        
    def prepare_dish(self):
        print(f"{self.name} is preparing dish, Please wait..")
        
    
    def order_prepared(self):
        print("Order ready!!")
        return self.order.dish
        # orm_system.notify_waiter_for_order_no(self.order.order_no)


class Waiter:
    def __init__(self, name, waiter_id ):
        self.name = name
        self.id = waiter_id
    
    def create_order(self, orm_system):
        print("What order would you like sir/madam ?")
        orm_system.create_new_order(self.id)
        
    def supply(self, order):
        print(f"Waiter {self.name} is supplying the order {order}")
        

# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    orm = ORMsystem("Venu Lola")

    waiter1 = Waiter("pranav", 1)
    
    cook1 = Cook("guru",1)
    
    print("================================")
    print(orm.available_dishes)
    
    waiter1.create_order(orm)
    
    dish = cook1.read_order(orm)
    
    waiter1.supply(dish)
    

# } Driver Code ends