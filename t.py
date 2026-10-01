# Starter lists
items = ["Rice", "Beans", "Sugar", "Milk", "Bread"]
prices = [1500, 1200, 1800, 900, 600]    # prices in RWF

# Helper function to write to both the terminal and recip.txt using open()
def write_output(text):
    # Print to console
    print(text)
    # Open file in append mode ("a") - automatically creates recip.txt if missing
    with open("recip.txt", "a") as file:
        file.write(text + "\n")

# Task (c): Function to calculate total price
def calculate_total(prices_list):
    total = 0
    for price in prices_list:
        total += price
    return total

# Task (d): Function to apply discount and display checkout details
def apply_discount(total):
    write_output(f"\nTotal: {total} RWF")
    
    if total > 20000:
        discount = total * 0.10
        write_output(f"Discount (10%): {int(discount)} RWF")
    else:
        discount = 0
        write_output("Discount (10%): 0 RWF")
        
    amount_to_pay = total - discount
    write_output(f"You pay: {int(amount_to_pay)} RWF")

# ⭐ Bonus Challenge: Find and print the most expensive item
def show_most_expensive():
    if not prices:
        write_output("The cart is empty.")
        return
        
    max_price = prices[0]
    max_index = 0
    
    for i in range(1, len(prices)):
        if prices[i] > max_price:
            max_price = prices[i]
            max_index = i
            
    write_output(f"\n⭐ Most Expensive Item: {items[max_index]} - {max_price} RWF")

# Task (e): Menu loop using while True
while True:
    print("\n=== MINI-MARKET ===")
    print("1. View cart   2. Add item   3. Checkout   4. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        # Task (a): Print every item with its number and price
        write_output("\n--- Current Cart Items ---")
        for i in range(len(items)):
            write_output(f"{i + 1}. {items[i]} - {prices[i]} RWF")
            
    elif choice == "2":
        # Task (b): Add a new product to both lists
        new_name = input("Enter new product name: ")
        new_price = int(input("Enter product price in RWF: "))
        
        items.append(new_name)
        prices.append(new_price)
        
        write_output(f"\nProduct added! Updated total items count: {len(items)}")
        
    elif choice == "3":
        # Checkout logic using defined functions
        current_total = calculate_total(prices)
        apply_discount(current_total)
        show_most_expensive() # Bonus output
        
    elif choice == "4":
        write_output("Thank you for visiting Musanze Mini-Market. Goodbye!")
        break
        
    else:
        write_output("Invalid choice. Please pick a number from 1 to 4.")