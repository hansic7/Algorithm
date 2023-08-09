-- 코드를 입력하세요
SELECT DR_NAME,	DR_ID,	MCDP_CD	, date_format(HIRE_YMD, '%Y-%m-%d') as HIRE_YMD
from doctor
where mcdp_cd = 'CS' or mcdp_cd = 'gS'
order by hire_ymd DESC, dr_name