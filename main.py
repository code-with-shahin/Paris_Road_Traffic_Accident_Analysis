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

# ------------------------------------------------------------------------------------------
# STEP 3. Summary Tables
# ------------------------------------------------------------------------------------------

# Load processed files

import pandas as pd
import os

processed_path = r"D:\PycharmProjects\Paris_Road_Traffic_Analysis\datasets\processed"

characteristics = pd.read_csv(
    os.path.join(processed_path, "characteristics_2020_2024.csv"),
    sep=";"
)

locations = pd.read_csv(
    os.path.join(processed_path, "locations_2020_2024.csv"),
    sep=";"
)

vehicles = pd.read_csv(
    os.path.join(processed_path, "vehicles_2020_2024.csv"),
    sep=";"
)

users = pd.read_csv(
    os.path.join(processed_path, "users_2020_2024.csv"),
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

