SELECT Customers.CustomerName, SUM(Orders.Total) AS TotalSales
FROM Orders
JOIN Customers ON Customers.CustomerId = Orders.CustomerId
GROUP BY Customers.CustomerName;