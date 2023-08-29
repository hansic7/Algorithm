-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID , date_format(OUT_DATE, "%Y-%m-%d") as OUT_DATE,
CASE
When out_date <= '2022-05-01' Then "출고완료"
when out_date > '2022-05-01' Then "출고대기"
else '출고미정'
end '출고여부'
from food_order
order by order_id