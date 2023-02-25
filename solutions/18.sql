/*
Мы хотим изучить, в какие дни у нас было больше всего продаж.
Выведите пары дата - количество продаж в те дни, когда их было больше 186000.
*/

SELECT
    *
FROM(
        SELECT
            sale_date,
            COUNT(sale_id) sale_count
        FROM
            sales
        GROUP BY
            sale_date
    ) subq
WHERE
    subq.sale_count > 186000;
