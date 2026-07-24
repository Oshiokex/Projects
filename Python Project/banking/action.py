import getpass

his = []
accounts = {
    "Divine": {"pin": "5225", "balance": 1000.00, "limits": 100000.00, "history": []},
    "Oshioke": {"pin": "5225", "balance": 3000.00, "limits": 300000.00, "history": []},
}


def actions():
    while True:
        userchoice = input("""
1. Deposit
2. Withdrawal
3. Transfer
4. Check Balance
5. Check History
0. Exit: --> """)

        if userchoice == "1":
            deposit()
        elif userchoice == "2":
            withdraw()
        elif userchoice == "3":
            transfer()
        elif userchoice == "4":
            check_balance()
        elif userchoice == "5":
            hist()
        elif userchoice == "0":
            break
        else:
            print("--> Invalid Input <--")


# ----------------Create account----------------------------
def create_account():
    while True:
        global accounts
        name = input("> Enter a name: ")

        if name in accounts:
            print("--> you've Used this name before try another one")

        else:
            pin = getpass.getpass("> Enter your pin (4-didit): ")
            balance = float(input("> How much do you want to start with: NGN"))
            limits = 100000.0
            if balance > limits:
                print(f"--> Deposit Failed. Your balance limit is {limits}")

            else:
                accounts[name] = {
                    "pin": pin,
                    "balance": balance,
                    "limits": limits,
                    "history": [],
                }
                print("--> Account Created Successfully! <--")
                break


# ---------------------Show Users --------------------------
def show_users():
    global accounts
    print("-----------> USER(s) <-----------")
    for name in accounts:
        print(f"---> {name}")


# -----------------deposit-----------------------------------------
def deposit():
    global balance
    global limits
    name = input("> Enter your name: ")

    if name in accounts:
        amount = float(input("> How much do you want to deposit: (NGN)"))
        balance = float(accounts[name]["balance"])
        total_amt = amount + balance
        limits = float(accounts[name]["limits"])
        pin = accounts[name]["pin"]
        acct = accounts[name]["history"]

        if balance <= limits and amount <= limits and total_amt <= limits:
            new_balance = balance + amount
            acct.append(f"You Deposited NGN{amount} :new balance {new_balance}")
            accounts[name] = {
                "pin": pin,
                "limits": limits,
                "balance": new_balance,
                "history": acct,
            }
            print(f"--> New Balance = {new_balance}")

        elif total_amt > accounts[name]["limits"]:
            c_bal = limits - balance
            print(f"--> You current balance is {balance} and you limits is {limits}")
            print(f"--> Hence, you can only add {c_bal}")

    else:
        print("--> UserName Does Not Exist")


# -------------------------------Withdraw----------------------------------
def withdraw():
    global balance

    name = input("> Enter your name: ")
    login_pin = getpass.getpass("> Enter your pin: ")

    if name in accounts and login_pin == accounts[name]["pin"]:
        pin = accounts[name]["pin"]
        amount = float(input("> How much do you want to withdraw: (NGN)"))
        limits = accounts[name]["limits"]
        acct = accounts[name]["history"]
        balance = accounts[name]["balance"]

        if amount <= balance:
            new_balance = balance - amount
            acct.append(f"You Withdrawed NGN{amount}: new balance {new_balance}")
            accounts[name] = {
                "pin": pin,
                "limits": limits,
                "balance": new_balance,
                "history": acct,
            }
            print(f"--> New balance = {new_balance}")

        elif amount > balance:
            print("--> insufficient funds")
            print(f"--> your current balance is {balance}")

    else:
        print("--> Incorrect Username and password <--")


# ---------------transfer--------------------------------
def transfer():
    name = input("> Enter your name: ")
    pin = getpass.getpass("> Enter your pin: ")

    if name in accounts and pin == accounts[name]["pin"]:
        reciever = input("> Enter the name of the reciever: ")

        if reciever == name:
            print("--> You cant send money to yourself <--")

        elif reciever != name and reciever in accounts:
            pin = accounts[name]["pin"]
            balance = accounts[name]["balance"]
            limits = accounts[name]["limits"]
            acct = accounts[name]["history"]
            reciever_pin = accounts[reciever]["pin"]
            reciever_balance = accounts[reciever]["balance"]
            reciever_limits = accounts[reciever]["limits"]
            reciever_acct = accounts[reciever]["history"]

            amount = float(input("> Enter the amount you want to transfer: NGN"))
            recievers_new_Limits = reciever_limits - reciever_balance
            if amount > recievers_new_Limits:
                print(
                    f"--> {reciever} cannot recieve {amount}. he can only recieve {recievers_new_Limits}"
                )
            else:
                if amount > balance:
                    print("--> Insufficient funds")
                else:
                    withdraw = balance - amount
                    send = reciever_balance + amount
                    acct.append(
                        f"You transfered NGN{amount} to {reciever} : new balance NGN{withdraw} "
                    )
                    reciever_acct.append(
                        f"you recieved NGN{amount} from {name} : new balance NGN{send}"
                    )
                    print(f"--> Transfer of NGN{amount} to {reciever} was Successfull")
                    print(f"--> New balance NGN{withdraw}")

                    accounts[name] = {
                        "pin": pin,
                        "limits": limits,
                        "balance": withdraw,
                        "history": acct,
                    }

                    accounts[reciever] = {
                        "pin": reciever_pin,
                        "limits": reciever_limits,
                        "balance": send,
                        "history": reciever_acct,
                    }

        else:
            print(f"--> {reciever} does not have an account <--")

    else:
        print("--> Incorrect Name or Pin <--")


# ---------------------------Check Balance----------------------
def check_balance():
    name = input("> Enter your name: ")
    Logn_pin = getpass.getpass("> Enter your pin: ")

    if name in accounts and Logn_pin == accounts[name]["pin"]:
        balance = float(accounts[name]["balance"])
        if name in accounts:
            print(f"--> Balance = NGN{balance}")
    else:
        print("--> Incorrect Username or Pin <--")


# -----------------------------History---------------------------
def hist():

    name = input("Enter your name: ")
    login_pin = getpass.getpass("Enter your pin: ")

    if name in accounts and login_pin == accounts[name]["pin"]:
        acct = accounts[name]["history"]
        print(f"""
---------> {name} History <---------
              """)
        for i in acct:
            print(f"--> {i}")
    else:
        print("incorrect user or pin")
