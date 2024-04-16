-- 코드를 작성해주세요
select sum(hg.score) as score, hg.emp_no, he.emp_name, he.position, he.email
from hr_grade as hg join hr_employees as he using (EMP_NO)
group by hg.emp_no
order by sum(hg.score) desc
limit 1