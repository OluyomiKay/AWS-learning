select Name, Mark, Grade,
rank() over(partition by Grade order by Mark) 'Rank'
from university.students;
