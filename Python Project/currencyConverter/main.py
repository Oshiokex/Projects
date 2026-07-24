import converter

currencies = {
    "euros" : {"rate" : 1250},
    "dollars" : {"rate" : 1250},
    "rupies" : {"rate" : 1250},
}

print("---> Welcome to my currency converter <---")

while True:
    Choice = input("""
Enter the Currency you want to convert to 
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