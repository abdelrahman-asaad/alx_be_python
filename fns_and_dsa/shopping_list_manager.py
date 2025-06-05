def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(item + " has been added to the list.")
        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(item + " has been removed from the list.")
            else:
                print(item + " not found in the list.")
        elif choice == "3":
            print("Current Shopping List:")
            if len(shopping_list) == 0:
                print("The shopping list is empty.")
            else:
                for i in range(len(shopping_list)):
                    print(str(i + 1) + ". " + shopping_list[i])
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
