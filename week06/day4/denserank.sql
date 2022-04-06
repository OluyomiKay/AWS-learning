select Name, Mark, Grade,
dense_rank() over(partition by Grade order by Mark) 'Rank'
from university.students;