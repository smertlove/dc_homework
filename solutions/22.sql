/*
Посчитайте количество однофамильцев для каждой фамилии.
Выведите колонки surname, n, где n - это название колонки с количеством людей.
*/

SELECT
    surname, COUNT(name) n
FROM
    customers
GROUP BY
    surname;
