import action
import getpass

action.accounts = {
    "Divine": {"pin": "5225", "balance": 1000, "limits": 100000, "history": []},
    "Oshioke": {"balance": 3000, "pin": "5225", "limits": 300000, "history": []},
}


print("----> WELCOME TO OSHIOKE MFB <----")

while True:
    menu = input("""
--> What would you like to do:
1. Login
2. Create Account
3. Show Users
0. Quit: --> """)

    if menu == "1":
        name = input("> Enter your name: ")
        pin = getpass.getpass("> Enter your pin: ")
        if name in action.accounts and pin == action.accounts[name]["pin"]:
            print(" ")
            print(f"--> Welcome {name} <--")
            action.actions()
        else:
            print("--> Incorrect Username And Pin <--")

    elif menu == "2":
        action.create_account()

    elif menu == "3":
        action.show_users()

    elif menu == "0":
        print("--> GoodBye!!! <--")
        break

    else:
        print("--> Invalid input <--")
