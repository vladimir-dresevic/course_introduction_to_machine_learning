import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')

# Define a simple rule-based sentiment classifier (binary only)
def classify_sentiment(text):

    text = str(text).lower()
    result = SentimentIntensityAnalyzer().polarity_scores(text)

    
    if result["compound"] >= 0:
        return "positive"
    else:
        return "negative"

# Load labeled dataset
df = pd.read_csv("data/reviews_labeled_cleaned.csv")

# Apply the classifier
df['predicted_sentiment'] = df['review'].apply(classify_sentiment)

# Save the results to a new CSV file
df.to_csv("data/reviews_with_predicted_sentiment_vader.csv", index=False)


