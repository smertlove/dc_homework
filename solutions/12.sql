/*
Выведите все пары product_id - store_id, которые купили зарегистрированные пользователи 14 февраля 2020 года.
*/

SELECT
    product_id, store_id
FROM
    sales
WHERE
    sale_date = '2020-02-14' AND customer_id IS NOT NULL;
