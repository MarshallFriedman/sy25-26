inventory = {}

while True:
    print(f"\nOptions: [1] Add [2] Remove [3] List [4] Exit")
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"{quantity} {item}(s) added to inventory.")
    elif choice == "2":
        name = input("Which item would you like to remove? ")
        if name in inventory:
            quantity = int(input("How many would you like to remove? "))
            if quantity <= inventory[name]:
                inventory[name] -= quantity
                print(f"{quantity} {name}(s) removed from inventory.")
                if inventory[name] == 0:
                    del inventory[name]
            else:
                print(f"Not enough {name}(s) in inventory to remove.")
        else:
            print(f"{name} not found in inventory.")
    elif choice == "3":
        if inventory:
            print("Current Inventory:")
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")
        else:
            print("Inventory is empty.")
    elif choice == "4":
        print("Exiting inventory management.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")