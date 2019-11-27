-- Select all cities and state with LEFT JOIN
SELECT cities.id, cities.name, states.name
FROM cities
         INNER JOIN states on cities.state_id = states.id;
