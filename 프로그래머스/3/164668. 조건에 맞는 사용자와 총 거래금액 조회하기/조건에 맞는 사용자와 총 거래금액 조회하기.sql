-- 코드를 입력하세요
select user_id, nickname, sum(price) as total_sales
from used_goods_board ugb join used_goods_user ugu 
    on ugb.writer_id = ugu.user_id
where ugb.status = 'DONE' 
group by writer_id
having total_sales>=700000
order by total_sales














