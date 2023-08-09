-- 코드를 입력하세요
SELECT animal_type, count(*) as count 
from animal_ins
group by animal_type 
having animal_type = 'Cat' or animal_type = 'Dog'
order by animal_type