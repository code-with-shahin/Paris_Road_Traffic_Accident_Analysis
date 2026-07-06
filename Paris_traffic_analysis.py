# Importing basic Python libraries:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------------------------------------------------------------
# STEP 1. Import and Append Datasets
# ---------------------------------------------------------------------------------------------

# =========================
# 1. CHARACTERISTICS
# =========================

characteristics_dfs = []

for year in range(2020, 2025):
    file = f"datasets/caracteristiques-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    # clean column names
    df.columns = df.columns.str.replace('"', '').str.strip()

    # fix schema difference (2022 issue)
    df.rename(columns={"Accident_Id": "Num_Acc"}, inplace=True)

    # add year column
    df["year"] = year

    characteristics_dfs.append(df)

characteristics = pd.concat(characteristics_dfs, ignore_index=True)

# =========================
# 2. LOCATIONS (LIEUX)
# =========================

location_dfs = []

for year in range(2020, 2025):
    file = f"datasets/lieux-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    # clean column names
    df.columns = df.columns.str.replace('"', '').str.strip()

    # add year column
    df["year"] = year

    location_dfs.append(df)

locations = pd.concat(location_dfs, ignore_index=True)

# Updating the data type for nbv column:
locations['nbv'] = pd.to_numeric(locations['nbv'], errors='coerce').astype('Int64')

# =========================
# 3. VEHICLES (VEHICULES)
# =========================

vehicle_dfs = []

for year in range(2020, 2025):
    file = f"datasets/vehicules-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    # clean column names
    df.columns = df.columns.str.replace('"', '').str.strip()

    # add year column
    df["year"] = year

    vehicle_dfs.append(df)

vehicles = pd.concat(vehicle_dfs, ignore_index=True)

# =========================
# 4. USERS (USAGERS)
# =========================

user_dfs = []

for year in range(2020, 2025):
    file = f"datasets/usagers-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    df.columns = df.columns.str.replace('"', '').str.strip()

    # fix missing "id_usager" column in 2020 table automatically
    if "id_usager" not in df.columns:
        df.insert(1, "id_usager", pd.NA)

    # add year column
    df["year"] = year

    user_dfs.append(df)

users = pd.concat(user_dfs, ignore_index=True)

# Updating the data type for id_usager column:
users['id_usager'] = (
    users['id_usager']
    .astype(str)
    .str.replace(' ', '', regex=False)  # remove thousands-separator spaces
    .str.replace('\xa0', '', regex=False)  # also handle non-breaking spaces, common in French exports
    .str.strip()
)

users['id_usager'] = pd.to_numeric(users['id_usager'], errors='coerce').astype('Int64')

# =========================
# QUICK CHECKS
# =========================

print("Characteristics:", characteristics.shape)
print("Locations:", locations.shape)
print("Vehicles:", vehicles.shape)
print("Users:", users.shape)

print("\n==================== CHARACTERISTICS ====================")
print(characteristics.head())

print("\n==================== LOCATIONS ====================")
print(locations.head())

print("\n==================== VEHICLES ====================")
print(vehicles.head())

print("\n==================== USERS ====================")
print(users.head())

# ------------------------------------------------------------------------------------------
# STEP 2. Data Cleaning
# ------------------------------------------------------------------------------------------

# 1. Rename the columns for all datasets:

characteristics = characteristics.rename(columns={
    'Num_Acc': 'accident_id',
    'jour': 'accident_day',
    'mois': 'accident_month',
    'an': 'accident_year',
    'hrmn': 'accident_time',
    'lum': 'lighting_conditions',
    'dep': 'department_id',
    'com': 'municipality_id',
    'agg': 'location',
    'int': 'intersection',
    'atm': 'atmospheric_conditions',
    'col': 'collision_type',
    'adr': 'address',
    'lat': 'latitude',
    'long': 'longitude'
})

locations = locations.rename(columns={
    'Num_Acc': 'accident_id',
    'catr': 'road_category',
    'voie': 'road_number',
    'v1': 'road_number_index',
    'v2': 'road_alphanumeric_index',
    'circ': 'traffic_regime',
    'nbv': 'number_of_traffic_lanes',
    'vosp': 'reserved_lane_type',
    'prof': 'road_profile',
    'pr': 'upstream_terminal_number',
    'pr1': 'distance_to_upstream_terminal',
    'plan': 'plan_layout',
    'lartpc': 'central_reservation_width',
    'larrout': 'carriageway_width',
    'surf': 'surface_condition',
    'infra': 'infrastructure',
    'situ': 'accident_location',
    'vma': 'max_speed_permitted'
})

vehicles = vehicles.rename(columns={
    'Num_Acc': 'accident_id',
    'id_vehicule': 'vehicle_id',
    'num_veh': 'vehicle_code',
    'senc': 'travel_direction',
    'catv': 'vehicle_category',
    'obs': 'fixed_obstacle_struck',
    'obsm': 'mobile_obstacle_struck',
    'choc': 'initial_impact_point',
    'manv': 'main_manoeuvre_before_the_accident',
    'motor': 'vehicle_engine_type',
    'occutc': 'occupants_in_public_transport'
})

users = users.rename(columns={
    'Num_Acc': 'accident_id',
    'id_usager': 'user_id',
    'id_vehicle': 'vehicle_id',
    'num_veh': 'vehicle_code',
    'place': 'seat_place',
    'catu': 'user_category',
    'grav': 'injury_severity',
    'sexe': 'gender',
    'an_nais': 'birth_year_user',
    'trajet': 'travel_reason',
    'secu1': 'safety_equipment1',
    'secu2': 'safety_equipment2',
    'secu3': 'safety_equipment3',
    'locp': 'pedestrian_location',
    'actp': 'pedestrian_action',
    'etatp': 'pedestrian_presence'
})

# Convert to a proper year format, keeping NaN as NaN (can't force int if missing values exist)
users['birth_year_user'] = users['birth_year_user'].astype('Int64')  # capital "I" = pandas nullable integer type

# Check the column names:

print("Characteristics columns:", characteristics.columns.tolist())
print("Locations columns:", locations.columns.tolist())
print("Vehicles columns:", vehicles.columns.tolist())
print("Users columns:", users.columns.tolist())

# 2. Update Data Format and Replace Numeric Codes with Labels

# 2.1 Update "Characteristics" Dataframe

# Mapping dictionary
lighting_map = {
    '1': 'Broad daylight',
    '2': 'Dusk or dawn',
    '3': 'Night without street lighting',
    '4': 'Night with street lighting off',
    '5': 'Night with street lighting on'
}

# Ensure the column is treated as string before mapping (in case it's read as int/float)
characteristics['lighting_conditions'] = (
    characteristics['lighting_conditions']
    .astype(str)
    .str.strip()          # remove any stray whitespace
    .str.split('.').str[0]  # handles cases where it was read as float, e.g. '1.0' -> '1'
    .map(lighting_map)
    .fillna('Unknown')
    .astype('category')
)

location_map = {
    '1': 'Outside urban areas',
    '2': 'Within built-up areas'
}

characteristics['location'] = (
    characteristics['location']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(location_map)
    .fillna('Unknown')
    .astype('category')
)

intersection_map = {
    '1': 'Outside intersection',
    '2': 'X-shaped intersection',
    '3': 'T-junction',
    '4': 'Y-junction',
    '5': 'Intersection with more than 4 branches',
    '6': 'Roundabout',
    '7': 'Square',
    '8': 'Level crossing',
    '9': 'Other intersection'
}

characteristics['intersection'] = (
    characteristics['intersection']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(intersection_map)
    .fillna('Unknown')
    .astype('category')
)

atmospheric_conditions_map = {
    '-1': 'Not specified',
    '1': 'Normal',
    '2': 'Light rain',
    '3': 'Heavy rain',
    '4': 'Snow - hail',
    '5': 'Fog - Smoke',
    '6': 'Strong wind - storm',
    '7': 'Glare',
    '8': 'Overcast weather',
    '9': 'Other'
}

characteristics['atmospheric_conditions'] = (
    characteristics['atmospheric_conditions']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(atmospheric_conditions_map)
    .fillna('Unknown')
    .astype('category')
)

collision_type_map = {
    '-1': 'Not specified',
    '1': 'Two vehicles - head-on',
    '2': 'Two vehicles - rear-end',
    '3': 'Two vehicles - side',
    '4': 'Three or more vehicles - chain collision',
    '5': 'Three or more vehicles - multiple collisions',
    '6': 'Other collision',
    '7': 'No collision'
}

characteristics['collision_type'] = (
    characteristics['collision_type']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(collision_type_map)
    .fillna('Unknown')
    .astype('category')
)

# 2.2 Update "Locations" Dataframe

# road_category
road_category_map = {
    '1': 'Motorway',
    '2': 'National road',
    '3': 'Departmental road',
    '4': 'Municipal roads',
    '5': 'Off public network',
    '6': 'Car parks open to public traffic',
    '7': 'Urban metropolitan roads',
    '9': 'Other'
}

locations['road_category'] = (
    locations['road_category']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(road_category_map)
    .fillna('Unknown')
    .astype('category')
)

# traffic_regime
traffic_regime_map = {
    '-1': 'Not specified',
    '1': 'One-way',
    '2': 'Two-way',
    '3': 'Separate carriageways',
    '4': 'With variable lanes'
}

locations['traffic_regime'] = (
    locations['traffic_regime']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(traffic_regime_map)
    .fillna('Unknown')
    .astype('category')
)

# reserved_lane_type
reserved_lane_type_map = {
    '-1': 'Not specified',
    '0': 'Not applicable',
    '1': 'Cycle path',
    '2': 'Cycle lane',
    '3': 'Reserved lane'
}

locations['reserved_lane_type'] = (
    locations['reserved_lane_type']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(reserved_lane_type_map)
    .fillna('Unknown')
    .astype('category')
)

# road_profile
road_profile_map = {
    '-1': 'Not specified',
    '1': 'Flat',
    '2': 'Slope',
    '3': 'Top of hill',
    '4': 'Bottom of hill'
}

locations['road_profile'] = (
    locations['road_profile']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(road_profile_map)
    .fillna('Unknown')
    .astype('category')
)

# plan_layout
plan_layout_map = {
    '-1': 'Not specified',
    '1': 'Straight section',
    '2': 'Left-hand curve',
    '3': 'Curve to the right',
    '4': 'S-shaped'
}

locations['plan_layout'] = (
    locations['plan_layout']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(plan_layout_map)
    .fillna('Unknown')
    .astype('category')
)

# surface_condition
surface_condition_map = {
    '-1': 'Not specified',
    '1': 'Normal',
    '2': 'Wet',
    '3': 'Puddles',
    '4': 'Flooded',
    '5': 'Snowy',
    '6': 'Muddy',
    '7': 'Icy',
    '8': 'Fats - oil',
    '9': 'Other'
}

locations['surface_condition'] = (
    locations['surface_condition']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(surface_condition_map)
    .fillna('Unknown')
    .astype('category')
)

# infrastructure
locations["infrastructure"] = locations["infrastructure"].replace({
    -1: "Not specified",
     0: "No infrastructure",
     1: "Underground - tunnel",
     2: "Bridge - flyover",
     3: "Interchange or junction slip road",
     4: "Railway line",
     5: "Improved crossroads",
     6: "Pedestrian zone",
     7: "Toll area",
     8: "Construction site",
     9: "Other"
})

# accident_location
accident_location_map = {
    '-1': 'Not specified',
    '0': 'None',
    '1': 'On the road',
    '2': 'On emergency lane',
    '3': 'On the shoulder',
    '4': 'On pavement',
    '5': 'On cycle path',
    '6': 'On other special lanes',
    '8': 'Other'
}

locations['accident_location'] = (
    locations['accident_location']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(accident_location_map)
    .fillna('Unknown')
    .astype('category')
)

# 2.3 Update "Vehicles" Dataframe

# travel_direction
travel_direction_map = {
    '-1': 'Not specified',
    '0': 'Unknown',
    '1': 'PK or PR or ascending postal address number',
    '2': 'PK or PR or descending postal address number',
    '3': 'No reference point'
}

vehicles['travel_direction'] = (
    vehicles['travel_direction']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(travel_direction_map)
    .fillna('Unknown')
    .astype('category')
)

# vehicle_category
vehicle_category_map = {
    '00': 'Indeterminable',
    '01': 'Bicycle',
    '02': 'Moped',
    '03': 'Microcar',
    '07': 'Light vehicle',
    '10': 'Light commercial vehicle',
    '13': 'HGV 3.5T < GVW <= 7.5T',
    '14': 'HGV > 7.5T',
    '15': 'HGV > 3.5T + trailer',
    '16': 'Road tractor',
    '17': 'Road tractor + semi-trailer',
    '20': 'Special vehicle',
    '21': 'Agricultural tractor',
    '30': 'Scooter < 50 cm3',
    '31': 'Motorcycle > 50 cm³ and ≤ 125 cm³',
    '32': 'Scooter > 50 cm3 and ≤ 125 cm3',
    '33': 'Motorcycle > 125 cc',
    '34': 'Scooter > 125 cc',
    '35': 'Light quad bike',
    '36': 'Heavy quad bike',
    '37': 'Bus',
    '38': 'Coach',
    '39': 'Train',
    '40': 'Tram',
    '41': '3RM ≤ 50 cm³',
    '42': '3RM > 50 cm³ ≤ 125 cm³',
    '43': '3-wheel motorcycles > 125 cm3',
    '50': 'Motorised EDP',
    '60': 'EDP without motor',
    '80': 'EAB',
    '99': 'Other vehicle'
}

vehicles['vehicle_category'] = (
    vehicles['vehicle_category']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .str.zfill(2)                 # restores leading zero, e.g. '0' -> '00', '1' -> '01'
    .map(vehicle_category_map)
    .fillna('Unknown')
    .astype('category')
)

# fixed_obstacle_struck
fixed_obstacle_struck_map = {
    '-1': 'Not specified',
    '0': 'Not applicable',
    '1': 'Parked vehicle',
    '2': 'Tree',
    '3': 'Metal guardrail',
    '4': 'Concrete barrier',
    '5': 'Other barrier',
    '6': 'Building, wall, bridge pier',
    '7': 'Vertical signage support or emergency call station',
    '8': 'Pole',
    '9': 'Street furniture',
    '10': 'Parapet',
    '11': 'Island, refuge, high bollard',
    '12': 'Kerbs',
    '13': 'Ditch, embankment, rock face',
    '14': 'Other fixed obstacle on the carriageway',
    '15': 'Other fixed obstacle on pavement or verge',
    '16': 'Road exit without obstacle',
    '17': 'Culvert – aqueduct head'
}

vehicles['fixed_obstacle_struck'] = (
    vehicles['fixed_obstacle_struck']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(fixed_obstacle_struck_map)
    .fillna('Unknown')
    .astype('category')
)

# mobile_obstacle_struck
mobile_obstacle_struck_map = {
    '-1': 'Not specified',
    '0': 'None',
    '1': 'Pedestrian',
    '2': 'Vehicle',
    '4': 'Rail vehicle',
    '5': 'Domestic animal',
    '6': 'Wild animal',
    '9': 'Other'
}

vehicles['mobile_obstacle_struck'] = (
    vehicles['mobile_obstacle_struck']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(mobile_obstacle_struck_map)
    .fillna('Unknown')
    .astype('category')
)

# initial_impact_point
initial_impact_point_map = {
    '-1': 'Not specified',
    '0': 'None',
    '1': 'Before',
    '2': 'Right forward',
    '3': 'Front left',
    '4': 'Rear',
    '5': 'Rear right',
    '6': 'Rear left',
    '7': 'Right side',
    '8': 'Left side',
    '9': 'Multiple impacts (rollovers)'
}

vehicles['initial_impact_point'] = (
    vehicles['initial_impact_point']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(initial_impact_point_map)
    .fillna('Unknown')
    .astype('category')
)

# main_manoeuvre_before_the_accident
main_manoeuvre_map = {
    '-1': 'Not specified',
    '0': 'Unknown',
    '1': 'No change in direction',
    '2': 'Same direction, same lane',
    '3': 'Between two lanes',
    '4': 'Reversing',
    '5': 'Wrong way',
    '6': 'Crossing the central reservation',
    '7': 'In the bus lane, in the same direction',
    '8': 'In the bus lane, in the opposite direction',
    '9': 'By turning around',
    '10': 'By turning around on the road',
    '11': 'Changing lanes to the left',
    '12': 'Changing lanes to the right',
    '13': 'Offset to the left',
    '14': 'Offset to the right',
    '15': 'Turning to the left',
    '16': 'Turning to the right',
    '17': 'Overtaking left',
    '18': 'Overtaking right',
    '19': 'Crossing the road',
    '20': 'Parking manoeuvre',
    '21': 'Evasive manoeuvre',
    '22': 'Opening the door',
    '23': 'Stopping (outside of parking)',
    '24': 'Parking (with occupants)',
    '25': 'Driving on the pavement',
    '26': 'Other manoeuvres'
}

vehicles['main_manoeuvre_before_the_accident'] = (
    vehicles['main_manoeuvre_before_the_accident']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(main_manoeuvre_map)
    .fillna('Unknown')
    .astype('category')
)

# vehicle_engine_type
vehicle_engine_type_map = {
    '-1': 'Not specified',
    '0': 'Unknown',
    '1': 'Hydrocarbons',
    '2': 'Electric hybrid',
    '3': 'Electric',
    '4': 'Hydrogen',
    '5': 'Human',
    '6': 'Other'
}

vehicles['vehicle_engine_type'] = (
    vehicles['vehicle_engine_type']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(vehicle_engine_type_map)
    .fillna('Unknown')
    .astype('category')
)

# 2.4 Update "Users" Dataframe

# seat_place
users['seat_place'] = (
    users['seat_place']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .replace({'10': 'Pedestrian'})
)

# user_category
user_category_map = {
    '1': 'Driver',
    '2': 'Passenger',
    '3': 'Pedestrian'
}

users['user_category'] = (
    users['user_category']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(user_category_map)
    .fillna('Unknown')
    .astype('category')
)

# injury_severity
injury_severity_map = {
    '1': 'Uninjured',
    '2': 'Killed',
    '3': 'Hospitalised',
    '4': 'Slightly injured'
}

users['injury_severity'] = (
    users['injury_severity']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(injury_severity_map)
    .fillna('Unknown')
    .astype('category')
)

# gender
gender_map = {
    '1': 'Male',
    '2': 'Feminine'
}

users['gender'] = (
    users['gender']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(gender_map)
    .fillna('Unknown')
    .astype('category')
)

# travel_reason
travel_reason_map = {
    '-1': 'Not specified',
    '0': 'Not specified',
    '1': 'Home – work',
    '2': 'Home – school',
    '3': 'Shopping – purchases',
    '4': 'Professional use',
    '5': 'Walking – leisure',
    '9': 'Other'
}

users['travel_reason'] = (
    users['travel_reason']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(travel_reason_map)
    .fillna('Unknown')
    .astype('category')
)

# safety_equipment
safety_equipment_map = {
    '-1': 'Not specified',
    '0': 'No equipment',
    '1': 'Seatbelt',
    '2': 'Helmet',
    '3': 'Child restraint',
    '4': 'Reflective vest',
    '5': 'Airbag (2-wheel/3-wheel)',
    '6': 'Gloves (2-wheel/3-wheel)',
    '7': 'Gloves + airbag (2-wheel/3-wheel)',
    '8': 'Not determinable',
    '9': 'Other'
}

for col in ['safety_equipment1', 'safety_equipment2', 'safety_equipment3']:
    users[col] = (
        users[col]
        .astype(str)
        .str.strip()
        .str.split('.').str[0]
        .map(safety_equipment_map)
        .fillna('Unknown')
        .astype('category')
    )

# pedestrian_location
pedestrian_location_map = {
    '-1': 'Not specified',
    '0': 'Not applicable',
    '1': 'More than 50 metres from the pedestrian crossing',
    '2': 'Less than 50 metres from the pedestrian crossing',
    '3': 'Pedestrian crossing without traffic lights',
    '4': 'Pedestrian crossing with traffic lights',
    '5': 'On the pavement',
    '6': 'On the hard shoulder',
    '7': 'On refuge or BAU',
    '8': 'On the side lane',
    '9': 'Unknown'
}

users['pedestrian_location'] = (
    users['pedestrian_location']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(pedestrian_location_map)
    .fillna('Unknown')
    .astype('category')
)

# pedestrian_action
pedestrian_action_map = {
    '-1': 'Not specified',
    '0': 'Not specified or not applicable',
    '1': 'Moving to the direction of vehicle impact',
    '2': 'Moving to the opposite direction to vehicle',
    '3': 'Crossing',
    '4': 'Hidden',
    '5': 'Playing – Running',
    '6': 'With animal',
    '9': 'Other',
    'A': 'Gets in/out of the vehicle',
    'B': 'Unknown'
}

users['pedestrian_action'] = (
    users['pedestrian_action']
    .astype(str)
    .str.strip()
    .str.upper()                    # normalizes 'a'/'b' to 'A'/'B' in case of inconsistent casing
    .str.split('.').str[0]
    .map(pedestrian_action_map)
    .fillna('Unknown')
    .astype('category')
)

# pedestrian_presence
pedestrian_presence_map = {
    '-1': 'Not specified',
    '1': 'Alone',
    '2': 'Accompanied',
    '3': 'In a group'
}

users['pedestrian_presence'] = (
    users['pedestrian_presence']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(pedestrian_presence_map)
    .fillna('Unknown')
    .astype('category')
)


# Stop pandas from truncating/wrapping columns in the console output:

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)      # 0 tells pandas to detect terminal width, but often works better than None for wrapping issues
pd.set_option('display.expand_frame_repr', False)  # this is the key one — stops line wrapping entirely


# Verify the dataframes

print("=== characteristics ===")
print(characteristics.head(5))

print("\n=== locations ===")
print(locations.head(5))

print("\n=== users ===")
print(users.head(5))

print("\n=== vehicles ===")
print(vehicles.head(5))

# 3. Drop redundant columns

# Drop "year" column from all datasets
characteristics = characteristics.drop(columns=['year'])
locations = locations.drop(columns=['year'])
vehicles = vehicles.drop(columns=['year'])
users = users.drop(columns=['year'])

# Drop unnecessary columns
locations = locations.drop(columns=['road_number_index', 'road_alphanumeric_index', 'central_reservation_width'])
vehicles = vehicles.drop(columns=['occupants_in_public_transport'])


# ------------------------------------------------------------------------------------------
# STEP 3. Save all appended tables
# ------------------------------------------------------------------------------------------

output_path = r"D:\PycharmProjects\Paris_Road_Traffic_Analysis\datasets\processed"

import os
os.makedirs(output_path, exist_ok=True)

# 1. Save CHARACTERISTICS

characteristics.to_csv(
    os.path.join(output_path, "characteristics.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 2. Save LOCATIONS

locations.to_csv(
    os.path.join(output_path, "locations.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 3. Save VEHICLES

vehicles.to_csv(
    os.path.join(output_path, "vehicles.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 4. Save USERS

users.to_csv(
    os.path.join(output_path, "users.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# ------------------------------------------------------------------------------------------
# STEP 4. Summary Tables
# ------------------------------------------------------------------------------------------

# Load processed files

import pandas as pd
import os

processed_path = r"D:\PycharmProjects\Paris_Road_Traffic_Analysis\datasets\processed"

characteristics = pd.read_csv(
    os.path.join(processed_path, "characteristics.csv"),
    sep=";"
)

locations = pd.read_csv(
    os.path.join(processed_path, "locations.csv"),
    sep=";"
)

vehicles = pd.read_csv(
    os.path.join(processed_path, "vehicles.csv"),
    sep=";"
)

users = pd.read_csv(
    os.path.join(processed_path, "users.csv"),
    sep=";"
)

# Summary Tables for each dataset

def create_summary(df):
    summary = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.values,
        "Missing Values": df.isnull().sum().values,
        "Missing %": df.isnull().mean().values * 100,
        "Unique Values": df.nunique().values
    })
    return summary

print("\n==================== CHARACTERISTICS ====================")
characteristics_summary = create_summary(characteristics)
print(characteristics_summary)

print("\n==================== LOCATIONS ====================")
locations_summary = create_summary(locations)
print(locations_summary)

print("\n==================== VEHICLES ====================")
vehicles_summary = create_summary(vehicles)
print(vehicles_summary)

print("\n==================== USERS ====================")
users_summary = create_summary(users)
print(users_summary)

# Shapes of Tables

print("Characteristics shape:", characteristics.shape)
print("Locations shape:", locations.shape)
print("Vehicles shape:", vehicles.shape)
print("Users shape:", users.shape)
