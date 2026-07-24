currencies = {
    "euros" : {"rate" : 1250},
    "dollars" : {"rate" : 1250},
    "rupies" : {"rate" : 1250},
}

def convert(Choice):
    global currencies
    if Choice in currencies:    
        rate = currencies[Choice]["rate"]
        amt_naira = int(input("Enter amount in naira> NGN: "))
        newamt = amt_naira / rate
        print(f"{amt_naira} Naira(s) is equal to {newamt} {Choice}")

    else:
        print("invalid input")