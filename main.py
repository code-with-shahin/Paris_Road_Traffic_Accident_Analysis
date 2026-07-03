
# Importing basic Python libraries:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Import Data

import pandas as pd

# =========================
# 1. CHARACTERISTICS
# =========================

characteristics_files = [
    f"datasets/caracteristiques-{year}.csv"
    for year in range(2020, 2025)
]

characteristics_dfs = []

for year in range(2020, 2025):
    file = f"datasets/caracteristiques-{year}.csv"
    df = pd.read_csv(file, sep=";")
    df["year"] = year
    characteristics_dfs.append(df)

characteristics = pd.concat(characteristics_dfs, ignore_index=True)


# =========================
# 2. LOCATIONS (LIEUX)
# =========================

location_files = [
    f"datasets/lieux-{year}.csv"
    for year in range(2020, 2025)
]

location_dfs = []

for year in range(2020, 2025):
    file = f"datasets/lieux-{year}.csv"
    df = pd.read_csv(file, sep=";")
    df["year"] = year
    location_dfs.append(df)

locations = pd.concat(location_dfs, ignore_index=True)


# =========================
# 3. VEHICLES (VEHICULES)
# =========================

vehicle_files = [
    f"datasets/vehicules-{year}.csv"
    for year in range(2020, 2025)
]

vehicle_dfs = []

for year in range(2020, 2025):
    file = f"datasets/vehicules-{year}.csv"
    df = pd.read_csv(file, sep=";")
    df["year"] = year
    vehicle_dfs.append(df)

vehicles = pd.concat(vehicle_dfs, ignore_index=True)


# =========================
# 4. USERS (USAGERS)
# =========================

user_files = [
    f"datasets/usagers-{year}.csv"
    for year in range(2020, 2025)
]

user_dfs = []

for year in range(2020, 2025):
    file = f"datasets/usagers-{year}.csv"
    df = pd.read_csv(file, sep=";")
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