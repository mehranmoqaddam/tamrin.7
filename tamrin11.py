products = []
sheet = open("productss" , mode ="r+")
for line in sheet:
    result = line.split("-")
    my_dict = {"id":result[0],"name":result[1],"price":result[2],"quantity":result[3]}
    products.append(my_dict)

def add():

    id = input("Enter id: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity: ")
    new_product = {"id":id,"name":name,"price":price,"quantity":quantity}
    products.append(new_product)
    sheet.write(id+"-"+name+"-"+price+"-"+quantity+"-"+"\n")
    print("New product has been successfully added.")

def delete():
    code = int(input("Enter item's index to delete it: "))
    product = products.pop(code - 1)
    print("Selected product has been successfully removed.")

def edit():
    edited = input("Enter item's id to edit: ")
    for product in products:
        if product["id"] == edited:
            print("1.Name")
            print("2.price")
            print("3.Count")

            edited_part = int(input("Your choice: "))
            if edited_part == 1:
                new_name = input("Enter new name for item: ")
                product["name"] = new_name
                print("successfully edited.")

            elif edited_part == 2:
                new_price = input("Enter the new price :")
                product["price"] = new_price
                print("successfully edited.")

            elif edited_part == 3:
                new_quantity = input("Enter the new count :")
                product["quantity"] = new_quantity
                print("successfully edited.")

def search():
    s = input("Enter your keyword : ")
    for product in products:
        if product["id"] == s or product["name"] == s:
            print(product)
            break
    else:
        print("the product you've been searched is not found!")

def show_list():

    for i in enumerate(products, start=1):
        print(i)

def buy():
    invoice = []
    cost = 0
    while True:
        print("yes or no :")
        yes = input("Would you want to make a purchase? ")
        if yes == "yes":
            selected_id = input("Enter item's id: ")
            for product in products:
                if product["id"] == selected_id:
                    quan = int(input("Enter your quantity: "))
                    cost += quan*int(product["price"])
                    if int(product["quantity"]) >= quan:
                        purchasedproduct = {product["name"] , str(quan)}
                        invoice.append(purchasedproduct)
                        product["quantity"] = str(int(product["quantity"])-quan)
                        break
                    elif int(product["quantity"]) < quan:
                        print("Unfortunately,this quantity of this product is not available!")
                        break
            else:
                print("Unfortunately,this product is not in stock!!")

        elif yes == "no":
            print("--thank you for visiting us--")
            print("-----your invoice-----")
            for item in invoice:
                print(item)
            print("cost is: ",cost)
            print("-----see you again-----")
            break

def show_menu():

    print("1- Add")
    print("2- Delete")
    print("3- Edit")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- Exit")

show_menu()
while True:
    operation = int(input("Enter your operation: "))

    if operation == 1:
        add()
    if operation == 2:
        show_list()
        delete()
        show_list()
    if operation == 3:
        show_list()
        edit()
    if operation == 4:
        search()
    if operation == 5:
        show_list()
    if operation == 6:
        show_list()
        buy()
    if operation == 7:
        exit(0)
    show_menu()