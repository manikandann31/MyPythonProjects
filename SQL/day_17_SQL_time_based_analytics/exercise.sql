--1.how many enrollmenrts hapen each month 
select 
    strftime('%Y-%m',enroll_date) as enroll_month, 
    count(*) as No_of_enrolls
from enrollments
group by enroll_month
order by enroll_month;

--2.MoM ANALYSIS 
with monthly_data as (
SELECT 
    strftime('%Y-%m',e.enroll_date) as enroll_month,  --STRFTIME is a function used in sqlite to extract month and year from the enroll date from the enrollments table 
    COUNT(*) AS monthly_enrollments
FROM enrollments e
JOIN courses c 
    ON c.course_id = e.course_id
GROUP BY enroll_month
ORDER BY enroll_month
)
SELECT 
    enroll_month,
    monthly_enrollments,
    lag(monthly_enrollments)over(
        order by enroll_month) AS previous_month,               --growth is not only a total its a copmparison between previous count and current count so we have to subract the current count with the previous count to get the growth by month 
    monthly_enrollments-lag(monthly_enrollments)over(
        order by enroll_month) AS growth
from monthly_data
ORDER BY enroll_month;
--3.category wise monthly trend
with monthly_data as (
SELECT c.category,
    strftime('%Y-%m',enroll_date) as enroll_month,
    count(*) as no_of_enrolls
from enrollments as e 
JOIN courses as c 
    on e.course_id=c.course_id
group by c.category,enroll_month
order by enroll_month,c.category
)
SELECT 
    category,
    enroll_month,
    no_of_enrolls,
    lag(no_of_enrolls)over(
        PARTITION BY category
        order by enroll_month) AS previous_month,               --growth is not only a total its a copmparison between previous count and current count so we have to subract the current count with the previous count to get the growth by month 
    no_of_enrolls-lag(no_of_enrolls)over(
        PARTITION BY category
        order by enroll_month) AS growth
from monthly_data
ORDER BY category,enroll_month;

--First Month vs Latest Month Performance

with monthly_data as (                             --1st CTE to collect the count of enroll per category per month 
SELECT c.category,
        strftime('%Y-%m',e.enroll_date) as enroll_month,
        count(*) as no_of_enrolls
from enrollments as e 
JOIN courses as c 
    on c.course_id=e.course_id
group by c.category,enroll_month
),
month_bounds as (                                  --2nd CTE which find the first enroll month and last enroll month 
select category,
        enroll_month,
        no_of_enrolls,
        first_value(enroll_month) over (
            PARTITION BY category 
            ORDER BY enroll_month
            ) as first_month,
        last_value(enroll_month) over (
            PARTITION BY category
            ORDER BY enroll_month
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
            ) as last_month
from monthly_data
)
SELECT *
FROM month_bounds
WHERE enroll_month IN (first_month, last_month)
ORDER BY category, enroll_month;



