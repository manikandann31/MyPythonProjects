--Problem 1: Student Course Progress Timeline
select student_name,e.enroll_date,
    ROW_NUMBER() OVER(
        PARTITION BY s.student_id
        ORDER BY date(e.enroll_date)
        ) as erl
from courses as c 
JOIN enrollments as e 
    on c.course_id=e.course_id
JOIN students as s 
    on s.student_id=e.student_id;
--Problem 2: Category-wise Enrollment Ranking
WITH student_erl as (
select s.student_name,e.enroll_date,c.category,
ROW_NUMBER() over (
    PARTITION BY c.category
    ORDER BY date(e.enroll_date)
    ) as erl
from students as s 
JOIN enrollments as e 
 on s.student_id=e.student_id 
JOIN courses as c 
    on c.course_id=e.course_id 
)
select student_name,enroll_date,category,erl
from student_erl
where erl=1;

SELECT s.student_id,
    s.student_name,
    c.course_name,
    e.enroll_date,
--to mcalculate previous enrollment date
    lag(e.enroll_date) OVER (
        PARTITION BY s.student_id
        ORDER BY date(e.enroll_date)
        ) AS previous_enrollment,
--to find days between consecutive enrollmwent per student 
    julianday (e.enroll_date)-
    julianday (lag(e.enroll_date) OVER (
        PARTITION BY s.student_id
        ORDER BY date(e.enroll_date)
        )) AS days_between_enrollments
from students as s 
JOIN enrollments as e 
 on s.student_id=e.student_id 
JOIN courses as c 
    on c.course_id=e.course_id 