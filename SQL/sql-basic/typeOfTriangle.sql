SELECT CASE
WHEN A + B > C AND B + C > A AND A + C > B
THEN
    CASE 
        WHEN A=B AND B=C AND A=C THEN "Equilateral"
        WHEN A!=B AND A!=C AND B!=C THEN "Scalene"
        WHEN A=B OR A=C OR B=C THEN "Isosceles" END

    ELSE "Not A Triangle"
END FROM TRIANGLES
