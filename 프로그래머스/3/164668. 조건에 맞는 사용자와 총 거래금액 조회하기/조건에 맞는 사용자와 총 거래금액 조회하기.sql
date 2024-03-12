-- 코드를 입력하세요
SELECT ugu.user_id, ugu.nickname, sum(ugb.price) as total_sales
FROM USED_GOODS_USER as ugu join USED_GOODS_BOARD as ugb on ugb.writer_id=ugu.user_id
where ugb.status = 'DONE'
group by ugb.writer_id
having total_sales >= 700000
order by total_sales asc