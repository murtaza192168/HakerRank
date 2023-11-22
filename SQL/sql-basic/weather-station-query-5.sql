(SELECT DISTINCT CITY, LENGTH(CITY) AS CITY_LEN
FROM STATION
ORDER BY CITY_LEN ASC
LIMIT 1)
UNION
(
SELECT DISTINCT CITY, LENGTH(CITY) AS CITY_LEN
FROM STATION
ORDER BY CITY_LEN DESC
LIMIT 1
);
