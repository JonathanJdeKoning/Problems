# Write your MySQL query statement below
SELECT firstName,lastName, city, state
FROM Person
LEFT JOIN ADDRESS
on Person.personId = Address.personId
