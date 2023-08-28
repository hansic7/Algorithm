-- 코드를 입력하세요
SELECT mcdp_cd as `진료과코드`, count(pt_no) as `5월예약건수`
from appointment 
where APNT_YMD like "2022-05%"
group by mcdp_cd
# having month(APNT_YMD) = "5"
order by 5월예약건수, 진료과코드
;



# SELECT apnt_no from appointment 
# where month(apnt_ymd) = "05";