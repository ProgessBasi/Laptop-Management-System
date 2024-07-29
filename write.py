def write_laptops(laptops):

        with open('laptops.txt', 'w') as file:
            for laptop in laptops:
                file.write(f"{laptop['name']},{laptop['brand']},{laptop['price']},{laptop['quantity']},{laptop['processor']},{laptop['graphic card']}\n")

