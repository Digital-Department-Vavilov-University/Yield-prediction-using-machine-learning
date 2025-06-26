import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import pickle

df = pd.read_csv("crop_yield_dataset.csv")
df_encoded = pd.get_dummies(df, columns=["soil_type", "crop"])
X = df_encoded.drop("yield", axis=1)
y = df_encoded["yield"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, predictions))
print(f"RMSE: {rmse:.2f} т/га")
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Модель сохранена в model.pkl")
