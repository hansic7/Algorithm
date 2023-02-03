select * from Customer;
select * from orders;
select * from book;

select * from Imported_Book;

-- 20. 고객과 고객의 주문에 관한 데이터를 모두 보이시오.
select * 
	from Customer 
		inner join orders;

-- 21. 고객과 고객의 주문에 관한 데이터를 고객번호 순으로 정렬하여 보이시오.
select * 
	from Customer C
		inner join orders O
	order by c.custid;

-- 22. 고객의 이름과 고객이 주문한 도서의 판매가격을 검색하시오.
select o.orderid, c.name, o.saleprice
	from orders O
		inner join Customer C 
			on o.custid = c.custid
    order by o.orderid;

-- 23 고객별로 주문한 모든 도서의 총 판매액을 구하고, 고객별로 정렬하시오.
select name, sum(saleprice) as '총 판매액'
from orders, customer
where orders.custid = customer.custid
group by name
order by name;

-- 24. 고객의 이름과 고객이 주문한 도서의 이름을 구하시오.
select name, bookname
from orders, customer, book
where Orders.custid = customer.custid and orders.bookid = book.bookid ;

-- 25. 가격이 20,000원인 도서를 주문한 고객의 이름과 도서의 이름을 구하시오.
select name, bookname
from orders, customer, book
where Orders.saleprice = 20000 
	and  Orders.custid = customer.custid
     and orders.bookid = book.bookid ;

-- 26. 도서를 구매하지 않은 고객을 포함하여 고객의 이름과 고객이 주문한 도서의 판매가격을 구하시오.
select o.orderid,name, o.saleprice
	from orders O
		right outer join customer C
			on O.custid = c.custid;

-- 27. 가장 비싼 도서의 이름을 보이시오.
select bookname, price as '가장비싼도서'
from book
where price = (select max(price) from book);

-- 28. 도서를 구매한 적이 있는 고객의 이름을 검색하시오.
select distinct name
from orders o 
	right outer join customer c
		on O.custid = c.custid
	where orderid is not null;
    
select name from customer
where custid in (select custid from orders);

-- 29. 대한미디어에서 출판한 도서를 구매한 고객의 이름을 보이시오.
select name
from customer
where custid in (select custid from orders where bookid  in (select bookid from book where publisher = '대한미디어'));

-- 30. 출판사별로 출판사의 평균 도서 가격보다 비싼 도서를 구하시오.
select b1.bookname
from book b1
where price > (select avg(price) from book b2 where b1.publisher = b2.publisher);

-- 31. 주문이 있는 고객의 이름과 주소를 보이시오. 
