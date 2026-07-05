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
# STEP 2. Save all appended tables
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
# STEP 3. Summary Tables
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


# ------------------------------------------------------------------------------------------
# STEP 4. Data Cleaning
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
    'id_vehicle': 'vehicle_id',
    'Num_Veh': 'vehicle_code',
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
    'An_nais': 'birth_year_user',
    'trajet': 'travel_reason',
    'secu1': 'safety_equipment1',
    'secu2': 'safety_equipment2',
    'secu3': 'safety_equipment3',
    'locp': 'pedestrian_location',
    'actp': 'pedestrian_action',
    'etatp': 'pedestrian_presence'
})

# Drop "year" column from all datasets

characteristics = characteristics.drop(columns=['year'])
locations = locations.drop(columns=['year'])
vehicles = vehicles.drop(columns=['year'])
users = users.drop(columns=['year'])

# Check the column names:

print("Characteristics columns:", characteristics.columns.tolist())
print("Locations columns:", locations.columns.tolist())
print("Vehicles columns:", vehicles.columns.tolist())
print("Users columns:", users.columns.tolist())

# 2. Update Data Format and Replace Numeric Codes with Labels

# 2.1 "Characteristics" Table

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

print(characteristics['lighting_conditions'].value_counts(dropna=False))

