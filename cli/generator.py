import random
import datetime
import names
import secrets

accountNames = [names.get_full_name() for i in range(100)]
accountEmailIDs = ["".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=7)) + "@gmail.com" for i in range(100)]
accountPasswords = [secrets.token_hex(8) for i in range(100)]
accountPhoneNumbers = [random.randint(1000000000,9999999999) for i in range(100)]
accountAddress1 = [" ".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10)) for i in range(100)]
accountAddress2 = [" ".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10)) for i in range(100)]
accountPincode = [random.randint(100000,999999) for i in range(100)]
accountSessionID = [i for i in range(1,101)]
isEmployee = [random.randint(0,1) for i in range(100)]


for i in range(100):
    print("insert into Accounts(Name,EmailID,Password,PhoneNumber,Address1,Address2,Pincode,SessionID,IsEmployee) values('{}','{}','{}',{},'{}','{}',{},NULL,{});".format(accountNames[i],accountEmailIDs[i],accountPasswords[i],accountPhoneNumbers[i],accountAddress1[i],accountAddress2[i],accountPincode[i],isEmployee[i]))

for i in range(100):
    print("insert into Session(CartValue) values(0);")

for i in range(100):
    print("insert into Membership(MembershipType,NumberOfMembers,Discount,Benefits) values('{}',0,0,'{}');".format("".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10)),"".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10))))

for i in range(100):
    if isEmployee[i]:
        print("insert into Employee(AccountID,Salary,isSalaryCredited) values({},0,0);".format(i+1))
    else:
        print("insert into Users(AccountID,MembershipID,MembershipStartDate,MembershipEndDate) values({},1,'{}','{}');".format(i+1,datetime.date.today(),datetime.date.today()+datetime.timedelta(days=365)))

for i in range(100):
    print("insert into Tag(TagName) values('{}');".format("".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10))))

for i in range(100):
    print("insert into Category(Name,Tag1,Tag2,Tag3) values('{}',{},NULL,NULL);".format("".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10)),i+1))

for i in range(100):
    print("insert into Discount(MembershipID,CategoryID,Percentage) values({},{},{});".format(i+1, random.randint(1,100), random.randint(1,100)))

for i in range(100):
    print("insert into Product(CategoryID,Name,Cost,Description,Discount,Rating,Quantity,Tag1,Tag2,Tag3) values(1,'{}',{},'{}',0,0,0,NULL,NULL,NULL);".format("".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10)),random.randint(100,1000)," ".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10))))

for i in range(100):
    print("insert into Review(ProductID,Rating,Content) values(1,0,'{}');".format(" ".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=10))))

for i in range(100):
    print("insert into CartItem(SessionID,ProductID,Quantity) values({},1,1);".format(i+1))
