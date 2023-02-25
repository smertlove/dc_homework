
/*
Выведите все уникальные имена клиентов, фамилия которых Джигурда.
*/


SELECT DISTINCT
    name
FROM
    customers
WHERE
    surname LIKE 'Джигурда';
