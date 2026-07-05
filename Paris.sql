USE paris_road_traffic_analysis;
DROP DATABASE IF EXISTS paris_road_traffic_analysis;
CREATE DATABASE paris_road_traffic_analysis;

USE paris_road_traffic_analysis;

-- STEP 1: IMPORT TABLES

-- CHARACTERISTICS 2020 Table

CREATE TABLE characteristics_2020 (
    Num_Acc VARCHAR(20),
    jour INT,
    mois INT,
    an INT,
    hrmn VARCHAR(10),
    lum INT,
    dep VARCHAR(10),
    com VARCHAR(10),
    agg INT,
    inter INT,
    atm INT,
    col INT,
    adr TEXT,
    lat DOUBLE,
    lon DOUBLE
);

SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/caracteristiques-2020.csv'
INTO TABLE characteristics_2020
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Num_Acc, jour, mois, an, hrmn, lum, dep, com, agg, inter, atm, col, adr, @lat, @lon)
SET
    lat = REPLACE(@lat, ',', '.'),
    lon = REPLACE(@lon, ',', '.');

-- CHARACTERISTICS 2021 Table

CREATE TABLE characteristics_2021 (
    Num_Acc VARCHAR(20),
    jour INT,
    mois INT,
    an INT,
    hrmn VARCHAR(10),
    lum INT,
    dep VARCHAR(10),
    com VARCHAR(10),
    agg INT,
    inter INT,
    atm INT,
    col INT,
    adr TEXT,
    lat DOUBLE,
    lon DOUBLE
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/caracteristiques-2021.csv'
INTO TABLE characteristics_2021
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Num_Acc, jour, mois, an, hrmn, lum, dep, com, agg, inter, atm, col, adr, @lat, @lon)
SET
    lat = REPLACE(@lat, ',', '.'),
    lon = REPLACE(@lon, ',', '.');

-- CHARACTERISTICS 2022 Table

CREATE TABLE characteristics_2022 (
    Num_Acc VARCHAR(20),
    jour INT,
    mois INT,
    an INT,
    hrmn VARCHAR(10),
    lum INT,
    dep VARCHAR(10),
    com VARCHAR(10),
    agg INT,
    inter INT,
    atm INT,
    col INT,
    adr TEXT,
    lat DOUBLE,
    lon DOUBLE
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/caracteristiques-2022.csv'
INTO TABLE characteristics_2022
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Num_Acc, jour, mois, an, hrmn, lum, dep, com, agg, inter, atm, col, adr, @lat, @lon)
SET
    lat = REPLACE(@lat, ',', '.'),
    lon = REPLACE(@lon, ',', '.');

-- CHARACTERISTICS 2023 Table

CREATE TABLE characteristics_2023 (
    Num_Acc VARCHAR(20),
    jour INT,
    mois INT,
    an INT,
    hrmn VARCHAR(10),
    lum INT,
    dep VARCHAR(10),
    com VARCHAR(10),
    agg INT,
    inter INT,
    atm INT,
    col INT,
    adr TEXT,
    lat DOUBLE,
    lon DOUBLE
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/caracteristiques-2023.csv'
INTO TABLE characteristics_2023
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Num_Acc, jour, mois, an, hrmn, lum, dep, com, agg, inter, atm, col, adr, @lat, @lon)
SET
    lat = REPLACE(@lat, ',', '.'),
    lon = REPLACE(@lon, ',', '.');

-- CHARACTERISTICS 2024 Table

CREATE TABLE characteristics_2024 (
    Num_Acc VARCHAR(20),
    jour INT,
    mois INT,
    an INT,
    hrmn VARCHAR(10),
    lum INT,
    dep VARCHAR(10),
    com VARCHAR(10),
    agg INT,
    inter INT,
    atm INT,
    col INT,
    adr TEXT,
    lat DOUBLE,
    lon DOUBLE
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/caracteristiques-2024.csv'
INTO TABLE characteristics_2024
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Num_Acc, jour, mois, an, hrmn, lum, dep, com, agg, inter, atm, col, adr, @lat, @lon)
SET
    lat = REPLACE(@lat, ',', '.'),
    lon = REPLACE(@lon, ',', '.');

-- LOCATIONS 2020 Table

CREATE TABLE locations_2020 (
    Num_Acc VARCHAR(20),
    catr INT,
    voie VARCHAR(50),
    v1 VARCHAR(10),
    v2 VARCHAR(10),
    circ INT,
    nbv VARCHAR(10),
    vosp INT,
    prof INT,
    pr VARCHAR(20),
    pr1 VARCHAR(20),
    plan INT,
    lartpc DOUBLE,
    larrout DOUBLE,
    surf INT,
    infra INT,
    situ INT,
    vma INT
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/lieux-2020.csv'
INTO TABLE locations_2020
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'   -- note: this file uses \r\n, not \n!
IGNORE 1 ROWS
(Num_Acc, catr, voie, v1, v2, circ, nbv, vosp, prof, pr, pr1, plan, @lartpc, @larrout, surf, infra, situ, vma)
SET
    lartpc = NULLIF(REPLACE(@lartpc, ',', '.'), ''),
    larrout = NULLIF(REPLACE(@larrout, ',', '.'), '');

-- LOCATIONS 2021 Table

CREATE TABLE locations_2021 (
    Num_Acc VARCHAR(20),
    catr INT,
    voie VARCHAR(50),
    v1 VARCHAR(10),
    v2 VARCHAR(10),
    circ INT,
    nbv VARCHAR(10),
    vosp INT,
    prof INT,
    pr VARCHAR(20),
    pr1 VARCHAR(20),
    plan INT,
    lartpc DOUBLE,
    larrout DOUBLE,
    surf INT,
    infra INT,
    situ INT,
    vma INT
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/lieux-2021.csv'
INTO TABLE locations_2021
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'   -- changed from \r\n
IGNORE 1 ROWS
(Num_Acc, catr, voie, v1, v2, circ, nbv, vosp, prof, pr, pr1, plan, @lartpc, @larrout, surf, infra, situ, vma)
SET
    lartpc = NULLIF(REPLACE(@lartpc, ',', '.'), ''),
    larrout = NULLIF(REPLACE(@larrout, ',', '.'), '');

-- LOCATIONS 2022 Table

CREATE TABLE locations_2022 (
    Num_Acc VARCHAR(20),
    catr INT,
    voie VARCHAR(50),
    v1 VARCHAR(10),
    v2 VARCHAR(10),
    circ INT,
    nbv VARCHAR(10),
    vosp INT,
    prof INT,
    pr VARCHAR(20),
    pr1 VARCHAR(20),
    plan INT,
    lartpc DOUBLE,
    larrout DOUBLE,
    surf INT,
    infra INT,
    situ INT,
    vma INT
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/lieux-2022.csv'
INTO TABLE locations_2022
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'   -- changed from \r\n
IGNORE 1 ROWS
(Num_Acc, catr, voie, v1, v2, circ, nbv, vosp, prof, pr, pr1, plan, @lartpc, @larrout, surf, infra, situ, vma)
SET
    lartpc = NULLIF(REPLACE(@lartpc, ',', '.'), ''),
    larrout = NULLIF(REPLACE(@larrout, ',', '.'), '');

-- LOCATIONS 2023 Table

CREATE TABLE locations_2023 (
    Num_Acc VARCHAR(20),
    catr INT,
    voie VARCHAR(50),
    v1 VARCHAR(10),
    v2 VARCHAR(10),
    circ INT,
    nbv VARCHAR(10),
    vosp INT,
    prof INT,
    pr VARCHAR(20),
    pr1 VARCHAR(20),
    plan INT,
    lartpc DOUBLE,
    larrout DOUBLE,
    surf INT,
    infra INT,
    situ INT,
    vma INT
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/lieux-2023.csv'
INTO TABLE locations_2023
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'   -- changed from \r\n
IGNORE 1 ROWS
(Num_Acc, catr, voie, v1, v2, circ, nbv, vosp, prof, pr, pr1, plan, @lartpc, @larrout, surf, infra, situ, vma)
SET
    lartpc = NULLIF(REPLACE(@lartpc, ',', '.'), ''),
    larrout = NULLIF(REPLACE(@larrout, ',', '.'), '');

-- LOCATIONS 2024 Table

CREATE TABLE locations_2024 (
    Num_Acc VARCHAR(20),
    catr INT,
    voie VARCHAR(50),
    v1 VARCHAR(10),
    v2 VARCHAR(10),
    circ INT,
    nbv VARCHAR(10),
    vosp INT,
    prof INT,
    pr VARCHAR(20),
    pr1 VARCHAR(20),
    plan INT,
    lartpc DOUBLE,
    larrout DOUBLE,
    surf INT,
    infra INT,
    situ INT,
    vma INT
);

LOAD DATA LOCAL INFILE 'D:/PycharmProjects/Paris_Road_Traffic_Analysis/datasets/lieux-2024.csv'
INTO TABLE locations_2024
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'   -- changed from \r\n
IGNORE 1 ROWS
(Num_Acc, catr, voie, v1, v2, circ, nbv, vosp, prof, pr, pr1, plan, @lartpc, @larrout, surf, infra, situ, vma)
SET
    lartpc = NULLIF(REPLACE(@lartpc, ',', '.'), ''),
    larrout = NULLIF(REPLACE(@larrout, ',', '.'), '');


-- STEP 2: APPENDING TABLES

-- Appending Characteristics Tables

CREATE TABLE characteristics (
    Num_Acc VARCHAR(20),
    jour INT,
    mois INT,
    an INT,
    hrmn VARCHAR(10),
    lum INT,
    dep VARCHAR(10),
    com VARCHAR(10),
    agg INT,
    inter INT,
    atm INT,
    col INT,
    adr TEXT,
    lat DOUBLE,
    lon DOUBLE,
    year INT
);

INSERT INTO characteristics
SELECT *,
       2020 AS year
FROM characteristics_2020;

INSERT INTO characteristics
SELECT *,
       2021 AS year
FROM characteristics_2021;

INSERT INTO characteristics
SELECT *,
       2022 AS year
FROM characteristics_2022;

INSERT INTO characteristics
SELECT *,
       2023 AS year
FROM characteristics_2023;

INSERT INTO characteristics
SELECT *,
       2024 AS year
FROM characteristics_2024;

-- Appending Locations Tables

CREATE TABLE locations (
    Num_Acc VARCHAR(20),
    catr INT,
    voie VARCHAR(50),
    v1 VARCHAR(10),
    v2 VARCHAR(10),
    circ INT,
    nbv VARCHAR(10),
    vosp INT,
    prof INT,
    pr VARCHAR(20),
    pr1 VARCHAR(20),
    plan INT,
    lartpc DOUBLE,
    larrout DOUBLE,
    surf INT,
    infra INT,
    situ INT,
    vma INT,
    year INT
);

INSERT INTO locations
SELECT *,
       2020 AS year
FROM locations_2020;

INSERT INTO locations
SELECT *,
       2021 AS year
FROM locations_2021;

INSERT INTO locations
SELECT *,
       2022 AS year
FROM locations_2022;

INSERT INTO locations
SELECT *,
       2023 AS year
FROM locations_2023;

INSERT INTO locations
SELECT *,
       2024 AS year
FROM locations_2024;

-- STEP 3: DROP OLD TABLES

DROP TABLE characteristics_2020;
DROP TABLE characteristics_2021;
DROP TABLE characteristics_2022;
DROP TABLE characteristics_2023;
DROP TABLE characteristics_2024;

DROP TABLE locations_2020;
DROP TABLE locations_2021;
DROP TABLE locations_2022;
DROP TABLE locations_2023;
DROP TABLE locations_2024;

ALTER TABLE characteristics
DROP COLUMN year;

ALTER TABLE locations
DROP COLUMN year;

-- STEP 4: DATA CLEANUP

-- 1. Rename columns

ALTER TABLE characteristics
    RENAME COLUMN Num_Acc TO accident_id,
    RENAME COLUMN jour TO accident_day,
    RENAME COLUMN mois TO accident_month,
    RENAME COLUMN an TO accident_year,
    RENAME COLUMN hrmn TO accident_time,
    RENAME COLUMN lum TO lighting_conditions,
    RENAME COLUMN dep TO department_id,
    RENAME COLUMN com TO municipality_id,
    RENAME COLUMN agg TO location,
    RENAME COLUMN inter TO intersection,
    RENAME COLUMN atm TO atmospheric_conditions,
    RENAME COLUMN col TO collision_type,
    RENAME COLUMN adr TO address,
    RENAME COLUMN lat TO latitude,
    RENAME COLUMN lon TO longitude;

DESCRIBE characteristics;

SELECT *
FROM characteristics
LIMIT 10;


ALTER TABLE locations
    RENAME COLUMN Num_Acc TO accident_id,
    RENAME COLUMN catr TO road_category,
    RENAME COLUMN voie TO road_number,
    RENAME COLUMN V1 TO road_number_index,
    RENAME COLUMN V2 TO road_alphanumeric_index,
    RENAME COLUMN circ TO traffic_regime,
    RENAME COLUMN nbv TO number_of_traffic_lanes,
    RENAME COLUMN vosp TO reserved_lane_type,
    RENAME COLUMN prof TO road_profile,
    RENAME COLUMN pr TO upstream_terminal_number,
    RENAME COLUMN pr1 TO distance_to_upstream_terminal,
    RENAME COLUMN plan TO plan_layout,
    RENAME COLUMN lartpc TO central_reservation_width,
    RENAME COLUMN larrout TO carriageway_width,
    RENAME COLUMN surf TO surface_condition,
    RENAME COLUMN infra TO infrastructure,
    RENAME COLUMN situ TO accident_location,
    RENAME COLUMN vma TO max_speed_permitted;
    
DESCRIBE locations;

SELECT *
FROM locations
LIMIT 10;

-- 2. Update Data Format and Replace Numeric Codes with Labels in "Characteristics" Table

SET SQL_SAFE_UPDATES = 0;

ALTER TABLE characteristics
MODIFY COLUMN lighting_conditions VARCHAR(50);

UPDATE characteristics
SET lighting_conditions = CASE lighting_conditions
    WHEN '1' THEN 'Broad daylight'
    WHEN '2' THEN 'Dusk or dawn'
    WHEN '3' THEN 'Night without street lighting'
    WHEN '4' THEN 'Night with street lighting off'
    WHEN '5' THEN 'Night with street lighting on'
    ELSE 'Unknown'
END;

ALTER TABLE characteristics
MODIFY location VARCHAR(50);

UPDATE characteristics
SET location = CASE location
    WHEN '1' THEN 'Outside urban areas'
    WHEN '2' THEN 'Within built-up areas'
    ELSE 'Unknown'
END;

ALTER TABLE characteristics
MODIFY COLUMN intersection VARCHAR(50);

UPDATE characteristics
SET intersection = CASE intersection
    WHEN '1' THEN 'Outside intersection'
    WHEN '2' THEN 'X-shaped intersection'
    WHEN '3' THEN 'T-junction'
    WHEN '4' THEN 'Y-junction'
    WHEN '5' THEN 'Intersection with more than 4 branches'
    WHEN '6' THEN 'Roundabout'
    WHEN '7' THEN 'Square'
    WHEN '8' THEN 'Level crossing'
    WHEN '9' THEN 'Other intersection'
    ELSE 'Unknown'
END;

ALTER TABLE characteristics
MODIFY COLUMN atmospheric_conditions VARCHAR(50);

UPDATE characteristics
SET atmospheric_conditions = CASE atmospheric_conditions
    WHEN '-1' THEN 'Not specified'
    WHEN '1' THEN 'Normal'
    WHEN '2' THEN 'Light rain'
    WHEN '3' THEN 'Heavy rain'
    WHEN '4' THEN 'Snow - hail'
    WHEN '5' THEN 'Fog - Smoke'
    WHEN '6' THEN 'Strong wind - storm'
    WHEN '7' THEN 'Glare'
    WHEN '8' THEN 'Overcast weather'
    WHEN '9' THEN 'Other'
    ELSE 'Unknown'
END;

ALTER TABLE characteristics
MODIFY COLUMN collision_type VARCHAR(60);

UPDATE characteristics
SET collision_type = CASE collision_type
    WHEN '-1' THEN 'Not specified'
    WHEN '1' THEN 'Two vehicles - head-on'
    WHEN '2' THEN 'Two vehicles - rear-end'
    WHEN '3' THEN 'Two vehicles - side'
    WHEN '4' THEN 'Three or more vehicles - chain collision'
    WHEN '5' THEN 'Three or more vehicles - multiple collisions'
    WHEN '6' THEN 'Other collision'
    WHEN '7' THEN 'No collision'
    ELSE 'Unknown'
END;


SELECT 
    (SELECT COUNT(*) FROM characteristics) AS total_rows,
    (SELECT COUNT(*) 
     FROM INFORMATION_SCHEMA.COLUMNS 
     WHERE TABLE_NAME = 'characteristics') AS total_columns;
     
     SELECT *
FROM characteristics
LIMIT 10;

-- 3. Update Data Format and Replace Numeric Codes with Labels in "Locations" Table

ALTER TABLE locations
MODIFY COLUMN road_category VARCHAR(100);

UPDATE locations
SET road_category = CASE road_category
    WHEN '1' THEN 'Motorway'
    WHEN '2' THEN 'National road'
    WHEN '3' THEN 'Departmental road'
    WHEN '4' THEN 'Municipal roads'
    WHEN '5' THEN 'Off public network'
    WHEN '6' THEN 'Car parks open to public traffic'
    WHEN '7' THEN 'Urban metropolitan roads'
    WHEN '9' THEN 'Other'
    ELSE 'Unknown'
END;

ALTER TABLE locations
MODIFY COLUMN traffic_regime VARCHAR(100);

UPDATE locations
SET traffic_regime = CASE traffic_regime
    WHEN '-1' THEN 'Not specified'
    WHEN '1'  THEN 'One-way'
    WHEN '2'  THEN 'Two-way'
    WHEN '3'  THEN 'Separate carriageways'
    WHEN '4'  THEN 'With variable lanes'
    ELSE 'Unknown'
END;

ALTER TABLE locations
MODIFY COLUMN reserved_lane_type VARCHAR(100);

UPDATE locations
SET reserved_lane_type = CASE reserved_lane_type
    WHEN '-1' THEN 'Not specified'
    WHEN '0'  THEN 'Not applicable'
    WHEN '1'  THEN 'Cycle path'
    WHEN '2'  THEN 'Cycle lane'
    WHEN '3'  THEN 'Reserved lane'
    ELSE 'Unknown'
END;

ALTER TABLE locations
MODIFY COLUMN road_profile VARCHAR(100);

UPDATE locations
SET road_profile = CASE road_profile
    WHEN '-1' THEN 'Not specified'
    WHEN '1'  THEN 'Flat'
    WHEN '2'  THEN 'Slope'
    WHEN '3'  THEN 'Top of hill'
    WHEN '4'  THEN 'Bottom of hill'
    ELSE 'Unknown'
END;

ALTER TABLE locations
MODIFY COLUMN plan_layout VARCHAR(100);

UPDATE locations
SET plan_layout = CASE plan_layout
    WHEN '-1' THEN 'Not specified'
    WHEN '1'  THEN 'Straight section'
    WHEN '2'  THEN 'Left-hand curve'
    WHEN '3'  THEN 'Curve to the right'
    WHEN '4'  THEN 'S-shaped'
    ELSE 'Unknown'
END;

ALTER TABLE locations
MODIFY COLUMN surface_condition VARCHAR(100);

UPDATE locations
SET surface_condition = CASE surface_condition
    WHEN '-1' THEN 'Not specified'
    WHEN '1'  THEN 'Normal'
    WHEN '2'  THEN 'Wet'
    WHEN '3'  THEN 'Puddles'
    WHEN '4'  THEN 'Flooded'
    WHEN '5'  THEN 'Snowy'
    WHEN '6'  THEN 'Muddy'
    WHEN '7'  THEN 'Icy'
    WHEN '8'  THEN 'Fats - oil'
    WHEN '9'  THEN 'Other'
    ELSE 'Unknown'
END;

ALTER TABLE locations
MODIFY COLUMN infrastructure VARCHAR(100);

UPDATE locations
SET infrastructure = CASE infrastructure
    WHEN '-1' THEN 'Not specified'
    WHEN '0'  THEN 'None'
    WHEN '1'  THEN 'Underground - tunnel'
    WHEN '2'  THEN 'Bridge - flyover'
    WHEN '3'  THEN 'Interchange or junction slip road'
    WHEN '4'  THEN 'Railway line'
    WHEN '5'  THEN 'Improved crossroads'
    WHEN '6'  THEN 'Pedestrian zone'
    WHEN '7'  THEN 'Toll area'
    WHEN '8'  THEN 'Construction site'
    WHEN '9'  THEN 'Other'
    ELSE 'Unknown'
END;

ALTER TABLE locations
MODIFY COLUMN accident_location VARCHAR(100);

UPDATE locations
SET accident_location = CASE accident_location
    WHEN '-1' THEN 'Not specified'
    WHEN '0'  THEN 'None'
    WHEN '1'  THEN 'On the road'
    WHEN '2'  THEN 'On emergency lane'
    WHEN '3'  THEN 'On the shoulder'
    WHEN '4'  THEN 'On pavement'
    WHEN '5'  THEN 'On cycle path'
    WHEN '6'  THEN 'On other special lanes'
    WHEN '8'  THEN 'Other'
    ELSE 'Unknown'
END;

SELECT 
    (SELECT COUNT(*) FROM locations) AS total_rows,
    (SELECT COUNT(*) 
     FROM INFORMATION_SCHEMA.COLUMNS 
     WHERE TABLE_NAME = 'locations') AS total_columns;
     
     SELECT *
FROM locations
LIMIT 10;

-- 4. Checking for Missing Values

SELECT
  SUM(accident_id IS NULL) AS missing_accident_id,
  SUM(accident_day IS NULL) AS missing_day,
  SUM(accident_month IS NULL) AS missing_month,
  SUM(accident_year IS NULL) AS missing_year,
  SUM(accident_time IS NULL) AS missing_time,
  SUM(lighting_conditions IS NULL) AS missing_lighting,
  SUM(department_id IS NULL) AS missing_department,
  SUM(municipality_id IS NULL) AS missing_municipality,
  SUM(location IS NULL OR location = '') AS missing_location,
  SUM(intersection IS NULL) AS missing_intersection,
  SUM(atmospheric_conditions IS NULL) AS missing_atmo,
  SUM(collision_type IS NULL) AS missing_collision_type,
  SUM(address IS NULL OR address = '') AS missing_address,
  SUM(latitude IS NULL) AS missing_lat,
  SUM(longitude IS NULL) AS missing_lon,
  COUNT(*) AS total_rows
FROM characteristics;

SELECT
  SUM(accident_id IS NULL) AS missing_accident_id,
  SUM(road_category IS NULL) AS missing_road_category,
  SUM(road_number IS NULL OR road_number = '') AS missing_road_number,
  SUM(road_number_index IS NULL OR road_number_index = '') AS missing_road_number_index,
  SUM(road_alphanumeric_index IS NULL OR road_alphanumeric_index = '') AS missing_alpha_index,
  SUM(traffic_regime IS NULL) AS missing_traffic_regime,
  SUM(number_of_traffic_lanes IS NULL) AS missing_lanes,
  SUM(reserved_lane_type IS NULL) AS missing_reserved_lane,
  SUM(road_profile IS NULL) AS missing_road_profile,
  SUM(upstream_terminal_number IS NULL OR upstream_terminal_number = '') AS missing_upstream_terminal,
  SUM(distance_to_upstream_terminal IS NULL) AS missing_distance,
  SUM(plan_layout IS NULL) AS missing_plan_layout,
  SUM(central_reservation_width IS NULL) AS missing_central_res_width,
  SUM(carriageway_width IS NULL) AS missing_carriageway_width,
  SUM(surface_condition IS NULL) AS missing_surface,
  SUM(infrastructure IS NULL) AS missing_infrastructure,
  SUM(accident_location IS NULL) AS missing_accident_location,
  SUM(max_speed_permitted IS NULL) AS missing_max_speed,
  COUNT(*) AS total_rows
FROM locations;

-- 5. Drop some columns from the Locations table (too many missing, excessive values)

ALTER TABLE locations
DROP COLUMN central_reservation_width,
DROP COLUMN road_number_index,
DROP COLUMN road_alphanumeric_index;


-- 6. Drop the "address" column from the Characteristics table:

ALTER TABLE characteristics
DROP COLUMN address;

-- 7. Checking for Duplicates

-- In characteristics
SELECT accident_id, COUNT(*) AS cnt
FROM characteristics
GROUP BY accident_id
HAVING COUNT(*) > 1;

-- In locations
SELECT accident_id, road_number, COUNT(*) AS cnt
FROM locations
GROUP BY accident_id, road_number
HAVING COUNT(*) > 1
ORDER BY cnt DESC;

