-- 코드를 작성해주세요
SELECT 
    CASE WHEN D.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') 
    AND D.SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY LIKE '%Front%') THEN 'A'
    WHEN D.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') THEN 'B'
    WHEN D.SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End') THEN 'C'
    END AS GRADE, D.ID, D.EMAIL FROM DEVELOPERS AS D
HAVING GRADE IS NOT NULL
ORDER BY GRADE, D.ID