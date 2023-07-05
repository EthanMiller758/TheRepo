# Program description: This is a program designed to help Billy Bob Bike Rentals process bike rentals he has made for the day.
# Written by: Ethan Miller
# Date written: May 29-2023
'''
# Program inputs.
CustName = input("Enter the customer's name: ")
if CustName == "":
    print("CustName cannot be blank - Please enter a name.")
PhoNum = input("Enter the phone number: ")
if PhoNum == "":
    print("PhoNum cannot be blank - Please enter a phone number.")
CodeType = input("Enter the code for the type of bike rented(T,M,or B): ")
if CodeType == "":
    print("CodeType cannot be blank - Please put in a code for the type of bike rented.")
NumBic = input("Enter the number of bikes rented(must be between 1 and 3: ")
NumBic = int(NumBic)
if NumBic > 3:
    print("NumBic exceeds amount - please enter a number between 1 and 3.")
CredNum = input("Enter the credit card number: ")
ExpDate = input("Enter the expiry date: ")
input("Do you want to continue?(Y or N): ")
'''

# Program description: This program is used to help a local used car company process used car sales.
# Written by: Ethan Miller
# Date written: May-28-2023 - May 2023

# Program inputs.
'''
while True:
    CustName = input("Enter the customer name: ")

    if CustName == "":
        print("Error - the customer name cannot be blank.")
    else:
        break





while True:
    PhoNum = input("Enter the phone number: ")

    if PhoNum == "":
        print("Error - the phone number cannot be blank.")
    else:break

CarYear = input("Enter the car year: ")

while True:
    MakeMod = input("Enter the make and model for the car: ")

    if MakeMod == "":
        print("Error - one variable must be entered.")
    else:break

while True:
    try:
        CarPri = input("Enter the price of the car: ")
    except:
      print("Error - the car price must be a valid number.")
    else:
     break


while True:
    try:
    TradAll = int(input("Enter the trade in allowance amount: ")
    except:
print("Error - the trade in allowance amount cannot exceed 10000")




    if CustName == "END":
        break
    
'''

# Program description: This is a program used by Computers R Us to evaluate retail staff on a weekly basis and compare their totals at a regional level.
# Written by: Ethan Miller
# Date written: May-30-2023-May--2023

# Program constants.
COMMISSION_SALES = 20.00

# Program inputs.
while True:

 while True:

  RegName = input("Enter the region name: ")
  if RegName == "":
   print("Error - The region name cannot be blank.")
  else:
        break




 while True:
    SalesFirst = input("Enter the salesperson first name: ")
    if SalesFirst == "":
        print("Error - The salesperson first name must be entered.")

    else:
        break

 while True:
    SalesLast = input("Enter the salesperson last name: ")
    if SalesLast == "":
        print("Error - The salesperson last name must be entered.")
    else:
        break

 while True:
  try:
    SalesWeek = float(input("Enter the number of sales for the week(1.00 -30000.00): "))
  except:
      print("Error - the number of sales for the week cannot exceed 30000.00.")
  else:
    if SalesWeek < 1.00 or SalesWeek > 30000.00:
     print("Error - the number of sales for the week must be between 1.00 and 30000.00.")
    else:
        break

 while True:
    try:
        NumWork = int(input("Enter the number of hours worked for the week: "))
    except:
        print("Error - The number of hours cannot exceed 60.")
    else:
        if NumWork < 10 or NumWork > 60:
            print("Error - The number of hours must be between 10 and 60.")
        else:
            break








# Program calculations.
 while True:
    try:
        GrosPay = NumWork * 26.00 * 0.01 * SalesWeek
    except:
        print("Error - The hourly rate cannot be lower than $26.00.")
    else:
        if SalesWeek < 250.00:
            COMMISSION_SALES = SalesWeek - GrosPay
        if SalesWeek > 20000.00:
            print("Above average.")
        else:
            break

        if SalesWeek in range (10000 , 20000):
         print("OK")
        else:
            break
        if SalesWeek < 10000.00:
         print("Below average.")
        else:
            break

        Increase = 0.20
        if Increase == 0.20:
            COMMISSION_SALES = SalesWeek - GrosPay
            GrosPay = NumWork * 26.00 * 0.01 * SalesWeek
        else:
            break



# Program outputs.
 while True:
    print("Computers R us - Regional Sales Analysis")
    print()
    print(f"Salesperson name: {SalesFirst:<10} {SalesLast:<10} Region: {RegName:<10}")
    print()
    SalesWeek = "${:,.2f}".format(SalesWeek)
    GrosPay = "${:,.2f}".format(GrosPay)
    print(f"Salesperson sales: {SalesWeek:<10}       Gross pay:{GrosPay:<10}")
    print(f"                                         Commission:{COMMISSION_SALES:<10}")
    print("                                          ----------------------------------")
    print(f"Status: {SalesWeek}                      Gross pay: {GrosPay}")
    print()
    print(f"Sales increase from 2 to 20%:{SalesWeek}")
    print()
    print("     Increase       Commission       Gross Pay")
    print("     -----------------------------------------")
    print()
    print()
    print()
    Process = input("Do you want to process another employee? (Y/N) :")
    if Process == "":
     print("Error - The process cannot be blank.")
    else:
     if Process == "Y":
         break
     elif Process == "N":
         exit()





















