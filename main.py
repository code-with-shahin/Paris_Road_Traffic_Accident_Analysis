# Importing basic Python libraries:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# ---------------------------------------------------------------------------------------------
# STEP 1. Import and Append Datasets

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
    os.path.join(output_path, "characteristics_2020_2024.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 2. Save LOCATIONS

locations.to_csv(
    os.path.join(output_path, "locations_2020_2024.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 3. Save VEHICLES

vehicles.to_csv(
    os.path.join(output_path, "vehicles_2020_2024.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 4. Save USERS

users.to_csv(
    os.path.join(output_path, "users_2020_2024.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)
