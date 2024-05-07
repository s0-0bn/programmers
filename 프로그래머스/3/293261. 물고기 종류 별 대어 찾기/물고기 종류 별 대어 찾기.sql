with a as (
    select fish_type, max(length)
    from fish_info
    group by fish_type
)

select fi.id, fni.fish_name, fi.length
from fish_info as fi join fish_name_info as fni using (fish_type)
where (fish_type, length) in (select * from a)
order by fi.id 