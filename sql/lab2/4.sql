SELECT OrderDate, COUNT(OrderId) AS OrderCount
FROM Orders
GROUP BY OrderDate;