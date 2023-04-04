select productid from (SELECT ProductID, SessionID
FROM ((select distinct(SessionID) from cartitem) as s cross join (select ProductID from product) as pi)
EXCEPT (SELECT ProductID,SessionID FROM cartitem)) as a

select category.Name,count(product.ProductID) from category,product
where category.categoryID = product.categoryID
group by category.Name with rollup

SELECT
CONCAT('Q', QUARTER(MembershipEndDate)) AS Quarter,
COUNT(*) AS MembershipCount FROM Users
GROUP BY Quarter WITH ROLLUP

SELECT 
CONCAT('Q', QUARTER(Users.MembershipEndDate))
AS Quarter, COUNT(*) 
AS NumUsers 
FROM Users JOIN Accounts ON Users.AccountID = Accounts.AccountID 
WHERE Accounts.SessionID IS NOT NULL GROUP BY Quarter WITH ROLLUP;

create trigger updateQuantity 
after insert
on cartItem
for each row
begin
update product set Quantity = Quantity - new.quantity where productID = new.productID;
end

create trigger deleteCartItem
after delete
on cartItem
for each row
begin
update product set Quantity = Quantity + old.quantity where productID = old.productID;
end