import time
import os
os.system('pause') 


def login_sequence():
    print('Enter your password and username.')

login_sequence()
while True:    
    userName = str("Nicholas")
    loginPassword = str("password")    
    loginName = input("Enter username: ")
    loginPass = input("Enter password: ")
    if loginName == userName and loginPass == loginPassword:
        print('\n------------------Hello Nicholas!---------------------------------------------------------------------------------------\n')
        break   
    elif loginName != userName or loginPass != loginPassword:     
        print('\nWrong login. Please re-enter your username and password\n')
  

website = {}


def main_menu():
    print('Select a menu option:',
    '\n1.Retrieve a password',
    '\n2.Enter a new password',
    '\n3.Exit to desktop')

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
        print('\nYour websites: ' )
        for k in website.keys():
            print(k)
        find_website = input(str("Enter the website you would like the password for: "))
        print('Your password is: ', website[find_website])               
        done = input(str('Would you like to retrieve another password? \n Yes or No:\n'))
        if done == str('Yes'):
            menu1()
        if done == str('No'):                        
            main_menu() 


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

def menu3():
    print('Goodbye Nicholas!') 
    time.sleep(2)
    exit()


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



