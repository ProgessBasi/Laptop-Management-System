from write import write_laptops
import time


def order_customers(laptops):
    try:
        name = input("Enter your name: ")
        phno = int(input("Enter your phone number: "))
    except ValueError:
        print("Invalid input. Please enter a valid input.")
        return

    total_cost = 0
    purchase_items = []

    while True:
        laptop_name = input("Enter the name of the laptop you want to purchase (type 'done' to finish): ")
        if laptop_name == 'done':
            break
        
        try:
            quantity = int(input("Enter the quantity you want to purchase: "))
            if quantity <= 0:
                print("Invalid input. Please enter a valid quantity.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid input.")
            continue

        for laptop in laptops:
            if laptop["name"] == laptop_name:
                if int(laptop["quantity"]) >= quantity:
                    laptop["quantity"] = str(int(laptop["quantity"]) - quantity)
                    purchase_item = {
                        'name': laptop_name,
                        'brand': laptop['brand'],
                        'processor': laptop['processor'],
                        'graphic card': laptop['graphic card'],
                        'quantity': quantity,
                        'price': int(laptop['price']),
                        'cost': int(laptop['price']) * quantity * 1.13
                    }
                    purchase_items.append(purchase_item)
                    total_cost += purchase_item['cost']
                    print(f"{quantity} {laptop_name} added to cart.")
                    break
                else:
                    print(f"Sorry, we only have {laptop['quantity']} {laptop_name}(s) available.")
                break
        else:
            print(f"Sorry, we do not have {laptop_name} in stock.")

    if purchase_items:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        invoice = f"\n============================== INVOICE ==============================\n"
        invoice += f"Customer name: {name}\nPhone no: {phno}\nPurchase time: {timestamp}\n"
        for purchase_item in purchase_items:
            invoice += f"\nLaptop: {purchase_item['name']}\nBrand: {purchase_item['brand']}\nProcessor: {purchase_item['processor']}\nGraphic card: {purchase_item['graphic card']}\nQuantity: {purchase_item['quantity']}\nPrice per unit: ${purchase_item['price']}\nTotal cost: ${purchase_item['cost']}\n"
        invoice += f"\nTotal cost: ${total_cost}\nVAT (13%): ${round(total_cost * 0.13, 2)}\nGross amount: ${round(total_cost * 1.13, 2)}\n"
        invoice += f"\n============================ Thank you! ============================\n"

        with open('invoices.txt', 'a') as file:
            file.write(invoice)
        write_laptops(laptops)
        print(invoice)

def order_supplier(laptops):
    try:
        name = input("Enter your store name: ")
        phno = int(input("Enter your landline number: "))
    except ValueError:
        print("Invalid input. Please enter a valid input.")
        return

    total_cost = 0
    purchase_items = []

    while True:
        laptop_name = input("Enter the name of the laptop you want to purchase (type 'done' to finish): ")
        if laptop_name == 'done':
            break
        
        try:
            quantity = int(input("Enter the quantity you want to purchase: "))
            if quantity <= 0:
                print("Invalid input. Please enter a valid quantity.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid input.")
            continue

        for laptop in laptops:
            if laptop["name"] == laptop_name:
                if int(laptop["quantity"]) >= quantity:
                    laptop["quantity"] = str(int(laptop["quantity"]) - quantity)
                    purchase_item = {
                        'name': laptop_name,
                        'brand': laptop['brand'],
                        'processor': laptop['processor'],
                        'graphic card': laptop['graphic card'],
                        'quantity': quantity,
                        'price': int(laptop['price']),
                        'cost': int(laptop['price']) * quantity * 1.13
                    }
                    purchase_items.append(purchase_item)
                    total_cost += purchase_item['cost']
                    print(f"{quantity} {laptop_name} added to cart.")
                    break
                else:
                    print(f"Sorry, we only have {laptop['quantity']} {laptop_name}(s) available.")
                break
        else:
            print(f"Sorry, we do not have {laptop_name} in stock.")

    if purchase_items:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        invoice = f"\n============================== INVOICE ==============================\n"
        invoice += f"Store name: {name}\nLandline no: {phno}\nPurchase time: {timestamp}\n"
        for purchase_item in purchase_items:
            invoice += f"\nLaptop: {purchase_item['name']}\nBrand: {purchase_item['brand']}\nProcessor: {purchase_item['processor']}\nGraphic card: {purchase_item['graphic card']}\nQuantity: {purchase_item['quantity']}\nPrice per unit: ${purchase_item['price']}\nTotal cost: ${purchase_item['cost']}\n"
        invoice += f"\nTotal cost: ${total_cost}\nVAT (13%): ${round(total_cost * 0.13, 2)}\nGross amount: ${round(total_cost * 1.13, 2)}\n"
        invoice += f"\n============================ Thank you! ============================\n"

        with open('invoices.txt', 'a') as file:
            file.write(invoice)
        write_laptops(laptops)
        print(invoice)
