import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df= pd.read_csv('combined3.csv')
df=df.dropna(axis=0)
y = df.on_time
features = ['distance', 'traffic_level', 'driver_load', 'is_peak_hour', 'ai_routing']
X = df[features]

train_X, val_X, train_y, val_y= train_test_split(X, y, random_state=28)

food_delivery_model = RandomForestClassifier(random_state=1)
food_delivery_model.fit(train_X, train_y)

y_pred = food_delivery_model.predict(val_X)
print(accuracy_score(val_y, y_pred))
print(classification_report(val_y, y_pred))

cm = confusion_matrix(val_y, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Late (False)", "On time(True)"])
disp.plot(cmap=plt.cm.Blues)

plt.title("Food Delivery Confusion Matrix")
plt.show()
