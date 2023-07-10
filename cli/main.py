import mysql.connector
import hashlib
# connect to mysql database
host = ""
user = ""
password = ""
mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password
)
# create cursor
mycursor = mydb.cursor()
mycursor.execute("use dbmsNew")

def userLogin(mycursor):
    registered = input("Are you registered user? (y/n) : ")
    if registered == 'n':
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        # encrypt password
        password = hashlib.md5(password.encode()).hexdigest()[:30]
        phoneNumber = input("Enter your phone number : ")
        address = input("Enter your address line 1: ")
        address2 = input("Enter your address line 2: ")
        pincode = input("Enter your pincode : ")
        admin = input("Are you an admin? (y/n) : ")
        mycursor.execute("insert into accounts(Name,EmailID,Password,PhoneNumber,Address1,Address2,Pincode,isemployee) values ('{}','{}','{}','{}','{}','{}','{}',{})".format(name,email,password,phoneNumber,address,address2,pincode,admin))
        if int(admin) == 0:
            print("You have been registered successfully! with membership\n")
            mycursor.execute("insert into users(accountid,membershipid,MembershipStartDate,MembershipEndDate) values ((select max(accountid) from accounts),1,curdate(),date_add(curdate(),interval 1 year))")
            mydb.commit()
        mydb.commit()
        print("You have been registered successfully!\n")
        userLogin(mycursor)

    else:
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        password = hashlib.md5(password.encode()).hexdigest()[:30]
        mycursor.execute("select * from accounts where EmailID = '{}' and Password = '{}'".format(email,password))
        account = mycursor.fetchall()
        if len(account) == 0:
            print("Invalid email or password")
            userLogin(mycursor)
            return False
        adminStatus = account[0][9]
        print("Login successful")
        # check if session already exists
        if account[0][8] == None:
            mycursor.execute("insert into session() values() ")
            mycursor.execute("update accounts set SessionID = (select max(SessionID) from session) where EmailID = '{}'".format(email))
            mydb.commit()

        if adminStatus == 1:
            print("Admin pannel")
            adminMenu(mycursor)
            return True
        else:
            print("User pannel")
            userMenu(mycursor,sessionID=account[0][8])
            return True
        
def userMenu(mycursor,sessionID):
    print("1. View all Categories")
    print("2. View all Products")
    print("3. View Cart Items")
    print("4. Add to Cart")
    print("5. Remove from Cart")
    print("6. Checkout")
    print("7. Logout")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        mycursor.execute("select * from category")
        for categories in mycursor.fetchall():
            for elements in categories:
                print(elements,end=" ")
            print()
        print()
        userMenu(mycursor,sessionID)
        return False
    elif choice == 2:
        mycursor.execute("select * from product")
        for products in mycursor.fetchall():
            for elements in products:
                print(elements,end=" ")
            print()
        print()
        userMenu(mycursor,sessionID)
        return False
    elif choice == 3:
        mycursor.execute("select * from cartItem where SessionID = {}".format(sessionID))
        product = mycursor.fetchall()
        if len(product) == 0:
            print("Cart is empty")
            userMenu(mycursor,sessionID)
            return False
        for cart in product:
            mycursor.execute("select Name from product where ProductID = {}".format(cart[1]))
            prodName = mycursor.fetchall()[0][0]
            print("product name: ",prodName," quantity: ",cart[2])
            print()
        print()
        userMenu(mycursor,sessionID)
        return False
    elif choice == 4:
        productID = input("Enter product ID : ")
        quantity = int(input("Enter quantity : "))
        mycursor.execute("select * from product where productID = {}".format(productID))
        product = mycursor.fetchall()
        if len(product) == 0 or int(quantity) > int(product[0][7]):
            print("Invalid product ID or quantity")
            userMenu(mycursor,sessionID)
            return False
        else:
            # check if product already exists in cart
            mycursor.execute("select * from cartItem where ProductID = {} and SessionID = {}".format(productID,sessionID))
            product = mycursor.fetchall()
            if len(product) != 0:
                mycursor.execute("update cartItem set quantity = quantity + {} where ProductID = {} and SessionID = {}".format(quantity,productID,sessionID))
                mydb.commit()
                print("Product quantity updated successfully!\n")
                userMenu(mycursor,sessionID)
                return False
            mycursor.execute("insert into cartItem(SessionID,ProductID,quantity) values ({},{},{})".format(sessionID,productID,quantity))
            mydb.commit()
            print("Product added to cart successfully!\n")
            userMenu(mycursor,sessionID)
            return False
    elif choice == 5:
        productID = input("Enter product ID : ")
        mycursor.execute("select * from cartItem where ProductID = {} and SessionID = {}".format(productID,sessionID))
        product = mycursor.fetchall()
        if len(product) == 0:
            print("Invalid product ID")
            userMenu(mycursor,sessionID)
            return False
        else:
            mycursor.execute("delete from cartItem where ProductID = {} and SessionID = {}".format(productID,sessionID))
            mydb.commit()
            print("Product removed from cart successfully!\n")
            userMenu(mycursor,sessionID)
            return False
    elif choice == 6:
        mycursor.execute("select * from cartItem where SessionID = {}".format(sessionID))
        cartItems = mycursor.fetchall()
        if len(cartItems) == 0:
            print("Cart is empty")
            userMenu(mycursor,sessionID)
        else:
            mycursor.execute("START Transaction")
            priceTotal = 0
            for cartItem in cartItems:
                mycursor.execute("select cost from product where ProductID = {}".format(cartItem[1]))
                price = mycursor.fetchall()[0][0]
                priceTotal += price*cartItem[2]
                # mycursor.execute("delete from cartItem where SessionID = {} and ProductID = {}".format(sessionID,cartItem[1]))
                mycursor.execute("update cartitem set quantity = 0 where ProductID = {} and sessionid = {}".format(cartItem[1],sessionID))
            print("Total price : ",priceTotal)
            mydb.commit()
            mycursor.execute("COMMIT")

def adminMenu(mycursor):
    print("1. Add new Category")
    print("2. View all Categories")
    print("3. Add new Product")
    print("4. Delete product")
    print("5. View all products")
    print("6. Logout")
    print("7. view all products which are not in all cart")
    print("8. view total number of products in each category")
    print("9. view membership ending quaterwise")
    print("10. view membership ending quarterwise for active customers")
    # what could be example of rollup query

    choice = int(input("Enter your choice : "))
    if choice == 1:
        categoryName = input("Enter category name : ")
        mycursor.execute("insert into category(Name) values ('{}')".format(categoryName))
        mydb.commit()
        print("Category added successfully!\n")
        adminMenu(mycursor)
    elif choice == 2:
        mycursor.execute("select * from category")
        categories = mycursor.fetchall()
        for category in categories:
            print("Category ID: ",category[0],end=" ")
            print("Category Name: ",category[1])
        print()
        adminMenu(mycursor)
    elif choice == 3:
        categoryName = input("Enter category name : ")
        mycursor.execute("select categoryID from category where Name = '{}'".format(categoryName))
        category = mycursor.fetchall()
        if len(category) == 0:
            print("Invalid category name")
            adminMenu(mycursor)
        else:
            productName = input("Enter product name : ")
            productPrice = input("Enter product price : ")
            productQuantity = input("Enter product quantity : ")
            productDescription = input("Enter product description : ")
            mycursor.execute("insert into product(Name,Cost,Quantity,Description,CategoryID) values ('{}','{}','{}','{}',{})".format(productName,productPrice,productQuantity,productDescription,category[0][0]))
            mydb.commit()
            print("Product added successfully!\n")
            adminMenu(mycursor)
    elif choice == 4:
        productName = input("Enter product name : ")
        mycursor.execute("select * from product where Name = '{}'".format(productName))
        product = mycursor.fetchall()
        if len(product) == 0:
            print("Invalid product name")
            adminMenu(mycursor)
        mycursor.execute("delete from product where Name = '{}'".format(productName))
        mydb.commit()
        print("Product deleted successfully!\n")
        adminMenu(mycursor)
    elif choice == 5:
        mycursor.execute("select * from product")
        products = mycursor.fetchall()
        for product in products:
            print("Product ID: ",product[0],end=" ")
            print("Product Name: ",product[2],end=" ")
            print("Product Price: ",product[3],end=" ")
            print("Product Quantity: ",product[7],end=" ")
            print("Category ID: ",product[1])
            # for elements in product:
            #     print(elements,end=" ")
            # print()
        print()
        adminMenu(mycursor)
    elif choice == 6:
        # mycursor.execute("delete from session where SessionID = (select max(SessionID) from session)")
        # mydb.commit()
        print("Logout successful")
        return True
    elif choice == 7:
        mycursor.execute("select distinct(productid) from (SELECT ProductID, SessionID FROM (( select distinct(SessionID) from cartitem) as s cross join (select ProductID from product) as pi) EXCEPT (SELECT ProductID,SessionID FROM cartitem)) as a")
        products = mycursor.fetchall()
        for product in products:
            mycursor.execute("select * from product where ProductID = {}".format(product[0]))
            product = mycursor.fetchall()
            print(product[0])
        print()
        adminMenu(mycursor)
    elif choice == 8:
        mycursor.execute("select category.Name, count(product.ProductID) from category,product where category.categoryID = product.categoryID group by category.Name with rollup")
        products = mycursor.fetchall()
        for product in products:
            print(product)
        print()
        adminMenu(mycursor)
    elif choice == 9:
        mycursor.execute("SELECT    CONCAT('Q', QUARTER(MembershipEndDate)) AS Quarter,   COUNT(*) AS MembershipCount FROM    Users GROUP BY    Quarter WITH ROLLUP")
        products = mycursor.fetchall()
        for product in products:
            print(product)
        print()
        adminMenu(mycursor)
    elif choice == 10:
        mycursor.execute("SELECT CONCAT('Q', QUARTER(Users.MembershipEndDate)) AS Quarter, COUNT(*) AS NumUsers FROM Users JOIN Accounts ON Users.AccountID = Accounts.AccountID WHERE Accounts.SessionID IS NOT NULL GROUP BY Quarter WITH ROLLUP")
        products = mycursor.fetchall()
        for product in products:
            print(product)
        print()
        adminMenu(mycursor)

userLogin(mycursor)


# to be done 
# create trigger for checkout to update quantity in product table
# create trigger for checkout to delete cartItem
# create trigger for membership to be updated for user according to thei purchase history

"""
create trigger updateQuantity 
after insert
on cartItem
for each row
begin
update product set Quantity = Quantity - new.quantity where productID = new.productID;
end
"""
"""
create trigger deleteCartItem
after delete
on cartItem
for each row
begin
update product set Quantity = Quantity + old.quantity where productID = old.productID;
end
"""

#  insert into membership(membershiptype) values('first');
#  insert into membership(membershiptype) values('second');
#  insert into membership(membershiptype) values('third');