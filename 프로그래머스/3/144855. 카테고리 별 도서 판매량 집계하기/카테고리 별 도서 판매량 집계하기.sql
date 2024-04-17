-- 코드를 입력하세요
SELECT b.category, sum(bs.sales) as total_sales
from book as b join book_sales as bs using(book_id)
where date_format(bs.sales_date,'%Y-%m') = '2022-01'
group by b.category
order by b.category