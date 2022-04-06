select CountryCode, sum(Population) 'Total'
from world.city
where Population >= 5000000
group by CountryCode with rollup
having sum(Population) >= 8000000
order by CountryCode limit 10;
