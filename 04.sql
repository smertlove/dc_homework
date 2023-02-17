/*
Задание 04:
Мы хотим создать карту, в какие магазины ходит каждый конкретный покупатель.
Выберите все пары customer_id, store_id для этого.
*/

SELECT
    DISTINCT customer_id, store_id
FROM
    sales;
