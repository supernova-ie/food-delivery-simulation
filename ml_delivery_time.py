import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

df= pd.read_csv('combined3.csv')
df=df.dropna(axis=0)
y = df.delivery_time
features = ['distance', 'traffic_level', 'driver_load', 'is_peak_hour', 'ai_routing']
X = df[features]

train_X, val_X, train_y, val_y= train_test_split(X, y, random_state=28)

food_delivery_model = RandomForestRegressor(random_state=1)
food_delivery_model.fit(train_X, train_y)

preds_val = food_delivery_model.predict(val_X)
print(mean_absolute_error(val_y, preds_val))
print("R²:", r2_score(val_y, preds_val))

importances = pd.Series(food_delivery_model.feature_importances_, index=features)
print(importances.sort_values(ascending=False))

plt.figure(figsize=(8, 6))
plt.scatter(val_y, preds_val, alpha=0.5, color="teal")
plt.plot([val_y.min(), val_y.max()], [val_y.min(), val_y.max()], 'r--')
plt.xlabel("Actual Delivery Time")
plt.ylabel("Predicted Delivery Time")
plt.title("Actual vs Predicted")
plt.savefig("regression_results.png")
plt.show()

importances.sort_values().plot(kind="barh", color="pink")
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.savefig("feature_importance.png")
plt.show()
