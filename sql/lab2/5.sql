SELECT Customers.CustomerName, SUM(Orders.Total) AS TotalSales
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY Customers.CustomerName
ORDER BY TotalSales DESC
LIMIT 3;