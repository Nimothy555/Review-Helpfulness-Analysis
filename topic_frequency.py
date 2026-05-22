import json
import pandas as pd

with open(r'C:\Users\gaelm\OneDrive\Documents\Spring 2026\IT 485\rentwise-classifier\data\apt_reviews_features.json', 'r',
encoding="utf-8") as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)
df['text'] = df['text'].fillna(" ")

keywords = [
    'maintenance', 'noise', 'parking', 'heat', 'water',
    'roaches', 'landlord', 'management', 'staff', 'clean',
    'safe', 'quiet', 'mold', 'pest', 'gym'
]

results = []
for kw in keywords:
    for rating in [1, 2, 3, 4, 5]:
        subset = df[df['rating'] == rating]
        count = subset['text'].str.lower().str.contains(kw).sum()
        pct = count / len(subset) * 100
        results.append({'keyword': kw, 'rating': rating, 'pct': pct})

kw_df = pd.DataFrame(results)
print(kw_df.pivot(index='keyword', columns='rating', values='pct').round(2))

import matplotlib.pyplot as plt
import seaborn as sns

pivot = kw_df.pivot(index="keyword" , columns="rating",
values="pct")

plt.figure(figsize=(10,7))
sns.heatmap(pivot, annot=True, fmt='.1f', cmap='YlOrRd')
plt.title("Keyword Frequency by Rating (% of reviews)")
plt.savefig("topic_heatmap.png")
plt.close()
print("Saved topic_heatmap.png")
