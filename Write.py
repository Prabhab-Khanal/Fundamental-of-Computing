import datetime

def main_write(dict):
    file = open("D:\Study\CW\ggg.txt", "w")
    for i in dict.values():
        file.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) )
        file.write("\n")
    file.close()

def bill_write_sell(name,address,phone,loop,list,random):
    if loop != True:
        print("Bill no: ", random)
        print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"), "\t\t\tDate: ",
            datetime.datetime.now().strftime(" %d/%m/%Y"), "\n")
        print("\t\t\t","Name: ", name, "\n")
        print("Address: ", address, "\t\t\t\tPhone: ", phone)
        total = 0
        totalAnna=0

        print("S.n\t\t", "Anna Number\t\t", "City/District\t\t\t", "Facing\t\t","Duration(Months)\t\t", "Anna\t\t", "Price\t\t" ,"Total Price")
        for i in range(len(list)):
            price_one = int(list[i][5])
            duration = int(list[i][3])
            price = price_one * duration * int(list[i][3])
            print(i+1,"\t\t",list[i][0],"\t\t",list[i][1],"\t\t",list[i][2],"\t\t",list[i][3],"\t\t\t\t",list[i][4],"\t\t\t",list[i][5],"\t\t\t",price)
            total = total + price
            totalAnna = totalAnna + int(list[i][3])
        print("\t\t\t\t\t\tTotal Cost: ", total)
        print("\t\t\t\t\t\tTotal Anna: ", totalAnna)

def bill_write_text(name,address,phone,loop_1,list,random):
    if loop_1 != True:
        files = open(f"{random}.txt", "w")
        files.write(f"Bill no:  {random}\n")
        date = datetime.datetime.now().strftime(" %d/%m/%Y")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        files.write(f"Time: {time} \t\t\tDate: {date}\n")

        files.write(f"\t\t\t Name:  {name} \n")
        files.write(f"Address: {address} \t\t\t\tPhone: {phone}\n")
        total = 0
        totalAnnas = 0
        files.write(f"S.n\t\t Anna Number\t\t City/District\t\t\t Facing\t\t Anna\t\t Price\n")
        price =0
        for i in range(len(list)):
            price_one = int(list[i][5])
            duration = int(list[i][3])
            price = price_one * duration * int(list[i][3])
            files.write(f"{i + 1} \t\t {list[i][0]} \t\t {list[i][1]} \t\t {list[i][2]}\t\t {list[i][3]} \t\t\t\t{list[i][4]} \t\t{list[i][5]} \t\t{price}\n")
            total = total + price
            totalAnnas = totalAnnas + int(list[i][4])
        files.write(f"\t\t\t\t\t\tTotal Cost:  {total}\n")
        files.write(f"\t\t\t\t\t\tTotal Annas:  {totalAnnas}\n")

def bill_write_rent_return(name, loop_1, list, random, fine):
    if loop_1 != True:
        print("Bill no: ", random)
        print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"), "\t\t\tDate: ",
              datetime.datetime.now().strftime(" %d/%m/%Y"), "\n")
        print("\t\t\t","Name: ", name, "\n")
        totalAnna =0
        total = 0
        print("S.n\t\t", "Anna Number\t\t", "City/District\t\t\t", "Facing\t\t", "Duration\t\t", "Anna\t\t", "Price")
        for i in range(len(list)):
            price_one = int(list[i][5])
            duration = int(list[i][3])
            price = price_one * duration
            print(i + 1, "\t\t", list[i][0], "\t\t", list[i][1], "\t\t", list[i][2], "\t\t", list[i][3], "\t\t\t\t",
                  list[i][4], "\t\t\t", list[i][5], "\t\t\t", price)
            total = total + price
            totalAnna = totalAnna + int(list[i][3])
        print("\t\t\t\t\t\tTotal Cost: ", total)
        print("\t\t\tAnna: ", totalAnna)
        with_fine= total + fine
        print("You have exceed the time period so you need to pay a fine of Rs",fine)
        print("\t\t\t\t\t\tTotal Cost: ", with_fine)

def bill_write_rent_return_write (name, loop_1, list, random, fine):
        file =open(f"{random}.txt", "w")
        if loop_1 != True:
            file.write("Bill no: {}\n".format(random))
            file.write("Time: {} \t\t Date: {}\n\n".format(
                datetime.datetime.now().strftime("%H:%M:%S"),
                datetime.datetime.now().strftime(" %d/%m/%Y")))
            file.write("\t\t\t Name: {}\n\n".format(name))
            total_anna = 0
            total = 0
            file.write("S.n\t\t Anna Number\t\t City/District\t\t\t Facing\t\t Duration\t\t Anna\t\t Price\n")
            i=0
            for i in range(len(list)):
                file.write(
                    f"{i + 1} \t\t {list[i][0]} \t\t {list[i][1]} \t\t {list[i][2]}\t\t {list[i][3]} \t\t\t\t{list[i][4]}\n")
                total = total + int(list[i][4])
                totalAnnas = totalAnnas + int(list[i][3])
            file.write("\t\t\t\t\t\t Total Cost: {}\n".format(total))
            file.write("\t\t\t Anna: {}\n".format(total_anna))
            with_fine = total + fine
            file.write("You have exceeded the time period so you need to pay a fine of Rs {}\n".format(fine))
            file.write("\t\t\t\t\t\t Total Cost with Fine: {}\n".format(with_fine))
