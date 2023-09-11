-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from animal_ins i
join animal_outs o

on i.animal_id = o.animal_id 

where (SEX_UPON_INTAKE not like "Neutered%" and SEX_UPON_INTAKE not like "Spayed%") and (SEX_UPON_OUTCOME like "Neutered%" or SEX_UPON_OUTCOME like "Spayed%")

order by animal_id