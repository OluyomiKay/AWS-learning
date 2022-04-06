select Name, Mark, Grade,
row_number() over(partition by Grade order by Mark) 'Rank'
from university.students;