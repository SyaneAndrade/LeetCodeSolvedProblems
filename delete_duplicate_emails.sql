/* Please write a DELETE statement and DO NOT write a SELECT statement.
  Write your MySQL query statement below*/
 DELETE FROM PERSON
    WHERE id NOT IN (
        SELECT MinID FROM(
            SELECT email, min(id) AS MinID
            FROM Person
            GROUP BY email
            ) email_duplicate
        )