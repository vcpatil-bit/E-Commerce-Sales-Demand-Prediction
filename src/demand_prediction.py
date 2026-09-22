"""
E-Commerce Sales Analysis & Demand Prediction
Main source-code workflow for the project.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def load_data(file_path):
    """Load the Superstore Excel dataset."""
    df = pd.read_excel(file_path)
    return df


def preprocess_data(df):
    """Clean the dataset and create date features."""
    df = df.copy()

    text_columns = df.select_dtypes(include="object").columns
    for column in text_columns:
        df[column] = df[column].str.strip()

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month_Name"] = df["Order Date"].dt.month_name()

    return df


def create_monthly_demand(df):
    """Create monthly demand data using Year and Month."""
    monthly_data = (
        df.groupby(["Year", "Month"])["Quantity"]
        .sum()
        .reset_index()
    )
    monthly_data.columns = ["Year", "Month", "Quantity"]
    return monthly_data


def evaluate_model(model, X_train, X_test, y_train, y_test):
    """Train a regression model and return evaluation metrics."""
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    return model, predictions, mae, rmse, r2


def main():
    # Update this path according to your local project structure.
    file_path = "../Data/raw/Sample - Superstore.xls"

    df = load_data(file_path)
    df = preprocess_data(df)

    monthly_data = create_monthly_demand(df)

    X = monthly_data[["Year", "Month"]]
    y = monthly_data["Quantity"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Linear Regression
    lr_model, lr_predictions, lr_mae, lr_rmse, lr_r2 = evaluate_model(
        LinearRegression(),
        X_train,
        X_test,
        y_train,
        y_test
    )

    # Random Forest
    rf_model, rf_predictions, rf_mae, rf_rmse, rf_r2 = evaluate_model(
        RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ),
        X_train,
        X_test,
        y_train,
        y_test
    )

    print("Linear Regression")
    print("MAE:", round(lr_mae, 2))
    print("RMSE:", round(lr_rmse, 2))
    print("R2:", round(lr_r2, 4))

    print("\nRandom Forest")
    print("MAE:", round(rf_mae, 2))
    print("RMSE:", round(rf_rmse, 2))
    print("R2:", round(rf_r2, 4))

    # 2027 forecast using Linear Regression
    future_data = pd.DataFrame({
        "Year": [2027] * 12,
        "Month": list(range(1, 13))
    })

    future_data["Predicted_Demand"] = lr_model.predict(
        future_data[["Year", "Month"]]
    )

    print("\n2027 Forecast")
    print(future_data)


if __name__ == "__main__":
    main()
