select name as customers from Customers
where id NOT IN (
    Select customerId from Orders
);