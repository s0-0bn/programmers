-- 코드를 작성해주세요
with parent_id as (
    select distinct parent_item_id
    from item_tree
    where parent_item_id is not null )
    
select item_id, item_name, rarity
from item_info
where item_id not in (select * from parent_id)
order by item_id desc