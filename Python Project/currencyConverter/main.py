import converter

currencies = {
    "euros" : {"rate" : 1557.10},
    "dollars" : {"rate" : 1366.81},
    "rupees" : {"rate" : 14.18},
}

print("---> Welcome to my currency converter (From Naira To ...) <---")

while True:
    Choice = input("""
From Naira to what currency: 
-> Dollars
-> Euros
-> Rupies
-> "Q" to Quit ==> """).lower()

    if Choice != "q":
        converter.convert(Choice)

    elif Choice == "q":
        print("goodbye")
        break

    else:
        print("invalid input")
