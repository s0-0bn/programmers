-- 코드를 작성해주세요
# select item_id, item_name, rarity
# from item_info
# where item_id in (select it.item_id 
#                   from item_tree it right join (select * 
#                                               from item_info 
#                                               where rarity = 'RARE') as rare 
#                                     on it.parent_item_id = rare.item_id
#                   where it.item_id is not null)
# order by item_id desc;


SELECT i.ITEM_ID, i.ITEM_NAME, i.RARITY
FROM ITEM_INFO i
WHERE i.ITEM_ID IN (SELECT t.ITEM_ID 
                    FROM ITEM_TREE t 
                    WHERE t.PARENT_ITEM_ID IN ( SELECT i.ITEM_ID 
                                               FROM ITEM_INFO i 
                                               WHERE i.RARITY = 'RARE')) 
ORDER BY i.ITEM_ID desc;