import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path=r"C:\Users\Adithyan\Downloads\oops\Demon Slayer.csv"
data = pd.read_csv(file_path)
print(data.head())
print(data.info())
print(data.tail())
status_counts = data['Status'].value_counts()
print("✅ Count of characters by Status:")
print(status_counts)

plt.figure(figsize=(6,4))
status_counts.plot(kind='bar', color=['red', 'green'])
plot_no = 1
plt.title(f'{plot_no}. Number of Characters by Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
plot_no += 1

gender_counts = data['Gender'].value_counts()
print(gender_counts)

plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['green', 'pink'])
plt.show()
plot_no += 1

race_count = data['Race'].value_counts()
print(race_count)

plt.figure(figsize=(6,4))
race_count.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title(f'{plot_no}. Count of Characters by Race', fontsize=14, weight='bold')
plt.xlabel("Race")
plt.ylabel("Number of Characters")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
plot_no += 1

breathing_count = data['Breathing_Style'].value_counts()
breathing_count = breathing_count[breathing_count.index != 'None']

plt.figure(figsize=(8,5))
breathing_count.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title(f"{plot_no}. Count of Characters by Breathing Style", fontsize=14, weight='bold')
plt.xlabel("Breathing Style")
plt.ylabel("Number of Characters")
plt.xticks(rotation=90)
plt.show()
plot_no += 1

filtered_df = data[data['Voice_Actor_Japanese'] != 'None']
top_10_va = (
    filtered_df['Voice_Actor_Japanese']
    .value_counts()
    .head(10)
    .index
)
filtered_df = filtered_df[filtered_df['Voice_Actor_Japanese'].isin(top_10_va)]
plt.figure(figsize=(10,6))
sns.countplot(
    data=filtered_df,
    y='Voice_Actor_Japanese',   # Flip axis for readability
    order=top_10_va, 
    palette="viridis"
)
plt.title(f"{plot_no}. Top 10 Japanese Voice Actors in Demon Slayer", fontsize=16, weight='bold', pad=15)
plt.xlabel("Number of Characters", fontsize=12)
plt.ylabel("Voice Actor (Japanese)", fontsize=12)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

sns.despine()

plt.show()
