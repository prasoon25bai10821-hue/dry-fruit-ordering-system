import os

# Product catalog with prices per kg
products = {
    1: {"name": "Cashew", "price_per_kg": 799},
    2: {"name": "Masala Kaju", "price_per_kg": 1299},
    3: {"name": "Peri Peri Cashew", "price_per_kg": 1399},
    4: {"name": "Chocolate Cashew", "price_per_kg": 1599},
    5: {"name": "Black Pepper Cashew", "price_per_kg": 1199},
    6: {"name": "Salted Cashew", "price_per_kg": 999},
    7: {"name": "California Almond", "price_per_kg": 799},
    8: {"name": "Chocolate Almond", "price_per_kg": 1599},
    9: {"name": "Pista", "price_per_kg": 1499},
    10: {"name": "Salted Pista", "price_per_kg": 1799},
    11: {"name": "Cranberry", "price_per_kg": 1999}
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n" + "="*60)
    print(" "*15 + "DRY FRUITS SHOP")
    print("="*60)
    print(f"{'No.':<5} {'Product Name':<25} {'Price/kg':<12} {'Price/250g':<12}")
    print("-"*60)
    
    for key, item in products.items():
        price_250g = item['price_per_kg'] / 4
        print(f"{key:<5} {item['name']:<25} ₹{item['price_per_kg']:<11} ₹{price_250g:<11.2f}")
    
    print("="*60)

def get_order():
    cart = []
    
    while True:
        display_menu()
        print("\nEnter product number (or 0 to checkout): ", end="")
        
        try:
            choice = int(input())
            
            if choice == 0:
                if len(cart) == 0:
                    print("\nYour cart is empty! Please add items first.")
                    input("Press Enter to continue...")
                    continue
                break
            
            if choice not in products:
                print("Invalid choice! Please try again.")
                input("Press Enter to continue...")
                continue
            
            print("\nSelect quantity:")
            print("1. 250g")
            print("2. 500g (2 packs)")
            print("3. 750g (3 packs)")
            print("4. 1kg (4 packs)")
            print("5. Custom quantity (in 250g packs)")
            
            qty_choice = int(input("\nEnter your choice: "))
            
            if qty_choice == 1:
                packs = 1
            elif qty_choice == 2:
                packs = 2
            elif qty_choice == 3:
                packs = 3
            elif qty_choice == 4:
                packs = 4
            elif qty_choice == 5:
                packs = int(input("Enter number of 250g packs: "))
            else:
                print("Invalid choice!")
                input("Press Enter to continue...")
                continue
            
            weight_kg = packs * 0.25
            price = products[choice]['price_per_kg'] * weight_kg
            
            cart.append({
                'product': products[choice]['name'],
                'packs': packs,
                'weight_kg': weight_kg,
                'price': price
            })
            
            print(f"\n✓ Added {products[choice]['name']} ({weight_kg}kg) to cart!")
            input("Press Enter to continue...")
            
        except ValueError:
            print("Invalid input! Please enter a number.")
            input("Press Enter to continue...")
    
    return cart

def display_bill(cart):
    clear_screen()
    print("\n" + "="*60)
    print(" "*20 + "INVOICE")
    print("="*60)
    print(f"{'Product':<25} {'Quantity':<15} {'Price':<15}")
    print("-"*60)
    
    total = 0
    for item in cart:
        print(f"{item['product']:<25} {item['weight_kg']}kg ({item['packs']} packs) ₹{item['price']:<14.2f}")
        total += item['price']
    
    print("-"*60)
    print(f"{'TOTAL':<40} ₹{total:.2f}")
    print("="*60)
    
    return total

def main():
    while True:
        clear_screen()
        print("\n" + "="*60)
        print(" "*10 + "WELCOME TO DRY FRUITS SHOP")
        print("="*60)
        print("\n1. View Menu & Place Order")
        print("2. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            cart = get_order()
            total = display_bill(cart)
            
            print("\nConfirm Order?")
            print("1. Yes")
            print("2. No")
            
            confirm = input("\nEnter your choice: ")
            
            if confirm == '1':
                print("\n" + "="*60)
                print(" "*15 + "ORDER CONFIRMED!")
                print("="*60)
                print(f"\nTotal Amount: ₹{total:.2f}")
                print("\nThank you for your order!")
                print("Your order will be delivered soon.")
                print("="*60)
                input("\nPress Enter to continue...")
            else:
                print("\nOrder cancelled!")
                input("Press Enter to continue...")
        
        elif choice == '2':
            print("\nThank you for visiting! Have a great day!")
            break
        
        else:
            print("\nInvalid choice! Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()