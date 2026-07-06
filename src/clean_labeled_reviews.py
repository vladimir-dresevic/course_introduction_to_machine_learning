import pandas as pd

# Step 1: Load the labeled dataset
df = pd.read_csv("data/reviews_labeled.csv")


# Step 2: Drop rows with missing values
df = df.dropna()

# Step 3: Standardize sentiment column to lowercase
df['sentiment'] = df['sentiment'].str.strip().str.lower()


# Optional: Check unique values to confirm
print("Unique sentiment values after standardization:", df['sentiment'].unique())

# Step 4: Save the cleaned dataset
df.to_csv("data/reviews_labeled_cleaned.csv", index=False)


