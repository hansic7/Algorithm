-- 코드를 입력하세요
SELECT animal_id, name, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜 
from animal_ins
order by animal_id