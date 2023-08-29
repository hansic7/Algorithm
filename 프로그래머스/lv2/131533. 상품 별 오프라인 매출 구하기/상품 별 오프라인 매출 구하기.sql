-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(o.sales_amount* p.price) as SALES
from product p join offline_sale o
on p.product_id = o.product_id
group by p.product_id
order by sales desc, p.product_code


# # SELECT p.PRODUCT_CODE, o.sales_amount* p.price as SALES
# select *
# from product p join offline_sale o
# where p.product_id = o.product_id
# group by p.product_id
# # order by sales desc, p.product_code
# order by p.product_code

