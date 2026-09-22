# E-Commerce Sales Analysis & Demand Prediction Report

## 1. Project Overview

This project analyzes e-commerce sales data to understand sales performance, product demand, regional patterns, and monthly demand trends. Machine learning models are then developed to predict product demand and generate a preliminary forecast for 2027.

## 2. Dataset

The project uses a Superstore  e-commerce dataset containing order, product, sales, quantity, profit, customer, and regional information.

The dataset contains 10,194 records and 21 original columns.

## 3. Data Cleaning and Preprocessing

The following preprocessing activities were performed:

- Checked the dataset structure and data types.
- Checked for missing values.
- Checked for duplicate records.
- Removed unnecessary spaces from text fields.
- Converted `Order Date` into a proper datetime format.
- Created `Year`, `Month`, and `Month_Name` features.
- Aggregated quantity at monthly level for demand prediction.

## 4. Exploratory Data Analysis

### Monthly Sales

Monthly sales showed considerable variation over time, with several high- and low-sales periods.

### Product Demand

The top products by quantity sold included:

- Staples – 234 units
- Staple envelope – 170 units
- Easy-staple paper – 150 units

These products can be considered important products for demand and inventory analysis within this dataset.

### Regional Sales

Total sales by region:
 Region  	 Sales 
 West 		 739,813.61
 East   		 691,828.17 
 Central 	 503,170.67
 South 	 	391,721.91

### Regional Demand

 Region 	Quantity Sold 
 West		 12,466 
 East 		 11,159 
 Central 	  8,820 
 South  	  6,209 

### Monthly Demand

The aggregated monthly demand showed higher quantities in September, November, and December. November recorded the highest aggregated monthly demand at 5,793 units.

Further year-wise analysis would be required to confirm a recurring seasonal pattern.

## 5. Machine Learning

Two regression models were developed:

### Linear Regression

  MAE: 124.70
  RMSE: 174.91
  R²: 0.3440

### Random Forest Regression

  MAE: 143.96
  RMSE: 177.27
  R²: 0.3262

On the current train-test split, Linear Regression produced lower MAE and RMSE and a higher R² than Random Forest.

These results apply to the current test split and should not be interpreted as universal model performance.

## 6. 2027 Demand Forecast

Linear Regression was used to generate monthly demand estimates for 2027.

The estimated demand increased from approximately 732 units in January to approximately 1,707 units in December.

These are model-based estimates and should be treated as preliminary planning references rather than guaranteed future demand.

## 7. Business Applications

The analysis can support:

- Inventory planning
- Regional stock allocation
- Identification of high-demand products
- Demand monitoring
- Preliminary sales forecasting
- Business decision support

## 8. Limitations

The demand model currently uses only `Year` and `Month` as prediction features. Real-world demand can also depend on price, discounts, promotions, product category, region, customer behavior, holidays, and other external factors.

The current train-test split is also relatively small because the monthly aggregation produces only 48 monthly observations.

## 9. Future Improvements

Future versions can include:

- Time-series forecasting models such as ARIMA, SARIMA, or Prophet
- Additional product and regional features
- Lag and rolling-window demand features
- Holiday and promotion information
- Hyperparameter tuning
- Cross-validation suitable for time-series data
- Interactive Power BI dashboard
- Deployment as a web application or API

## 10. Conclusion

The project demonstrates an end-to-end data analytics and machine learning workflow, from data preprocessing and exploratory analysis to regression-based demand prediction and future forecasting.

It provides practical insights into sales, product demand, regional performance, and preliminary demand planning.

