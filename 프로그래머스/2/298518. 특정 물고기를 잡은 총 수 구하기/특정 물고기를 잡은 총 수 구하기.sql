-- 코드를 작성해주세요
select count(*) as fish_count
from fish_info as fi join fish_name_info as fni on fi.fish_type = fni.fish_type
where fni.fish_name in ('SNAPPER','BASS')