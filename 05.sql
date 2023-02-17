/*
Задание 05:
Выведите все уникальные бренды товаров в алфавитном порядке.
*/

SELECT
    DISTINCT brand
FROM
    products
ORDER BY
    brand;
