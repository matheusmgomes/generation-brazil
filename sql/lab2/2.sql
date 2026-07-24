SELECT Products.ProductName, SUM(Orders.Quantity) AS TotalQuantity
FROM Orders
JOIN Products ON Orders.ProductId = Products.ProductId
GROUP BY Products.ProductName
ORDER BY SUM(Orders.Quantity) DESC
LIMIT 1;