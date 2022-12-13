# Write your MySQL query statement below

SELECT *
     FROM (
        SELECT product_id,
           store,
           CASE 
            WHEN store = 'store1' THEN store1
            WHEN store = 'store2' THEN store2
            WHEN store = 'store3' THEN store3
           END AS price
        FROM Products CROSS JOIN
        (
            SELECT 'store1' AS store
            UNION ALL
            SELECT 'store2'
            UNION ALL
            SELECT 'store3'
        ) AS Stores
     ) AS UnpivotedProducts
     WHERE price IS NOT NULL
     ORDER BY price