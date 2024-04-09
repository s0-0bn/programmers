-- 코드를 입력하세요
with tab as (
    select host_id
    from places
    group by host_id
    having count(host_id)>1
)

SELECT id, name, host_id
from places
where host_id in (select host_id from tab)
order by id