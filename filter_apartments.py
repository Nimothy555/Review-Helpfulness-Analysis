import json

def parse(path):
    with open(path, 'r', encoding='utf-8') as f:
        for l in f:
            yield json.loads(l)

# Keep only apartment/residential businesses
apt_keywords = ['apartment', 'apartments', 'realty', 'rental', 'residential', 'housing']

apt_ids = set()
for meta in parse('data/meta-Massachusetts.json'):
    cats = [c.lower() for c in (meta.get('category') or [])]
    if any(k in ' '.join(cats) for k in apt_keywords):
        apt_ids.add(meta['gmap_id'])

print(f"Apartment businesses: {len(apt_ids)}")

apt_reviews = []
for review in parse('data/review-Massachusetts.json'):
    if review['gmap_id'] in apt_ids:
        apt_reviews.append(review)

print(f"Apartment reviews: {len(apt_reviews)}")

with open('data/apt_reviews_massachusetts.json', 'w', encoding='utf-8') as f:
    json.dump(apt_reviews, f)

print("Saved to data/apt_reviews_massachusetts.json")
