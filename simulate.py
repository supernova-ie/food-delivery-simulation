import pandas as pd
import random

def simulate(ai_routing=False):
    results= []
    for driver in range(1,51):
        for order in range(1,16):
            hour = random.randint(0, 24)
            if 6 <= hour < 12:
                traffic_level = "low"
            elif 12 <= hour < 18:
                traffic_level = "medium"
            else:
                traffic_level = "high"

            distance = round(random.uniform(1, 15), 2)

            driver_load = int(order * random.uniform(0.7, 1.3))

            is_peak_hour = 1 if (12 <= hour < 14 or 18 <= hour < 20) else 0

            base_time = distance * 3
            traffic_penalty = {"low": 0, "medium": 5, "high": 15}[traffic_level]
            load_penalty = driver_load * 0.2
            peak_penalty = is_peak_hour * 8
            noise = random.gauss(0, 3)

            if ai_routing:
                traffic_penalty = traffic_penalty * 0.5
                peak_penalty = peak_penalty * 0.7

            delivery_time = base_time + traffic_penalty + load_penalty + peak_penalty + noise
            on_time = delivery_time <= 40
            results.append({"driver":driver,
                            "order" : order,
                            "hour":hour,
                            "delivery_time" : round(delivery_time,2),
                            "on_time" : on_time,
                            "traffic_level" : traffic_level,
                            "distance" : distance,
                            "driver_load" : driver_load,
                            "is_peak_hour" : is_peak_hour,
                            "ai_routing": int(ai_routing)})
    return pd.DataFrame(results)


sim1 = simulate(ai_routing=False)
sim2 = simulate(ai_routing=True)

sim1["traffic_level"] = sim1["traffic_level"].map({"low": 0, "medium": 1, "high": 2})
sim2["traffic_level"] = sim2["traffic_level"].map({"low": 0, "medium": 1, "high": 2})
sim1.to_csv('simulation_1.csv', index=False)
sim2.to_csv('simulation_2.csv', index=False)
combined = pd.concat([sim1, sim2])
combined.to_csv('combined3.csv', index=False)
