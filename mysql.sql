
-- 1. 모든 도서의 이름과 가격을 검색하시오.
select bookname, price from book;

-- 2. 모든 도서의 도서번호,  도서이름, 출판사, 가격을 검색하시오.
select * from book;

-- 3. 도서 테이블에 있는 모든 출판사를 검색하시오.(중복을 제거)
select distinct publisher from book;

-- 4. 가격이 20,000원 미만인 도서를 검색하시오.
select * from book where price < 20000;

-- 5. 가격이 10,000원 이상 20,000 이하인 도서를 검색하시오.
select * from book where price <= 20000 and price >= 10000;

-- 6. 출판사가 ‘굿스포츠’ 혹은 ‘대한미디어’인 도서를 검색하시오.
select * from book where publisher = '대한미디어' or publisher = '굿스포츠';

-- 7. 도서이름에 ‘축구’가 포함된 출판사를 검색하시오.
select * from book where bookname like '%축구%';

-- 8. 도서이름의 왼쪽 두 번째 위치에 ‘구’라는 문자열을 갖는 도서를 검색하시오.
select * from book where bookname like '_구%';

-- 9. 축구에 관한 도서 중 가격이 20,000원 이상인 도서를 검색하시오.
select * from book where bookname like '%축구%' having price >= 20000;

-- 10. 출판사가 ‘굿스포츠’ 혹은 ‘대한미디어’인 도서를 검색하시오.
select * from book where publisher = '대한미디어' or publisher = '굿스포츠';

-- 11. 도서를 이름순으로 검색하시오.
select * from book order by bookname;

-- 12. 도서를 가격순으로 검색하고, 가격이 같으면 이름순으로 검색하시오.
select * from book order by price, bookname;

-- 13. 도서를 가격의 내림차순으로 검색하시오. 만약 가격이 같다면 출판사의 오름차순으로 검색한다.
select * from book order by price desc, publisher;

select * from orders;

-- 14. 고객이 주문한 도서의 총 판매액을 구하시오.
select sum(saleprice) as '총 판매액' from orders;

-- 15. 2번 김연아 고객이 주문한 도서의 총 판매액을 구하시오.
select sum(saleprice) as '총 판매액' from orders 
	group by custid
	having custid = 2;

-- 16. 고객이 주문한 도서의 총 판매액, 평균값, 최저가, 최고가를 구하시오.
select sum(saleprice) as '총 판매액', AVG(saleprice)as '평균값', 
min(saleprice) as '최저가', max(saleprice) as '최고가' from orders;

-- 17. 서점의 도서 판매 건수를 구하시오.
select max(orderid) as '도서 판매 건수' from orders;

-- 18. 고객별로 주문한 도서의 총 수량과 총 판매액을 구하시오.
select custid , count(*) as '총 수량',  sum(saleprice) as '총 판매액' from orders 
	group by custid;
    select * from orders;

-- 19. 가격이 8,000원 이상인 도서를 구매한 고객에 대하여 고객별 주문 도서의 총 수량을 구하시오. 
--     단, 두 권 이상 구매한 고객만 구한다.

select custid , count(*) as '총 수량' from orders where saleprice >= 8000
	group by custid
    having count(*) >= 2;