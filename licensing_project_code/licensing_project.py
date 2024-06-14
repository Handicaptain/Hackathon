import os

available_software = {1:"Word", 2:"Excel", 3:"Project", 4:"Powerpoint", 5:"OneNote"}
license_count = {"Word":2 ,"Excel":2, "Project":2, "Powerpoint":2, "OneNote":2}
current_license_count = {"Word":2 ,"Excel":2, "Project":2, "Powerpoint":2, "OneNote":2}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome_menu():
    
    print("###WELCOME TO LICENSING PROJECT###")
    print("------------------------------------")

def get_num_of_users():
    num_of_users = int(input("How many users are requesting software? "))
    return num_of_users
    
def get_user_id():    
    user_id = input("Enter a user ID: ")
    return user_id
    
def get_available_software(available_software):    
    print(available_software)
    accessed = True
    while accessed == True:
        software_request_num = int(input("Please select a software to access: "))
        if software_request_num in range(1, 6):
            accessed = False
        else:
            print("Invalid selection. Please select a software from the list.")
            accessed = True
    software_request = available_software[software_request_num]
    
    return software_request
    

def vm_select(software_request):
    print(f"There are 5 virtual machines with a license for {software_request}:")
    print("1. VM1")
    print("2. VM2")
    print("3. VM3")
    print("4. VM4")
    print("5. VM5")
    accessed = True 
    while accessed == True: 
        selected_vm = int(input("Please select a VM to access: "))
        if selected_vm in range(1, 6):
            accessed = False
        else:
            print("Invalid selection. Please select a VM from the list.")
            accessed = True
    print(f"Successfully logged into the virtual machine")
    return selected_vm

def update_license_count(license_count,software_request):
    current_license_count[software_request] = current_license_count[software_request] - 1


def main():
    
    stop = False
    
    display_welcome_menu()
    
    selected_user_id = get_user_id()

    while stop == False:
        selected_software = get_available_software(available_software)
        if current_license_count[selected_software] <= 0:
            finished = input(f"{selected_software} is currently unavailable, have you finished (Y/N)?")
            if finished.capitalize() == "Y":
                clear_screen()
                display_welcome_menu()
                selected_user_id = get_user_id()
                continue
            else:
                continue
        selected_vm = vm_select(selected_software)
        update_license_count(license_count,selected_software)
        finished = input("Have you finished (Y/N)?")
        if finished.capitalize() == "Y":
            clear_screen()
            display_welcome_menu()
            selected_user_id = get_user_id()
            continue


main()


    
