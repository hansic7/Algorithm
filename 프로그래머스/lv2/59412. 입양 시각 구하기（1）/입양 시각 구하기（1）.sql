-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, 
count(animal_id) as COUNT 
from animal_outs
group by hour
having hour >= 9 and 19 >= hour
order by hour;