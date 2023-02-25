/*
Посчитайте количество магазинов в регионе 5.
Выведите единственное число.
*/

SELECT
    COUNT(store_id)
FROM
    stores
WHERE
    region = 5;
