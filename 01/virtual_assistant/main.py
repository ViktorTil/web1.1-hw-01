from functions import *
from base_cls import *

def input_command_items():
    print("Welcome to Virtual Assistant!")
    contacts = Contacts()
    notes = Notes()
    load_books(filename)

    while True:   
        print(command_offer(command_maps))
        command = nick_str(command_item = input("Enter the command: ").lower(), command_items = command_maps.keys())
        if command:
            try:
                print(command_maps[command]())
            except TypeError:
                try:
                    items = command_items(command)
                    items = nick_str(command = command, command_items = items)
                    for item in items:
                        if item == "note":
                            name = input(f"Enter the {Colors.HEADER}note title{Colors.ENDC}: ").lower()
                            print(command_maps[command]([item], name))
                            items.remove(item)
                                
                        if len(items) < 1:
                            continue
                    
                        if item == "tags" and item in list(filter(lambda x: available_options[command][x] == True, available_options[command])):
                            name = input(f"Enter the note title of the tags: ").lower()
                            print(command_maps[command](items, name))
                        
                        elif item in list(filter(lambda x: available_options[command][x] == True, available_options[command])):
                            name = input(f"Enter the name of the contact: ").lower()
                            print(command_maps[command](items, name))

                        else:
                            print(f"{Colors.FAIL}{Colors.UNDERLINE}Error: choose from available options.{Colors.ENDC}")

                except KeyError:
                    folder = input("Enter the path of the folder to organize: ")
                    print(command_maps[command](folder))
                    continue
                  
            
if __name__ == "__main__":
    input_command_items()
