/*
Выведите все данные по ценам,
которые действовали в течение февраля 2020 года (учтите оба поля start_date и end_date).
*/

SELECT
    *
FROM
    prices
WHERE
    start_date >= '2020-02-01' AND end_date < '2020-03-01';
