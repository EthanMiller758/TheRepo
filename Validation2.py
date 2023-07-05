# Program description: This is a program used by Computers R Us to evaluate retail staff on a weekly basis and compare their totals at a regional level.
# Written by: Ethan Miller
# Date written: May-30-2023-May--2023

# Program constants.

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


 while True:
    Process = input("Do you want to process another employee? (Y/N): ").upper()
    if Process == "":
      print("Error - The process cannot be blank.")
    elif Process == "N":
     breakpoint("Thanks for the help!")
    else:
     if Process == "Y":
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


