# Hanoi House Price Prediction

## Motivation
Hanoi's housing market is booming, but prices often reach unrealistic levels.  
This project aims to build a **predictive model** that estimates property prices based on location, size, and other features, helping buyers, sellers, and investors make data-driven decisions.

---

## 1. Problem Setup
### a. Problem Statement
Predict house prices in Hanoi using multiple property attributes:
- Address & District
- Property Type (apartment, villa, private house, etc.)
- Area (m²)
- Bedrooms, Bathrooms, Floors
- Legal Status & Furniture Condition
- Geolocation (Latitude & Longitude → Distance from city center)

Unlike simple calculations like `Price = Unit Price × Area`, our model captures **complex relationships** between multiple factors affecting price.

### b. Features of Interest
- **Numerical:** Area, Bedrooms, Bathrooms, Floors, Distance to city center
- **Categorical:** Property type, Legal status, Furniture
- **Target:** Log-transformed Price (`log_price`)

### c. Project Workflow
- **Data Collection:** Scraped from [batdongsan.com](https://batdongsan.com) via Apify.
- **Data Cleaning & Feature Engineering:**  
  - Dropped irrelevant or high-null columns.
  - Grouped categorical variables (e.g., furniture & legal status).
  - Created new feature: `distance_to_center`.
  - Applied log transformation to reduce skewness.
- **EDA (Exploratory Data Analysis):**  
  - Distribution analysis, correlation matrix, outlier detection.
  - Geographic visualization of property clusters.
- **Modeling:** Multiple regression algorithms tested.
- **Deployment:** Flask web app for live predictions.

---

## 2. Dataset Overview
- **Source:** Batdongsan.com (via Apify)
- **Size:** Several thousand Hanoi property listings
- **Content:** Location, property specs, and pricing information
- **Target Variable:** `log_price` (log-transformed VND price)

---

## 3. Modeling & Results
### Models Tested
- Linear Regressor
- Decision Tree Regressor
- Random Forest Regressor
- XGBRegressor
- AdaBoost Regressor
- CatBoost Regressor
- Gradient Boosting Regressor
- K Nearest Neighbors
- Ridge
- Lasso

### Performance (R² Scores)
| Model                   | R² Score |
|------------------------|---------:|
| Linear Regressor       | 0.6099 |
| Decision Tree          | 0.4655 |
| Random Forest Regressor| 0.8148 |
| XGBRegressor           | 0.7255 |
| AdaBoost Regressor     | 0.7051 |
| CatBoost Regressor     | **0.8419** |
| Gradient Boosting      | 0.8176 |
| K Nearest Neighbors    | 0.7014 |
| Ridge                  | 0.6129 |
| Lasso                  | 0.6141 |

**Best Model:** CatBoost Regressor (R² = 0.8419)

---

## 4. Web Application
- Built with **Flask**
- Takes user input (area, bedrooms, district, etc.)  
- Returns predicted house price instantly.

---

## 5. Tools & Libraries
Python · pandas · numpy · scikit-learn · XGBoost · CatBoost · Flask · matplotlib · seaborn · geopy

---

## 6. Future Work
- Expand dataset for other cities.
- Incorporate macroeconomic factors (interest rates, GDP growth).
- Deploy a **Dockerized API** or **cloud-hosted app**.

---
