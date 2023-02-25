/*
Выведите все уникальные product_id, которые были проданы покупателю с customer_id = 69 14 февраля 2020 года.
*/

SELECT DISTINCT
    product_id
FROM
    sales
WHERE
    customer_id = 69 AND sale_date = '2020-02-14';
