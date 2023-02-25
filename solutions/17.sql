/*
Выведите средннюю цену каждого товара за 2020 год в виде product_id - avg_price,
где avg_price - это название колонки со средней ценой.
Отсортируйте выборку в порядке возрастания product_id.
*/

SELECT
    product_id,
    AVG(price) avg_price
FROM
    prices
GROUP BY
    product_id
ORDER BY
    product_id;
