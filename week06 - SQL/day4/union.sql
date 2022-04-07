select Name,Code, Population
from world.country
where Population > 10000000
union all
select Name, CountryCode, Population
from world.city
where Population > 8000000;