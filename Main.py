# Arrays to store item code, description, and price
item_codes = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'G1', 'G2']
descriptions = ['Compact Case', 'Tower Case', '8 GB RAM', '16 GB RAM', '32 GB RAM', '1 TB HDD', '2 TB HDD', '4 TB HDD',
                '240 GB SSD', '480 GB SSD', '1 TB HDD', '2 TB HDD', '4 TB HDD', 'DVD/Blu-Ray Player', 'DVD/Blu-Ray Re-writer',
                'Standard OS', 'Professional OS']
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Function to display available items and get user choice
def get_user_choice(category_name, category_items):
    print("Available", category_name, ":")
    for i in range(len(category_items)):
        print(f"{i + 1}. {descriptions[category_items[i] - 1]} - ${prices[category_items[i] - 1]:.2f}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(category_items):
                return category_items[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Task 1 - Setting up the system and ordering main items
print("Welcome to the Online Computer Shop!")
print("Basic components include Case, RAM, and Main Hard Disk Drive.")
case_choice = get_user_choice("Cases", [1, 2])
ram_choice = get_user_choice("RAM", [3, 4, 5])
hdd_choice = get_user_choice("Main Hard Disk Drive", [6, 7, 8])

# Calculate the price of the computer
basic_components_price = 200.00
total_price = basic_components_price + prices[case_choice - 1] + prices[ram_choice - 1] + prices[hdd_choice - 1]

# Store and output the chosen items and price of the computer
chosen_items = [descriptions[case_choice - 1], descriptions[ram_choice - 1], descriptions[hdd_choice - 1]]
print("\nChosen items:")
for item in chosen_items:
    print("-", item)
print("Total price: ${:.2f}".format(total_price))

# Task 2 - Ordering additional items
additional_items = []
while True:
    choice = input("Do you want to purchase additional items? (yes/no): ").lower()
    if choice == 'yes':
        category_choice = get_user_choice("Additional Items", [9, 10, 11, 12, 13, 14, 15, 16])
        additional_items.append(descriptions[category_choice - 1])
        total_price += prices[category_choice - 1]
    elif choice == 'no':
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

# Store and output additional items and the new price of the computer
print("\nAdditional items:")
for item in additional_items:
    print("-", item)
print("New total price: ${:.2f}".format(total_price))

# Task 3 - Offering discounts
discount = 0
if len(additional_items) == 1:
    discount = 0.05
elif len(additional_items) >= 2:
    discount = 0.10

discount_amount = total_price * discount
total_price -= discount_amount

print("\nDiscount applied: ${:.2f}".format(discount_amount))
print("Final price after discount: ${:.2f}".format(total_price))
