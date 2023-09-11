-- 코드를 입력하세요
SELECT PRODUCT_CODE, sum(sales_amount * price) SALES
# SELECT *
from product p join offline_sale o
on p.product_id = o.product_id
group by product_code
order by sales DESC, product_code