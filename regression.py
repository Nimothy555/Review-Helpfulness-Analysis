import json
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

with open(r'C:\Users\gaelm\OneDrive\Documents\Spring 2026\IT 485\rentwise-classifier\data\apt_reviews_features.json', 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)

# Define features and target
X = df[['word_count', 'has_photos', 'recency_days', 'has_response', 'is_extreme_rating']]
y = (df['helpfulness_score'] >= 3).astype(int)  # 1 = helpful, 0 = not helpful

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Feature importance
coefficients = pd.Series(model.coef_[0], index=X.columns)
print("\nFeature coefficients:")
print(coefficients.sort_values(ascending=False))

import matplotlib.pyplot as plt

coefficients.sort_values().plot(kind='barh', color='steelblue')
plt.title('Feature Coefficients — Logistic Regression')
plt.xlabel('Coefficient Value')
plt.tight_layout()
plt.savefig('feature_coefficients.png')
plt.close()
print("Saved feature_coefficients.png")
