# 📦 Supply Chain Simulation (IoT-Inspired)

## 📖 Overview
This project simulates a real-time supply chain tracking system inspired by large-scale logistics environments like Walmart's ambient supply chain.

The goal is to model how items move through a warehouse and identify inefficiencies using data.

---

## ⚙️ Features
- Simulates item movement across 5 warehouse stages:
  - Receiving → Storage → Picking → Packing → Shipping
- Generates timestamped event-level data
- Introduces random delays to mimic real-world bottlenecks
- Creates derived metrics for analysis

---

## 🧠 Key Analysis
- Identified bottlenecks using average dwell time
- Flagged delayed items based on thresholds
- Analyzed stage-to-stage transition times

---

## 🛠 Tech Stack
- Python (pandas, datetime, random)
- CSV data output
- Ready for visualization in Tableau/Power BI

---

## 📊 Example Use Cases
- Warehouse efficiency optimization
- Inventory flow tracking
- Delay detection and alert systems

---

## 🚀 Future Improvements
- Real-time streaming simulation
- Predictive modeling for delays
- Interactive dashboard

---

## 📁 Files
- `simulation.py` → main dataset generator
- `supply_chain_simulation.csv` → generated dataset

---

## 💡 Business Impact
Reducing dwell time and identifying bottlenecks can significantly improve inventory flow, reduce stockouts, and increase operational efficiency.
