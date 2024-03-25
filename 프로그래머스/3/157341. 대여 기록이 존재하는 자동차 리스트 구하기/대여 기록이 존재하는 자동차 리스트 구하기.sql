-- 코드를 입력하세요
SELECT distinct(crcr.car_id)
from car_rental_company_car as crcr join car_rental_company_rental_history as crcrh
    using (car_id)
where month(crcrh.start_date)=10 and crcr.car_type='세단'
order by crcr.car_id desc