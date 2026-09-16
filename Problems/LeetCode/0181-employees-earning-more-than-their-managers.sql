# Write your MySQL query statement below
SELECT e.name as Employee
FROM Employee AS e
JOIN Employee AS m ON e.managerID=m.id
WHERE e.salary > m.salary 