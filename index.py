#handles the main processes
import bs4, requests, urllib.request, sys, os
sys.path.insert(1, r'C:\Users\nolan\Documents\master-ps5\utils')
import ps5
version = '0.1'
code_released = requests.get('https://raw.githubusercontent.com/StevenHarvey/PS5Autobuy/main/version.txt')
def login():
    try:
        check1 = open(r'information(IMPORTANT)\completed.txt', 'r+').read()
        if '1' in check1:
            print("Data already found! Launching now")
            ps5.main()

    except:
        check1 = open(r"information(IMPORTANT)\completed.txt", 'w')
        print("Note: No Data will leave this PC and Walmart.Com")
        data_write = open(r'information(IMPORTANT)\information.txt', 'r+')
        name_first = input("Insert first name:")
        data_write.write(name_first)
        name_last = input("Insert last name:")
        data_write.write("\n"+name_last)
        address = input("Insert address:")
        data_write.write("\n"+address)
        phone_number = input("Insert phone number:")
        data_write.write("\n"+phone_number)
        email = input("Insert email address:")
        data_write.write("\n"+email)
        state = input("Insert state:")
        data_write.write("\n"+state)
        zipcode = input("Insert zipcode:")
        data_write.write("\n"+zipcode)
        card = input("Insert card number:")
        data_write.write("\n"+card)
        exporation = input("Insert exporation date:")
        data_write.write("\n"+exporation)
        check1.write("1")
        check1.close()
        login()
if version in str(code_released.content):
    input("Working, press enter to continue")
    login()
else:
    input("Update needed! Go to the GitHub for a new version or press enter and request a new version now.")
    input("Feature coming soon - Update directly from GitHub for now.")