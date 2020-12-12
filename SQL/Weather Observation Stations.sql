--Query a list of CITY and STATE from the STATION table.
--The STATION table is described as follows: https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg
SELECT CITY, STATE
FROM STATION;
---------------------------------------------------------------------

--Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.


SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2)=0;
-----------------------------------------------------------------------------------------------------------------------------------------------

--Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
SELECT   (COUNT(CITY) - COUNT(DISTINCT CITY) ) AS DIFFERENCE
FROM STATION;
------------------------------------------------------------------------------------------------------------------------------------
--Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths
--(i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that 
--comes first when ordered alphabetically.

SELECT  CITY,LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY), CITY ASC
LIMIT 1;

 SELECT CITY, LENGTH(CITY)
 FROM STATION
 ORDER BY LENGTH(CITY) DESC
LIMIT 1;

---------------------------------------------------------------------------------------------------------------------------------------
--Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates
SELECT DISTINCT CITY 
FROM STATION

WHERE CITY RLIKE '^[AEIOU]';   --This is the MySql keyword i.e. 'RLIKE' for pattern matching 
-------------------------------------------
