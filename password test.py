import time
import os
os.system('pause') 

login_data = {}
website = {}

#where the user signs up
def sign_up_sequence():
    print('\n------------------Sign Up-----------------------------------------------------------------------------------------------\n')
    print('Enter a new password and username.')
    sign_up_data = True
    while sign_up_data:
        set_up_username = input(str("Enter a new username: "))
        set_up_password = input(str('Enter a new password: '))
        login_data[set_up_username] = set_up_password
        login_data_file = open('login_data_file.txt', 'w')
        for k,v in login_data.items():
            login_data_file.write(k + '|' + v)
        login_data_file.close()
        if len(login_data) == 1:
            break

#where the user signs in        
def login_sequence():
    print('\n------------------Sign In-----------------------------------------------------------------------------------------------\n')
    print('Enter your password and username.')
    while True:
        f = open('login_data_file.txt', 'r')
        for line in f:
            splitter = line.split('|')
            login_data[str(splitter[0])] = splitter[1]       
        loginName = input("Enter username: ")
        loginPass = input("Enter password: ")
        if loginName in login_data and login_data[loginName] == loginPass:
            print('\n------------------Hello', loginName,'!---------------------------------------------------------------------------------------\n')
            break   
        elif loginName != login_data[loginName] or loginPass != login_data[loginPass]:     
            print('\nWrong login. Please re-enter your username and password.\n')

#this checks to see if th user needs to sign up or can proceed with the sign in screen
def login_check():
    f = open('login_data_file.txt', 'r')
    for line in f:
        splitter = line.split('|')
        login_data[str(splitter[0])] = splitter[1]
   
    if len(login_data) == 0:
        sign_up_sequence()
        
    if len(login_data) >= 1 :
        login_sequence()

#start of the program        
def start():
    login_check()        


#the main menu
def main_menu():
    print('Select a menu option:',
    '\n1.Retrieve a password',
    '\n2.Enter a new password',
    '\n3.Exit to desktop')

#lets user retrieve stored passwords
def menu1():
    f = open('password_manager_file.txt', 'r')
    for line in f:
        splitter = line.split('|')
        website[str(splitter[0])] = splitter[1]
    if len(website) == 0:
        print('\nThere are no entered websites or passwords.\n')
        done = input(str('Would you like to add a password? \n Yes or No:\n'))
        if done == str('Yes'):
            menu2()
        if done == str('No'):                        
            return
    if len(website) >= 1:
        print('\nYour websites: ')
        for k in website.keys():
            print(k)
        find_website = input(str("Enter the website you would like the password for: "))
        print('Your password is: ', website[find_website])               
        done = input(str('Would you like to retrieve another password? \n Yes or No:\n'))
        if done == str('Yes'):
            menu1()
        if done == str('No'):                        
            main_menu() 

#lets user add new passwords
def menu2():
    website_open = True
    while website_open:
        added_website = input(str("Enter a new website: "))
        added_password = input(str('Enter a new password: '))
        website[added_website] = added_password
        text_file = open('password_manager_file.txt', 'w')
        for k,v in website.items():
                text_file.write(k + '|' + v)
        text_file.close()
        done = input(str('Would you like to continue? \n Yes or No:\n'))
        if done == str('No'):
            website_open = False
            

#end of the program
def menu3():
    print('Goodbye!') 
    time.sleep(2)
    exit()
start()

main_menu()
pick_option = int(input('Enter menu option: '))

while pick_option != 0:
    if pick_option == 1:
        menu1()       
    elif pick_option == 2:
        menu2()  
    elif pick_option == 3:
        menu3() 
    else:
        print("Invalid option! Please enter a correct option to continue.")
        
    main_menu()
    pick_option = int(input('Enter menu option: '))
