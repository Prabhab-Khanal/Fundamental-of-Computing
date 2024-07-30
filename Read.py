def header():
    print("\n")  # enter ek line tala janxa
    print("\n")
    print("\t \t \t \t \t TechnoPropertyNepal")  # one tab space
    print("\n")
    print("\t \t \t \t  Kathmandu| 98696996969")
    print("\n")

    print("----------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t Welcome to our store, and we are glad to you are here!!")
    print("----------------------------------------------------------------------------------------------------------")
    print("\n")

def display(dict):
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    print("Kitta No\t\tCity/District\t\t\tLand Facing\tAnna\t\tPrice\tAvailability Status")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    file = open("D:\Study\CW\ggg.txt")
    a = 1
    for i in dict.values():
        if int(i[3])>0:
            status = "Available"
        else:
            status = "Not Available"
        print(i[0],"\t\t",i[1],"\t\t",i[2],"\t\t",i[3],"\t\t",i[4],"\t\t",status)
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

def dictionary():
    land = {}
    files = open('D:\Study\CW\ggg.txt', 'r')
    lines = files.readlines()
    l = 0
    for i in lines:
        a = lines[l].strip().split(",")
        print(a)
        l = l + 1
        x = a[0]
        land[x] = a
    print(land)
    return land
