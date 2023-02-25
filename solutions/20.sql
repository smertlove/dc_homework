/*
Выведите количество продаж по месяцам в 2020 году.
Формат вывода: двузначный номер месяца - количество продаж.
*/

SELECT
    EXTRACT(MONTH FROM sale_date) sale_month,
    COUNT(sale_id)
FROM
    sales
GROUP BY
    sale_month;
