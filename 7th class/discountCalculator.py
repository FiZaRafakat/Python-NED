print("DISCOUNT CALCULATOR")

bill= int(input("Enter your bill"))

if 2000<bill<=5000:
    print ("Pay the bill as it is")

elif bill>5000:
    print(bill*0.8 ,"here is your bill with 20% discount")

else:
    print("No discount applied900")        