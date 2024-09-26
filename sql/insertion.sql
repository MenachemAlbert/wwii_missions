insert into countries (country_name)
select distinct target_country
from mission
where target_country is not null
on conflict (country_name) do nothing;


insert into cities (city_name, country_id)
select distinct
    m.target_city,
    c.country_id
from mission m
join countries c on m.target_country = c.country_name
where m.target_city is not null
on conflict (city_name) do nothing;


INSERT INTO locations (latitude, longitude, city_id)
SELECT DISTINCT
    m.target_latitude,
    m.target_longitude,
    ci.city_id
FROM mission m
JOIN cities ci ON m.target_city = ci.city_name
WHERE m.target_latitude IS NOT NULL AND m.target_longitude IS NOT NULL
ON CONFLICT (city_id) DO NOTHING;


insert into target_types (target_type_name)
select distinct target_type
from mission
where target_type is not null
on conflict (target_type_name) do nothing;


insert into industry (industry_name)
select distinct target_industry
from mission
where target_industry is not null
on conflict (industry_name) do nothing;


insert into targets (location_id, target_type_id, industry_id, target_priority)
select distinct
    l.location_id,
    tt.target_type_id,
    i.industry_id,
    m.target_priority::integer
from mission m
join cities ci on m.target_city = ci.city_name
join locations l on l.city_id = ci.city_id
join target_types tt on m.target_type = tt.target_type_name
join industry i on m.target_industry = i.industry_name
where m.target_id is not null and m.target_priority is not null
on conflict (target_id) do nothing;
