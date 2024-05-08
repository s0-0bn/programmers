-- 코드를 작성해주세요
with maxsize as (
    select year(differentiation_date) as year_s,max(size_of_colony) as max_size
    from ecoli_data
    group by year_s),
year_ecoli as (
    select year(differentiation_date) as year_s, id, size_of_colony
    from ecoli_data)

select ye.year_s as year, (ms.max_size-ye.size_of_colony) as year_dev, ye.id
from year_ecoli ye join maxsize ms using (year_s)
order by ye.year_s, year_dev