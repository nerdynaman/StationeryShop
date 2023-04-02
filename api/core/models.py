from django.db import models
# Create your models here.


"""Database Schema:
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
    FOREIGN KEY (Tag1) REFERENCES Tag(TagID) on delete cascade on update cascade,
    FOREIGN KEY (Tag2) REFERENCES Tag(TagID) on delete cascade on update cascade,
    FOREIGN KEY (Tag3) REFERENCES Tag(TagID) on delete cascade on update cascade
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
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID) on delete cascade on update cascade,
    -- FOREIGN KEY (Tag1,Tag2,Tag3) REFERENCES Tag(TagID)
    FOREIGN KEY (Tag1) REFERENCES Tag(TagID) on delete cascade on update cascade,
    FOREIGN KEY (Tag2) REFERENCES Tag(TagID) on delete cascade on update cascade,
    FOREIGN KEY (Tag3) REFERENCES Tag(TagID) on delete cascade on update cascade
);
create table Review(
    ReviewID int NOT NULL AUTO_INCREMENT,
    ProductID int NOT NULL,
    Rating int NOT NULL DEFAULT 0,
    Content varchar(300),
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) on delete cascade on update cascade
);"""
class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    CategoryID = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cost = models.IntegerField()
    description = models.CharField(max_length=200)
    discount = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    quantity = models.IntegerField()
    tag1 = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='tag1', null=True)
    tag2 = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='tag2', null=True)
    tag3 = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='tag3', null=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    TagID = models.AutoField(primary_key=True)
    TagName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.TagName
    
class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    content = models.CharField(max_length=300)
    
    def __str__(self):
        return self.content
    