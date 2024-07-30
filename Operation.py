def dictionary_check(option, kitta, anna, land):
    if option == 1:
        for i in land.keys():
            if kitta == i:
                annas = int(land[kitta][3])
                if annas == 0:
                    print("Sorry currently the land is unavailable for renting please contact later!!!!")
                    print("\n")

                if int(anna) <= annas:
                    land[kitta][3] = annas - int(anna)

                if int(anna)>annas:
                    print("Sorry check the values!!!!")
    elif option == 2:
        for i in land.keys():
            if kitta == i:
                annas = int(land[kitta][3])
                land[kitta][3] = annas + anna

def loop():
    con = True
    while con:
        ask = input("Do you want to continue(y/n):  ")
        if ask.lower() == "n":
            a= False
            con = False
            return a
        elif ask.lower() == "y":
            a= True
            con = False
            return a
        else:
            print("Enter proper values")

def add_list(dict, kitta, anna, list, duration):
    annaNo = kitta
    kitta = str(kitta)
    li = dict[kitta]
    city = li[1]
    facing = li[2]
    totalanna = anna
    price = int(li[4])
    if li[3]!='0':
        list.append([annaNo, city, facing, duration,totalanna, price])

def add_list_return(dict,code,quantity,list,duration):
    annaNo = code
    code=str(code)
    li=dict[code]
    city = li[1]
    facing=li[2]
    totalanna = quantity
    price = int(li[4])
    # list=[annaNo, c_name, price, quantity, t_price]
    list.append([annaNo, city, facing, duration,totalanna, price])



