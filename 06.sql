/*
Задание 06:
Мы хотим оценить, какой объем персональных предложений планировать на следующий год.
Выведите customer_id и дату рождения клиентов, отсортированные по дате рождения без учета года
(от 1 января до 31 декабря).
*/

SELECT
    customer_id, birth_date
FROM
    customers
ORDER BY
    EXTRACT(MONTH FROM birth_date),
    EXTRACT(DAY FROM birth_date);
