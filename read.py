def load_laptops():
    laptops = []
    try:
        with open('laptops.txt', 'r') as file:
            for line in file:
                laptop = {}
                data = line.strip().split(',')
                laptop['name'] = data[0]
                laptop['brand'] = data[1]
                laptop['price'] = data[2]
                laptop['quantity'] = data[3]
                laptop['processor'] = data[4]
                laptop['graphic card'] = data[5]
                laptops.append(laptop)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")
    return laptops
