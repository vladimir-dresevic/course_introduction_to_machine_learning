import pandas as pd

# Define simple keyword lists
positive_words = ["great", "excellent", "amazing", "love", "perfect", "good", "fantastic", "happy", "recommend"]
negative_words = ["bad", "terrible", "worst", "broken", "poor", "disappointed", "awful", "hate", "slow"]

# Define a simple rule-based sentiment classifier (binary only)
def classify_sentiment(text):
    text = str(text).lower()
    pos_hits = sum(word in text for word in positive_words)
    neg_hits = sum(word in text for word in negative_words)
    
    if pos_hits >= neg_hits:
        return "positive"
    else:
        return "negative"

# Load labeled dataset
df = pd.read_csv("data/reviews_labeled_cleaned.csv")

# Apply the classifier
df['predicted_sentiment'] = df['review'].apply(classify_sentiment)

# Save the results to a new CSV file
df.to_csv("data/reviews_with_predicted_sentiment.csv", index=False)


