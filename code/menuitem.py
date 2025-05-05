from dataclasses import dataclass, asdict

@dataclass
class MenuItem:
    # these are built-in properties
    category: str
    name: str
    price: float
    description: str

    # convert to a dictionary
    def to_dict(self):
        #convert the MenuItem to a dictionary format
        return asdict(self)

    @staticmethod
    def from_dict(data):
        #create a MenuItem instance from a dictionary
        return MenuItem(**data)
    
if __name__=='__main__':
    # example of howto use the dataclass

    # create a new MenuItem    
    mozzarella_sticks = MenuItem(
        name = "Mozzarella Sticks", 
        price = 8.99, 
        category="Apps", 
        description="Fried cheese sticks served with marinara sauce.")

    # can assign a new category
    mozzarella_sticks.category = "Appetizers"
    print(mozzarella_sticks)
    # convert back to a dictionary
    print(mozzarella_sticks.to_dict())

    # create a new MenuItem from a dictionary
    burger_data ={
        "name": "Burger", 
        "price": 9.99, 
        "description": "A delicious burger.", 
        "category": "Entrees"}
    burger = MenuItem.from_dict(burger_data)
    print(burger)

