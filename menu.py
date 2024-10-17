# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_choice = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_choice.isdigit():

        menu_choice = int(menu_choice)

        # Check if the customer's input is a valid option
        if menu_choice in menu_items:
            # Save the menu category name to a variable
            menu_category = menu_items[menu_choice]

            # Print out the menu category name they selected
            print(f"\nYou have selected {menu_category}. Here are the items available:")

            # Print out the menu options from the menu_category_name
            item_index = 1
            category_items = menu[menu_category]
            item_lookup = {}

            # Check if the menu item is a dictionary to handle differently
            if isinstance(category_items, dict):
                for item, price in category_items.items():
                    if isinstance(price, dict):  # Handle case where there are sub-items
                        for sub_item, sub_price in price.items():
                            print(f"{item_index}: {item} ({sub_item}) - ${sub_price:.2f}")
                            item_lookup[item_index] = (item, sub_item, sub_price)
                            item_index += 1
                    else:
                        print(f"{item_index}: {item} - ${price:.2f}")
                        item_lookup[item_index] = (item, None, price)
                        item_index += 1
            else:

                print("The selected category does not have any valid items.")
                continue

            # 2. Ask customer to input menu item number
            item_choice = input("\nEnter the number of the item you'd like to order: ")

            # 3. Check if the customer typed a number
            if item_choice.isdigit():
                # Convert the menu selection to an integer
                item_choice = int(item_choice)

                # 4. Check if the menu selection is in the menu items
                if item_choice in item_lookup:
                    # Store the item name as a variable
                    item_name, sub_item, item_price = item_lookup[item_choice]
                    full_item_name = f"{item_name} ({sub_item})" if sub_item else item_name

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {full_item_name}s would you like? ")

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order.append({"name": full_item_name, "price": item_price, "quantity": quantity})
                    print(f"Added {quantity} {full_item_name}(s) to your order.")

                else:
                    # Tell the customer that their input isn't valid
                    print("That was not a valid item selection.")
            else:
                # Tell the customer they didn't select a menu option
                print("That was not a valid number.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("\nWould you like to order anything else? (Y)es or (N)o ").lower()

        # 5. Check the customer's input

                # Keep ordering
        if keep_ordering == 'y':
                # Exit the keep ordering question loop
            break

                # Complete the order
        elif keep_ordering == 'n':
                # Since the customer decided to stop ordering, thank them for
                # their order
            print("\nThank you for your order!")

                # Exit the keep ordering question loop
            place_order = False
            break

                # Tell the customer to try again
        else:
            print("Please enter a valid choice: (Y)es or (N)o.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["name"]
    price = item["price"]
    quantity = item["quantity"]

    # 8. Calculate the number of spaces for formatted printing
    name_spaces = 26 - len(item_name)
    price_spaces = 8 - len(f"${price:.2f}")

    # 9. Create space strings
    name_space_str = " " * name_spaces
    price_space_str = " " * price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_space_str} | ${price:.2f}{price_space_str} | {quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(item["price"] * item["quantity"] for item in order)
print(f"\nTotal cost: ${total_cost:.2f}")
print("\nThank you for ordering from the variety food truck!")