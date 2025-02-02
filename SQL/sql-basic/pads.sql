SELECT CONCAT(NAME, '(' , SUBSTR(OCCUPATION,1,1), ')')
FROM OCCUPATIONS
ORDER BY NAME ASC; 

SELECT CONCAT('There are a total of',' ', COUNT(OCCUPATION),' ', lower(OCCUPATION), 's.' ) as PROFESSION
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY PROFESSION ASC;
