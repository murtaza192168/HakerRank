--Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
--City TAble is as followed..
--https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg

SELECT *
FROM CITY
WHERE POPULATION > 100000 AND COUNTRYCODE  = 'USA';
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

--Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

SELECT NAME
FROM CITY
WHERE COUNTRYCODE='USA' AND POPULATION > 120000;
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

--Query all columns for a city in CITY with the ID 1661.

SELECT *
FROM CITY
WHERE ID = 1661;
------------------------------------------------------------------------------------------------------------------------------------------------------------------

--Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

SELECT *
FROM CITY
WHERE COUNTRYCODE = 'JPN';
---------------------------------------------------------------------------------------------------------------------------------------------------------------
--Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';
------------------------------------
--************************Aggregate Functions**********************
--Query a count of the number of cities in CITY having a Population larger than .



--The CITY table is described as follows: CITY.jpg
SELECT COUNT(DISTINCT ID)
FROM CITY
WHERE POPULATION > 100000;
-------------------------------:-:----
--Query the total population of all cities in CITY where District is California.

SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';
-----------------------------------------
--Query the average population of all cities in CITY where District is California.
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';
-----------------------------------------------
--Query the average population for all cities in CITY, rounded down to the nearest integer.
SELECT ROUND(AVG(POPULATION), 0) as avg_population
FROM CITY;
-------------------------
--Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN';
-------------------------:---:-------------
--Query the difference between the maximum and minimum populations in city

SELECT MAX(POPULATION) - MIN(POPULATION) AS POPULATION_DIFFERENCE
FROM CITY;
