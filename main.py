import pandas as pd

# load data
df = pd.read_csv("./data/train.csv")

# check if data loaded correctly
print("Top 5 rows:\n", df.head())

# analyse the data
print("Shape:", df.shape)

# columns
print("\nColumns:")
print(df.columns.tolist())

# Data type
print("\nDatatype:")
print(df.dtypes)

# finding the missing value
print("\nFinding missing values")
print(df.isnull().sum())

# statistics
print("\nStatistics:")
print(df.describe())

# You're trying to answer:

# How many rows are there?
# How many columns?
# Which columns are numerical?
# Which columns are categorical?
# Which columns have missing values?
# What does SalePrice look like?

# Don't preprocess anything yet.
