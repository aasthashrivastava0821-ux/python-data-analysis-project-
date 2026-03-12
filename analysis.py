import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Show data
print("Sales Data:")
print(data)

# Plot graph
plt.bar(data["Month"], data["Sales"])
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()