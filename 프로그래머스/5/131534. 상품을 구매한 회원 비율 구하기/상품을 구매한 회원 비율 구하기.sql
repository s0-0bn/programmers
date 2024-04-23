-- 코드를 입력하세요
SELECT year(os.sales_date) as year, month(os.sales_date) as month,
        count(distinct(ui.user_id)) as puchased_users, 
        round(count(distinct(ui.user_id))/
              (select count(distinct(user_id)) 
               from user_info 
               where joined like '2021%'),1) as puchased_ratio
from user_info as ui right join online_sale as os 
                            on ui.user_id=os.user_id and ui.joined like '2021%'
group by year, month
order by year, month;