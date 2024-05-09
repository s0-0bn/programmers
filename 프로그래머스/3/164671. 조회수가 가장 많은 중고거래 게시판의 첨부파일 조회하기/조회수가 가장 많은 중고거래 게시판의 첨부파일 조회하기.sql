-- 코드를 입력하세요
select concat("/home/grep/src/",ugf.board_id,"/",ugf.file_id,ugf.file_name,ugf.file_ext)as file_path
from used_goods_board as ugb 
    join used_goods_file as ugf using(board_id)
where views = (select max(views)
               from used_goods_board)
order by file_id desc