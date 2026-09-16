# Write your MySQL query statement below
select name, sum(amount) as balance
from Users
INNER JOIN Transactions on Users.account = Transactions.account
group by name
having sum(amount) > 10000