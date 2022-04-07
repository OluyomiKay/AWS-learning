select Name, Mark, Grade,
ntile(6) over(partition by Grade order by Mark) 'Rank'
from university.students;