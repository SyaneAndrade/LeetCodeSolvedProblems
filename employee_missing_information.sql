# Write your MySQL query statement below
(SELECT Emp.employee_id
    FROM Employees AS Emp LEFT JOIN Salaries AS Sal
    ON Emp.employee_id = Sal.employee_id
    WHERE Sal.employee_id is NULL
UNION 
SELECT Sal.employee_id 
    FROM Salaries AS Sal LEFT JOIN Employees AS Emp
    ON Sal.employee_id = Emp.employee_id
    WHERE Emp.employee_id is NULL)
ORDER BY employee_id