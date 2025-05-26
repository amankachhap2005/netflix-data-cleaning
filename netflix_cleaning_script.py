
import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")  # Make sure this file is in the same folder

# Show initial info
print("Original data shape:", df.shape)

# 1. Drop duplicates
df = df.drop_duplicates()

# 2. Handle missing values
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 3. Standardize text formatting
df['title'] = df['title'].str.strip()
df['country'] = df['country'].str.title()
df['rating'] = df['rating'].str.upper()

# 4. Rename columns to snake_case
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 5. Filter out rows with missing or incorrect release_year
df = df[df['release_year'].notnull()]
df['release_year'] = df['release_year'].astype(int)

# 6. Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("Cleaned data shape:", df.shape)
print("Cleaning complete. File saved as 'cleaned_netflix_data.csv'")
