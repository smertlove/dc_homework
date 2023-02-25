/*
Выведите все уникальные customer_id покупателей,
которые совершали покупки в феврале 2020 года, в порядке возрастания.
*/

SELECT DISTINCT
    customer_id
FROM
    sales
WHERE
    sale_date BETWEEN '2020-02-01' AND '2020-02-29'
ORDER BY
    customer_id;
