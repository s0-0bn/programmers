-- 코드를 작성해주세요
select item_id, item_name, rarity
from item_info
where item_id in (select it.item_id 
from item_tree it right join (select * from item_info where rarity = 'RARE') as rare 
on it.parent_item_id = rare.item_id
where it.item_id is not null)
order by item_id desc
