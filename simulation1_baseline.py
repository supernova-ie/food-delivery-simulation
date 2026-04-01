import pandas as pd
import random

NUM_DRIVERS = 10
ORDERS_PER_DRIVER = 15
BASE_DELIVERY_TIME = 35  # dakika (Simulation 1 baseline)
results=[]
for i in range(15):
    delivery_time = random.gauss(35, 8)
    on_time = delivery_time <= 40
    results.append({"delivery":i,"delivery time" : round(delivery_time), "on time":on_time,  })

output = pd.DataFrame(results)
output.to_csv('submission1.csv', index=False)
print("Submission dosyası başarıyla oluşturuldu!")