/*
Выведите все уникальные адреса магазинов региона 5 в алфавитном порядке.
*/

SELECT DISTINCT
    address
FROM
    stores
WHERE
    region = 5
ORDER BY
    address;
