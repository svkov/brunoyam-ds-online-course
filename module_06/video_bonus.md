# План

1. Показываю как и откуда установить SQLite Studio
2. Показываю как создать свою базу данных, заполнить таблички
3. Выводим имена и классы учеников старше 2008 года
4. Считаем сколько учеников в каждом классе
5. Для каждого класса найдем младшего ученика
6. Объясняю как строится рейтинг учеников
    * Создаем временную таблицу с суммой оценок за каждый день
    * Объясняю, что строки пропущены, готовим таблицу со всеми учениками и оценками
    * Считаем кумулятивную сумму
    * Определяем номер ученика в рейтинге за каждый день, складываем во временную таблицу
    * Выбираем топ-1

```sql
WITH rating_table(date, student_id, cumsum) AS (
    WITH aggregated_marks(date, student_id, points) AS (
        WITH dates_and_students(date, student_id, name) AS (
            SELECT DISTINCT date(datetime) as date, student.id as student_id, name FROM mark, student
        )
    
        SELECT dates_and_students.date, dates_and_students.student_id, SUM(value) as points FROM dates_and_students
        LEFT JOIN mark ON date(mark.datetime) == dates_and_students.date AND mark.student_id == dates_and_students.student_id
        GROUP BY dates_and_students.date, dates_and_students.student_id
    )
        
    SELECT date, student_id, SUM(points) over w as cumsum FROM aggregated_marks
    WINDOW w AS (PARTITION BY student_id ORDER BY date)
)

SELECT date, student_id FROM (
    SELECT date, student_id, DENSE_RANK() OVER w as rating FROM rating_table
    WINDOW w AS (PARTITION BY date ORDER BY cumsum DESC)
) WHERE rating == 1
```
