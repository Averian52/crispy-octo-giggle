import sys

class MainMenu:
    def __init__(self, options_dict):
        self.options_dict = options_dict
        self.exit_option = "Exit"
        
    def display_menu(self):
        current_options = self.options_dict
        current_menu = "Main Menu"
        while True:
            print(current_menu + ":")
            for i, option in enumerate(current_options):
                print(str(i + 1) + ". " + option)
            choice = input("Please enter your choice: ")
            
            if choice.isdigit():
                choice = int(choice)
                if choice == len(current_options) + 1:
                    return
                elif choice == len(current_options) + 1:
                    return
                elif choice > 0 and choice <= len(current_options):
                    if type(current_options[choice - 1]) is dict:
                        current_options = current_options[choice - 1]
                        current_menu = option
                    else:
                        current_options[choice - 1]()
                else:
                    print("Invalid choice. Please enter a valid number.")
            else:
                print("Invalid choice. Please enter a valid number.")