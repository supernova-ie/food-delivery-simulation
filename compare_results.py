import pandas as pd
import matplotlib.pyplot as plt

sim1 = pd.read_csv('simulation1.csv')
sim2 = pd.read_csv('simulation2.csv')

print("Sim1 ortalama süre:", sim1["delivery_time"].mean())
print("Sim2 ortalama süre:", sim2["delivery_time"].mean())

print("Sim1 zamanında teslimat:", sim1["on_time"].mean() * 100, "%")
print("Sim2 zamanında teslimat:", sim2["on_time"].mean() * 100, "%")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

plt.hist(sim1["delivery_time"], alpha=0.5, label="Sim1")
plt.hist(sim2["delivery_time"], alpha=0.5, label="Sim2")
plt.legend()
plt.title("Delivery Time Distribution")
plt.xlabel("Minute")
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1. Histogram
axes[0].hist(sim1["delivery_time"], alpha=0.5, label="Sim1", color="teal")
axes[0].hist(sim2["delivery_time"], alpha=0.5, label="Sim2", color="purple")
axes[0].set_title("Delivery Time Distribution")
axes[0].set_xlabel("Minute")
axes[0].legend()

# 2. On-time bar chart
values = [sim1["on_time"].mean()*100, sim2["on_time"].mean()*100]
axes[1].bar(["Sim1", "Sim2"], values, color=["teal", "purple"])
axes[1].set_title("On-Time Delivery %")
axes[1].set_ylabel("%")

plt.tight_layout()

plt.show()