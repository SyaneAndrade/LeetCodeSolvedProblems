/* Write your MySQL query statement below*/

Update Salary 
SET sex =  case
                when sex = 'm' then 'f'
                when sex = 'f' then 'm'
                else null
                end