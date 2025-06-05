shopping_list = []
def display_menu() :
    
    add = "add"
    remove = "remove"
    view_item = "view"

    choice = "Hi"
    while choice != "exit":
        print(shopping_list)
        choice = input("what you want to do is: \nAdd Item  \nRemove Item  \nView List  \nExit \n:")   
        if choice == add :
              new_item = input("new item :")
              shopping_list.append(new_item)
    
     
        elif choice == remove:    
                removed_item = input("Enter the item you want to remove : ")
                if removed_item in shopping_list:
                   shopping_list.remove(removed_item)
                   
                else :
                    pass 
                  
        elif choice == view_item :
             pass
                
        elif choice !="exit" or add or remove or view_item :
             pass
            
display_menu()            
