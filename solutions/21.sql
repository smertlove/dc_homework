/*
Выведите самый популярный product_id среди незарегистрированных клиентов.
*/

SELECT
    product_id
FROM
    sales
WHERE
    customer_id IS NULL
GROUP BY
    product_id
ORDER BY
    COUNT(sale_id)
LIMIT
    1;
