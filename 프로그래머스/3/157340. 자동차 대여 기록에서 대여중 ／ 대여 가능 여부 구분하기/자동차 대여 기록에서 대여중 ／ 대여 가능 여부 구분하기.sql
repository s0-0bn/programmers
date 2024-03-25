-- 코드를 입력하세요
SELECT car_id, 
        if (sum('2022-10-16' between start_date and end_date)=0,'대여 가능','대여중') as availabilty

from car_rental_company_rental_history
group by car_id
order by car_id desc