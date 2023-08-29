-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME
from animal_ins i join animal_outs o
where i.animal_id = o.animal_id and i.datetime >= o.datetime
order by i.datetime


# SELECT I.ANIMAL_ID, I.NAME 
# FROM ANIMAL_INS AS I JOIN ANIMAL_OUTS AS O 
# WHERE I.ANIMAL_ID = O.ANIMAL_ID AND O.DATETIME <= I.DATETIME 
# ORDER BY I.DATETIME