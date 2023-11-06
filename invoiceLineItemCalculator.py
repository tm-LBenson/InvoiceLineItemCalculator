# Lewis Benson
# CIS261
# InvoiceLineItemCalculator

def get_float(prompt):
    """Prompt the user for a float value and return it."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_int(prompt):
    """Prompt the user for an integer value and return it."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    """Main function that runs the invoice line item calculator program."""
    print("The Invoice Line Item Calculator")
    
    while True:
        price = get_float("Enter price: ")
        quantity = get_int("Enter quantity: ")
        
        total = price * quantity
        # F-string with format options. Using the > to move it to the right
        # .2f makes it a floating point with 2 decimals. 
        print(f"PRICE:     {price:>.2f}")
        print(f"QUANTITY:  {quantity}")
        print(f"TOTAL:     {total:>.2f}")
        
        another = input("Enter another line item? (y/n): ").lower()
        if another[0] != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
