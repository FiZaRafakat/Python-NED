cal = int(input("Enter a Bill amount ...."))

if cal > 5000 :
    disc = (cal*20)/100
    Bill = cal - disc
    print(Bill)
elif cal > 2000 and cal <= 5000:
    disc = (cal*10)/100
    Bill = cal-disc
    print(Bill)
else :
    print('Total bill is',cal)
    print("No discount is applied!!!")