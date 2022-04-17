import qrcode
from pyfiglet import Figlet
f = Figlet(font='standard')
print(f.renderText('Arash Store'))
#######################################
PRODUCTS = []
#######################################
def load():
    print('loading...')
    myfile = open("database.txt","r")
    data = myfile.read()
    product_list=data.split('\n')
    for i in range(len(product_list)):
        product_info=product_list[i].split(',')
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = product_info[3]
        PRODUCTS.append(mydict)
    print('welcome')
#######################################
def show_menu():
    print('1-Add Product')
    print('2-Edit Product')
    print('3-Delete Product')
    print('4-search')
    print('5-show list')
    print('6-Buy')
    print('7-show Product info by qrcode')
#######################################-1
def add_product():
    Item= open("database.txt", "a")    
    Item = input("enter id Item:")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    productDict = {}
    productDict['id'] = Item
    productDict['name'] = name
    productDict['price'] = int(price)
    productDict['count'] = int(count)
    PRODUCTS.append(productDict)
    print(PRODUCTS)
#######################################-2
def Edit_Product():
    toole_mahsol = 0
    name = input("choose name: ")
    while toole_mahsol < len(PRODUCTS):
        if PRODUCTS[toole_mahsol]['name'] == name:
            OP = input("choose change: I.id P.Price C.Count: ")
            if OP =='I':
                id = int(input("New id: "))
                PRODUCTS[toole_mahsol]['id']= id
            elif OP == 'P':
                Price = int(input("New Price: "))
                PRODUCTS[toole_mahsol]['price']= Price
            elif OP == 'C':
                count = int(input("New count: "))
                PRODUCTS[toole_mahsol]['count'] = count
            break            
        toole_mahsol=toole_mahsol+1        
    
#######################################-3
def delet_product():
    id= int(input("enter id :"))
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]["id"]==id:
            PRODUCTS.pop(i)
    print("Done")     
#######################################-4
def search_product():
        name = input("search by name :")
        for i in range(len(PRODUCTS)):
           if PRODUCTS[i]['name'] == name:
            print(PRODUCTS[i]) 
        print(" Done ")
#######################################-5
def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
#######################################-6 
def shopping():

    show_list()
    tedad_kharid = 0 
    while True :
        a=int(input("1.shopping  2.payment: "))  
        if a == 1:             
            id=input("please enter Product_id: ")

            for i in range (len(PRODUCTS)):
                if PRODUCTS[i]['id'] == id :
                    print('Name: ' , PRODUCTS[i]['name'])
                    print('Price: ', PRODUCTS[i]['price'])
                    count = int(input("che tedad mikhay: "))
                    if count <=int(PRODUCTS[i]['count']):
                        PRODUCTS[i]['count']= int(PRODUCTS[i]['count'])- count  
                        kharid = count * int(PRODUCTS[i]['price'])                       
                        tedad_kharid =kharid + tedad_kharid
                        print("ezafe shod")
                    else:
                        print("bishtar az mojodi ")
                        print("meghdar mojod : ", PRODUCTS[i]['count'])
        if a==2:  
            break          
    print('mablaghe kharid: ' ,tedad_kharid )
#######################################-7
def code():
     id=int(input("Enter id: "))
     for i in range (len(PRODUCTS)):
         if PRODUCTS[i]['id']==id :
             img=qrcode.make(PRODUCTS[i]['name'] + PRODUCTS[i]['price'] + PRODUCTS[i]['count'])
             img.save('qrcode.png')        
#######################################
load()
show_menu()
choice = int(input("please choose a number: "))
#######################################
if choice == 1:
    add_product()
elif choice == 2:
    Edit_Product()
elif choice == 3:
    delet_product()
elif choice == 4:
    search_product()
elif choice == 5:
    show_list()
elif choice == 6:
    shopping()
elif choice == 7:
    pass   