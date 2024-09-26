--query 1

SELECT air_force,target_city,  COUNT(*) AS active_missions
FROM  mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
GROUP BY air_force, target_city
ORDER BY  active_missions DESC
LIMIT 1

--

EXPLAIN ANALYZE SELECT air_force,target_city,  COUNT(*) AS active_missions
FROM  mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
GROUP BY air_force, target_city
ORDER BY  active_missions DESC
LIMIT 1


--

CREATE INDEX idx_mission_date_year ON mission (EXTRACT(YEAR FROM mission_date));

--

DROP INDEX IF EXISTS idx_mission_date_year;


-- query 2


select bomb_damage_assessment , count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country ,bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1

--

EXPLAIN ANALYZE select bomb_damage_assessment , count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country ,bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1


--

CREATE INDEX idx_mission_performance ON mission (airborne_aircraft, bomb_damage_assessment, target_country);

--

DROP INDEX IF EXISTS idx_mission_performance;



