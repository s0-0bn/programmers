-- 코드를 입력하세요

with box as (select shipment_id, flavor, total_order
from first_half
union
select shipment_id, flavor, total_order
from july)

select flavor
from box
group by flavor
order by sum(total_order) desc
limit 3