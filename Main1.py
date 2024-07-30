import Operation
import Read
import Write
import random
from datetime import datetime
def main():
    Read.header()
    loop = True
    while loop == True:
        print("------------------------------------------------------------------------------------")
        print("You can choose your own option")
        print("------------------------------------------------------------------------------------")
        print("\n")
        print("Press 1 to Rent A Land ")
        print("Press 2 to Return A Rented Land")
        print("Press 3 Exit")
        print("\n")
        print("------------------------------------------------------------------------------------")
        print("\n")
        while True:
            try:
                option= int(input("Enter the option to continue: "))
                break
            except ValueError as ex:
                print("Enter numeric value")
        print("\n")
        allDict = Read.dictionary()
        if option==1:
            while True:
                try:
                    name = input("Enter your full name: ")
                    address = input("Enter your current address: ")
                    phone = int(input("Enter your phone number: "))
                    citizenship_no = input("Enter your Passport/Citizenship Number: ")
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            first_loop = True
            list=[]
            while first_loop:
                Read.display(allDict)
                while True:
                    try:
                        kittaNum = input("Enter the Kitta Number you want to rent: ")
                    except ValueError as ex:
                        print("Enter numeric value")
                    else:
                        if kittaNum in allDict:
                            print()
                            break
                        else:
                            print("error")
                while True:
                    try:
                        anna = input("Enter the number of anna you want to rent: ")
                        val=int(anna)
                    except ValueError as ex:
                        print("Enter numeric value")
                    else:
                        if val <= int(allDict[kittaNum][3]):
                            break
                        else:
                            print("error")

                while True:
                    duration = input("Enter the duration you wan to rent(In Months): ")
                    try:
                        int(duration)
                        break
                    except ValueError as ex:
                        print("Enter numeric value")

                Operation.dictionary_check(option,kittaNum,anna,allDict)
                Write.main_write(allDict)
                first_loop =Operation.loop()
                Operation.add_list(allDict,kittaNum,anna,list,duration)
                random_int = random.randint(0,100)
                Write.bill_write_sell(name, address, phone, first_loop,list,random_int)
                Write.bill_write_text(name, address, phone, first_loop, list, random_int)
            print("Thankyou for buying laptops")
            print("\n")
        elif option==2:
            name = input("Enter your full name: ")
            first_loop = True
            list = []
            while first_loop:
                Read.display(allDict)
                while True:
                    try:
                        kittaNum = input("Enter the Kitta Number you want to rent: ")
                    except ValueError as ex:
                        print("Enter numeric value")
                    else:
                        if kittaNum in allDict:
                            print()
                            break
                        else:
                            print("error")
                while True:
                    try:
                        anna = input("Enter the number of anna you want to rent: ")
                        val = int(anna)
                    except ValueError as ex:
                        print("Enter numeric value")
                    else:
                        if val <= int(allDict[kittaNum][3]):
                            break
                        else:
                            print("error")

                while True:
                    duration = input("Enter the duration you wan to rent(In Months): ")
                    try:
                        int(duration)
                        break
                    except ValueError as ex:
                        print("Enter numeric value")
                date_input = input("Please enter the date when you rented (YYYY-MM-DD format): ")
                try:
                    # Convert the input date to a datetime object
                    input_date = datetime.strptime(date_input, "%Y-%m-%d")
                    # Get the current date
                    current_date = datetime.now()
                    # Calculate the difference between the current date and the input date
                    difference = current_date - input_date
                except ValueError:
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                if difference.days>(duration*30):
                    print("Exceeded Limit Time!!!!")
                    fine = difference.days - (duration*30)
                    if fine<=30:
                        fine_value = 10000
                    if fine>30:
                        fine_value = 20000
                Operation.dictionary_check(option,kittaNum,anna,allDict)
                Write.main_write(allDict)
                first_loop = Operation.loop()
                Operation.add_list_return(allDict, kittaNum, anna, list,duration)
                random_val= random.randint(0, 100)
                Write.bill_write_rent_return(name, first_loop, list, random_val,fine_value)
                Write.bill_write_rent_return_write(name, first_loop, list, random_val, fine_value)
            print("\n")
        elif option==3:
            loop = False
            print("Thankyou for using our system")
            print("\n")
        else:
            print("Your option",option,"does not seem to match as per our requirement")
            print("\n")

main()