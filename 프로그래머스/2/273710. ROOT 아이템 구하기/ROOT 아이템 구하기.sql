-- 코드를 작성해주세요
select item_id, item_name
from item_info as ii join item_tree as it using(item_id)
where it.parent_item_id is null
order by item_id