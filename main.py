from read import load_laptops
from write import write_laptops
from operations import order_customers, order_supplier

def main():

    laptops = load_laptops()

    print("Available laptops: ")    
    for laptop in laptops:
        print(f"Name: {laptop['name']}")
        print(f"Brand: {laptop['brand']}")
        print(f"Price: ${laptop['price']}")
        print(f"Quantity: {laptop['quantity']}")
        print(f"Processor: {laptop['processor']}")
        print(f"Graphic card: {laptop['graphic card']}")
        print()

    continueLoop = True
    while continueLoop == True:
        MorS = input("Are you a manufacturer or a customer? ")
        if MorS.upper() == "CUSTOMER":
            continueLoop = False
            order_customers(laptops)    
        elif MorS.upper() == "MANUFACTURER":
            continueLoop = False
            order_supplier(laptops)
        else:
            print("Invalid input.")
            cont = input("Do you want to try again? Enter 'yes' to continue or anything else to exit: ").lower()
            if cont == "yes":
                continue
            else:
                print("Successfully closed.")
                return

    cont = input("Do you want to make another purchase? Enter 'yes' to continue or anything else to exit: ").lower()
    if cont == "yes":
        main()
    else:
        print("Successfully closed.")
        return

main()
