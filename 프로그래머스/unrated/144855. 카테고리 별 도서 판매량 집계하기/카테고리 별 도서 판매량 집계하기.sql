-- 코드를 입력하세요
SELECT category,sum(sales) as total_sales

FROM BOOK B,BOOK_SALES bS

where sales_date like "2022-01%" and b.book_id = bs.book_id
group by category
order by category