# France Road Traffic Accident Analysis (2021–2024)

## 📌 Project Overview

This project analyses road traffic accidents resulting in personal injury in France between **2021 and 2024** using **Microsoft Power BI**. The goal is to transform raw accident data into an interactive dashboard that helps identify accident trends, high-risk groups, environmental factors, and geographical patterns.

The project follows data analytics best practices, including data cleaning, dimensional modelling, DAX calculations, and interactive dashboard design.

---

## 🎯 Project Objectives

- Analyse accident trends over time
- Identify high-risk demographics
- Examine the influence of weather and lighting conditions
- Investigate accident severity
- Explore geographic distribution of accidents
- Build an efficient star schema data model
- Create interactive dashboards for business users

---

## 📊 Dataset

The project uses the official French road traffic accident datasets containing personal injury accidents.

The dataset consists of four annual datasets (2021–2024) and includes information about:

- Accident characteristics
- Vehicles involved
- Road users
- Accident locations

Main entities include:

- Characteristics
- Users
- Vehicles
- Locations

---

## 🏗️ Data Model

A **Star Schema** was implemented to improve performance and simplify reporting.

### Fact Table

- Fact_Users

### Dimension Tables

- Dim_Date
- Dim_Vehicles
- Dim_Locations
- Dim_Weather

---

## 🛠 Tools & Technologies

- Python (PyCharm)
- SQL (MySQL)
- Microsoft Power BI Desktop
- Power Query
- DAX
- Data Modelling
- Star Schema
- Microsoft Excel

---

## 📈 Dashboard Features

The dashboard provides interactive analysis including:

### Accident Overview

- Total accidents
- Total casualties
- Number of vehicles involved
- Number of road users

### Time Analysis

- Accidents by Year
- Accidents by Month
- Accident trends over time

### Demographic Analysis

- Age distribution
- Gender distribution
- User category
- Travel purpose

### Environmental Analysis

- Weather conditions
- Lighting conditions
- Road surface conditions

### Road Analysis

- Road category
- Speed limit
- Number of traffic lanes
- Road profile

### Injury Analysis

- Injury severity
- Serious vs minor injuries
- Fatal accidents

### Geographic Analysis

- Accident locations
- Department-level analysis
- Latitude & Longitude mapping

---

## 📊 Data Preparation

Data preprocessing included:

- Cleaning missing values
- Correcting data types
- Removing duplicates
- Creating calculated columns
- Building relationships
- Creating a Date table
- Data normalisation
- Power Query transformations

---

## 📐 DAX Measures

- Total Accidents
- Total Users Involved
- Total Vehicles Involved
- Average Age
- Fatal Accident Count
- Serious Injury Count
- Accident Rate
- Year-over-Year Growth
- Percentage of Severe Accidents
- Accidents per 1000 Users

---

## 📷 Dashboard Preview

<img width="1364" height="789" alt="2026-07-20 22_54_23-France" src="https://github.com/user-attachments/assets/555e1477-7979-4287-832a-af0fa4ec27d1" />

---

## 📁 Repository Structure

```
France_Road_Traffic_Accident_Analysis/
│
├── Datasets/
│   ├── Raw Data
│   └── Clean Data
│
├── Images/
│   ├── dashboard_overview.png
│   ├── accident_trends.png
│   └── map_analysis.png
│
├── PowerBI/
│   └── France.pbix
│
├── README.md
└── LICENSE
```

---

## 💡 Key Insights

- Accident frequency varies throughout the year.
- Poor lighting conditions are associated with higher accident severity.
- Young drivers are involved in a significant proportion of accidents.
- Urban areas experience higher accident volumes than rural regions.
- Weather conditions influence accident occurrence and severity.

---

## 🚀 Future Improvements

- Predict accident severity using Machine Learning
- Integrate weather API data
- Add forecasting with Power BI
- Perform hotspot analysis using GIS
- Build a real-time dashboard

---

## 👤 Author

**Shahin Amirov**

- Microsoft Certified: Power BI Data Analyst Associate (PL-300)
- Data Analyst
- LinkedIn: *https://www.linkedin.com/in/shahin-amirov/*
- GitHub: *https://github.com/code-with-shahin*

---

## ⭐ If you found this project useful, feel free to star the repository!
