if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from menuitem import MenuItem


def clean_price(price:str) -> float:
    price = price.replace("$", "").replace(",","")
    return float(price)

def clean_scraped_text(scraped_text: str) -> list[str]:
    #clean up scraped text and return a list of useful strings
    items = scraped_text.split("\n")
    cleaned_items = []

    #filter out unwanted lines
    for item in items:
        if item in ['GS', "V", "S", "P"]:
            continue
        if "NEW" in item:
            continue
        if item.strip() == "":
            continue
        cleaned_items.append(item)
    return cleaned_items

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    #extract the menu item data and return a MenuItem instance
    cleaned_items = clean_scraped_text(scraped_text)
    item = MenuItem(category=title, name="", price=0.0, description="")

    item.name = cleaned_items[0]
    item.price = clean_price(cleaned_items[1])

    #set description or default message
    if len(cleaned_items) > 2:
        item=description = cleaned_items[2]
    else:
        item.description = "No description available"
    
    return item



if __name__=='__main__':
    #test with some example menu item data
    test_data = [
        '''
NEW!
Tully Tots
$11.79
Made from scratch with shredded potatoes, cheddar-jack cheese and Romano cheese all rolled up and deep-fried. Served with a spicy cheese sauce.
''',
'''Super Nachos
$15.49
GS

Tortilla chips topped with a mix of spicy beef and refried beans, nacho cheese sauce, olives, pico de gallo, jalepenos, scallions and shredded lettuce. Sour cream and salsa on the side. Add guacomole $2...
'''
    ]

    for data in test_data:
        print(extract_menu_item("Appetizers", data))
