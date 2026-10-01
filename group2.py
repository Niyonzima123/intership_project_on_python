# Starter lists
items =['Beans','Oil','Maize','Rice','Cassava','Potatoes','Ikiraha']
prices =[1200,1500,1000,1600,700,500,300]

# Task (c): Function to calculate total price
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

# Task (d): Function to apply discount and display checkout details
def apply_discount(total):
    print(f"\nTotal: {total} RWF")
    
    if total > 20000:
        discount = total * 0.10
        print(f"Discount (10%): {int(discount)} RWF")
    else:
        discount = 0
        print("Discount (10%): 0 RWF")
        
    amount_to_pay = total - discount
    print(f"You pay: {int(amount_to_pay)} RWF")

# ⭐ Bonus Challenge: Find and print the most expensive item
def show_most_expensive():
    if not prices:
        print("The cart is empty.")
        return
        
    max_price = prices[0]
    max_index = 0
    
    for i in range(1, len(prices)):
        if prices[i] > max_price:
            max_price = prices[i]
            max_index = i
            
    print(f"\n⭐ Most Expensive Item: {items[max_index]} - {max_price} RWF")

# Task (e): Menu loop using while True
while True:
    print("\n select one choice")
    print("1. View cart   2. Add item   3. Checkout   4. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        print("\nCurrent Cart Items ")
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]} - {prices[i]} RWF")
            
    elif choice == "2":
        # Task (b): Add a new product to both lists
        new_name = input("Enter new product name: ")
        new_price = int(input("Enter product price in RWF: "))
        
        items.append(new_name)
        prices.append(new_price)
        
        print(f"\nProduct added! Updated total items count: {len(items)}")
        
    elif choice == "3":
        # Checkout logic using defined functions
        current_total = calculate_total(prices)
        apply_discount(current_total)
        show_most_expensive() # Bonus output
        
    elif choice == "4":
        print("Thank you for visiting Musanze Mini-Market. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please pick a number from 1 to 4.")
