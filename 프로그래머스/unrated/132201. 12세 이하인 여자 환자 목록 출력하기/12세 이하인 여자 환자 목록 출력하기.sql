-- 코드를 입력하세요
SELECT 	PT_NAME,	PT_NO,GEND_CD,	AGE, ifnull(TLNO, 'NONE') as 'TLNO'
from patient
where gend_cd = 'W' and age <= 12
order by age DESC ,pt_name 