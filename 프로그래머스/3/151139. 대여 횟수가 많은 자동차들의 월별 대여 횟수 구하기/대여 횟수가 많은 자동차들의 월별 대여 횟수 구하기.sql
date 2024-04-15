-- 코드를 입력하세요
with car as(
    select car_id
    from car_rental_company_rental_history
    where month(start_date) between 8 and 10
    group by car_id
    having count(car_id) >= 5
)

select month(start_date) as month , car_id, count(car_id) as RECORDS
from car_rental_company_rental_history
where month(start_date) between 8 and 10
    and car_id in (select * from car)
group by month(start_date), car_id
having RECORDS >0
order by month asc , car_id desc