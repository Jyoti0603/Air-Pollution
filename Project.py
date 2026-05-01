# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load data
file_path = "C:\\Users\\Jyoti\\OneDrive\\Desktop\\air-quality-india.csv"
df = pd.read_csv(file_path)

# Step 3: Check data
print(df.head())

# Step 4: Convert Timestamp properly
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Step 5: Drop missing values
df = df.dropna()

# Step 6: (Optional) Recreate Month & Year from Timestamp (more accurate)
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month

# Step 7: Trend over time
df.groupby('Timestamp')['PM2.5'].mean().plot(figsize=(10,5))
plt.title("PM2.5 Trend Over Time")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.show()

# Step 8: Monthly pattern
df.groupby('Month')['PM2.5'].mean().plot(marker='o')
plt.title("Monthly Pollution Pattern")
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.show()

# Step 9: Yearly trend
df.groupby('Year')['PM2.5'].mean().plot(kind='bar')
plt.title("Yearly Pollution Trend")
plt.xlabel("Year")
plt.ylabel("PM2.5")
plt.show()

# Step 10: Distribution
sns.histplot(df['PM2.5'], bins=50)
plt.title("PM2.5 Distribution")
plt.show()
df.to_csv("clean_air_data.csv", index=False)