/*
Выведите количество дней, в которые количество продаж было больше 186000.
*/

SELECT
    COUNT(sale_date) day_count
FROM
    (
        SELECT
            sale_date,
            COUNT(sale_id) sale_count
        FROM
            sales
        GROUP BY
            sale_date
        HAVING
            COUNT(sale_id) > 186000
    ) subq;
