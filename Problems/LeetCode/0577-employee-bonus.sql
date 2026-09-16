# Write your MySQL query statement below
select e.name as name, b.bonus as bonus
from Employee as e
left join Bonus as b on e.empID=b.empID
having (b.bonus < 1000 or b.bonus is null)