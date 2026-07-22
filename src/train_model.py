import joblib

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# load the labeled dataset
df = pd.read_csv("data/reviews_labeled_cleaned.csv")

# separate features and target
X = df['review']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# vectorize all input reviews
vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
X_train_tfidf = vectorizer.fit_transform(X_train)

# train the logistic regresion model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

joblib.dump(model, "model/sentiment_model.joblib")
joblib.dump(vectorizer, "model/tfidf_vectorizer.joblib")

print("Model and vectorizer are saved.")

