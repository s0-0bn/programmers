-- 코드를 입력하세요
with sample as (
select rf.rest_id, rf.rest_name, rf.food_type, 
        rf.favorites, rf.address,round(avg(rr.review_score),2) as score
from rest_info as rf join rest_review as rr using (rest_id)
group by rf.rest_id
order by avg(rr.review_score) desc, rf.favorites desc)

select *
from sample
where address like "서울%"