import json
import pandas as pd

DATA_IN  = r'C:\Users\gaelm\OneDrive\Documents\Spring 2026\IT 485\rentwise-classifier\data\apt_reviews_massachusetts.json'
DATA_OUT = r'C:\Users\gaelm\OneDrive\Documents\Spring 2026\IT 485\rentwise-classifier\data\apt_reviews_features.json'

with open(DATA_IN, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)
df['time'] = pd.to_datetime(df['time'], unit='ms')
df['text'] = df['text'].fillna('')

# Feature 1: review length
df['word_count'] = df['text'].str.split().str.len()

# Feature 2: has photos
df['has_photos'] = df['pics'].apply(lambda x: 1 if x and len(x) > 0 else 0)

# Feature 3: recency (days since oldest review)
df['recency_days'] = (df['time'] - df['time'].min()).dt.days

# Feature 4: has business response
df['has_response'] = df['resp'].notna().astype(int)

# Feature 5: rating extremity (1 or 5 vs middle)
df['is_extreme_rating'] = df['rating'].apply(lambda x: 1 if x in [1, 5] else 0)

# Composite helpfulness score (0-5)
df['helpfulness_score'] = (
    (df['word_count'] >= 50).astype(int) +
    df['has_photos'] +
    (df['recency_days'] >= 365).astype(int) +
    df['has_response'] +
    df['is_extreme_rating']
)

print("Helpfulness score distribution:")
print(df['helpfulness_score'].value_counts().sort_index())

df.to_json(DATA_OUT, orient='records', date_format='iso')
print("\nSaved to apt_reviews_features.json")
