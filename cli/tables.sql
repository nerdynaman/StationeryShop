create table Session(
    SessionID int NOT NULL AUTO_INCREMENT,
    CartValue int NOT NULL DEFAULT 0,
    PRIMARY KEY (SessionID)
);
create table Accounts(
    AccountID int NOT NULL AUTO_INCREMENT,
    Name varchar(40) NOT NULL,
    EmailID varchar(100) NOT NULL UNIQUE,
    Password varchar(30) NOT NULL,
    PhoneNumber BIGINT NOT NULL,
    Address1 varchar(50) NOT NULL,
    Address2 varchar(50),
    Pincode int NOT NULL,
    SessionID int UNIQUE,
    IsEmployee bit NOT NULL DEFAULT 0,
    PRIMARY KEY (AccountID),
    FOREIGN KEY (SessionID) REFERENCES Session(SessionID)
);
create table Membership(
    MembershipID int NOT NULL AUTO_INCREMENT,
    MembershipType varchar(20) NOT NULL UNIQUE,
    NumberOfMembers int NOT NULL DEFAULT 0,
    Discount float NOT NULL DEFAULT 0,
    Benefits varchar(200),
    PRIMARY KEY (MembershipID)
);
create table Users(
    AccountID int NOT NULL UNIQUE,
    MembershipID int NOT NULL,
    MembershipStartDate date NOT NULL,
    MembershipEndDate date NOT NULL,
    PRIMARY KEY (AccountID),
    FOREIGN KEY (MembershipID) REFERENCES Membership(MembershipID),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);
create table Employee(
    AccountID int NOT NULL UNIQUE,
    Salary int NOT NULL DEFAULT 0,
    isSalaryCredited bit NOT NULL DEFAULT 0,
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);
create table Tag(
    TagID int NOT NULL AUTO_INCREMENT,
    TagName varchar(50) NOT NULL,
    PRIMARY KEY (TagID)
);
create table Category(
    CategoryID int NOT NULL AUTO_INCREMENT,
    Name varchar(50) NOT NULL,
    Tag1 int ,
    Tag2 int ,
    Tag3 int,
    PRIMARY KEY (CategoryID),
    -- FOREIGN KEY (Tag1,Tag2,Tag3) REFERENCES Tag(TagID)
    FOREIGN KEY (Tag1) REFERENCES Tag(TagID),
    FOREIGN KEY (Tag2) REFERENCES Tag(TagID),
    FOREIGN KEY (Tag3) REFERENCES Tag(TagID)
);
create table Discount(
    MembershipID int NOT NULL,
    CategoryID int NOT NULL,
    Percentage float NOT NULL DEFAULT 0,
    PRIMARY KEY (MembershipID,CategoryID),
    FOREIGN KEY (MembershipID) REFERENCES Membership(MembershipID),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);
create table Product(
    ProductID int NOT NULL AUTO_INCREMENT,
    CategoryID int NOT NULL,
    Name varchar(30) NOT NULL,
    Cost int NOT NULL,
    Description varchar(200) NOT NULL,
    Discount float NOT NULL DEFAULT 0,
    Rating float NOT NULL DEFAULT 0,
    Quantity int NOT NULL,
    Tag1 int ,
    Tag2 int ,
    Tag3 int,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    -- FOREIGN KEY (Tag1,Tag2,Tag3) REFERENCES Tag(TagID)
    FOREIGN KEY (Tag1) REFERENCES Tag(TagID),
    FOREIGN KEY (Tag2) REFERENCES Tag(TagID),
    FOREIGN KEY (Tag3) REFERENCES Tag(TagID)
);
create table Review(
    ReviewID int NOT NULL AUTO_INCREMENT,
    ProductID int NOT NULL,
    Rating int NOT NULL DEFAULT 0,
    Content varchar(300),
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
create table CartItem(
    SessionID int NOT NULL,
    ProductID int NOT NULL,
    Quantity int NOT NULL DEFAULT 1,
    PRIMARY KEY (SessionID,ProductID),
    FOREIGN KEY (SessionID) REFERENCES Session(SessionID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);