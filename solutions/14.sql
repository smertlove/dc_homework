/*
Мы хотим сделать акцию к международному дню буквы К и оценить, сколько покупателей могут праздновать этот день.
Выведите все customer_id, имена и фамилии покупателей, у которых имя или фамилия начинаются с буквы К (кириллицей).
*/

SELECT
    customer_id,
    name,
    surname
FROM
    customers
WHERE
    name LIKE 'К%'
    AND
    surname LIKE 'К%';