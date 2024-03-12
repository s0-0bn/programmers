-- 코드를 입력하세요
SELECT AO.ANIMAL_ID, AO.ANIMAL_TYPE, AO.NAME
FROM ANIMAL_OUTS AO LEFT JOIN ANIMAL_INS AI ON AO.ANIMAL_ID = AI.ANIMAL_ID
WHERE AI.SEX_UPON_INTAKE<>AO.SEX_UPON_OUTCOME
ORDER BY AO.ANIMAL_ID;

select ao.animal_id, ao.animal_type, ao.name
from animal_outs ao join animal_ins ai using(animal_id)
where ai.sex_upon_intake <> ao.sex_upon_outcome
order by ao.animal_id