-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, date_format(START_DATE,'%Y-%m-%d'), date_format(END_DATE,'%Y-%m-%d'), if(datediff(end_date,start_date)>=29,'장기 대여','단기 대여') as rent_type
from car_rental_company_rental_history
where year(start_date)=2022 and month(start_date)=9 
order by history_id desc