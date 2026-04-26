import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

NUM_ITEMS = 500

STAGES = ["Receiving", "Storage", "Picking", "Packing", "Shipping"]

#Base time
start_time = datetime.now()

#Generating Item Flow
def simulate_item_flow(item_id):
    records = []
    current_time = start_time
    for stage in STAGES:
            # Simulate time taken for each stage (in minutes)
            base_time = {
            "Receiving": random.randint(5, 20),
            "Storage": random.randint(30, 180),
            "Picking": random.randint(10, 60),
            "Packing": random.randint(5, 30),
            "Shipping": random.randint(10, 45)
            }
            time_spent = base_time[stage]

            #Introducing random delays (to simualte bottlenecks, and real world scenarios)
            if random.random() < 0.15 : #15% chance of delay
                delay = random.randint(30, 120) # Delay between 30 to 120 minutes
                time_spent += delay
            
            current_time += timedelta(minutes=time_spent)
                
            records.append({
                "item_id": item_id,
                "stage": stage,
                "timestamp": current_time,
                "time_spent_minutes": time_spent
            })
    return records

#Generate data for all items
all_data = []
for item in range(1, NUM_ITEMS + 1):
    item_flow = simulate_item_flow(item)
    all_data.extend(item_flow)

df = pd.DataFrame(all_data)

#Add Derived Metrics
df["previous_timestamp"]=df.groupby("item_id")["timestamp"].shift(1)
df["time_between_stage"] = (df["timestamp"] - df["previous_timestamp"]).dt.total_seconds() / 60

#Flag Delays (example threshold)
df["is_delayed"] = df["time_spent_minutes"] > 90 # Flag if time between stages is greater than 90 minutes)


#Save Data
df.to_csv("supply_chain_simulation.csv", index=False)

print("Dataset created successfully.")
print(df.head())

#Bottleneck analysis
bottlenecks = df.groupby("stage")["time_spent_minutes"].mean().sort_values(ascending=False)
print("Average Time Spent at Each Stage:")
print(bottlenecks)

#Delay counts
delays = df[df["is_delayed"] == True]["stage"].value_counts()
print("\nDelay Counts by Stage:")
print(delays)
