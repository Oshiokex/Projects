currencies = {
    "euros" : {"rate" : 1557.10},
    "dollars" : {"rate" : 1366.81},
    "rupees" : {"rate" : 14.18},
}

def convert(Choice):
    global currencies
    if Choice in currencies:    
        rate = currencies[Choice]["rate"]
        amt_naira = float(input("Enter amount in naira> NGN: "))
        newamt = amt_naira / rate
        print(f"{amt_naira} Naira(s) is equal to {newamt} {Choice}")

    else:
        print("invalid input")
