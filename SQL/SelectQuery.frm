--Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
--City TAble is as followed..
--https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg

SELECT *
FROM CITY
WHERE POPULATION > 100000 AND COUNTRYCODE  = 'USA';

