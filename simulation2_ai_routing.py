import pandas as pd
import random

BASE_DELIVERY_TIME = 35  # dakika (Simulation 1 baseline)

def simulate(ai_routing=False):
    results= []
    for driver in range(1,11):
        for order in range(1,16):
            hour = random.randint(0, 24)
            if 6 <= hour < 12:
                traffic_multiplier = random.uniform(0.8, 1)
            elif 12 <= hour < 18:
                traffic_multiplier = random.uniform(1.0, 1)
            else:
                traffic_multiplier = random.uniform(1.3, 1)

            if ai_routing:
                traffic_multiplier = max(traffic_multiplier * 0.75, 0.8)

            delivery_time = random.gauss(BASE_DELIVERY_TIME, 8) * traffic_multiplier
            on_time = delivery_time <= 40
            results.append({"driver":driver,
                            "order" : order,
                            "hour":hour,
                            "delivery_time" : round(delivery_time,2),
                            "on_time" : on_time})
    return pd.DataFrame(results)


sim1 = simulate(ai_routing=False)
sim2 = simulate(ai_routing=True)

sim1["simulation"] = "Sim1"
sim2["simulation"] = "Sim2"
sim1.to_csv('simulation1.csv', index=False)
sim2.to_csv('simulation2.csv', index=False)
combined = pd.concat([sim1, sim2])
combined.to_csv('combined.csv', index=False)