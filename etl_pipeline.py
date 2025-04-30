import pandas as pd

# Step 1: Extract
def extract():
    df = pd.read_csv("sample_data.csv")
    print("Extracted data:")
    print(df)
    return df

# Step 2: Transform
def transform(df):
    df["name"] = df["name"].str.upper()  # convert names to uppercase
    print("Transformed data:")
    print(df)
    return df

# Step 3: Load
def load(df):
    df.to_csv("output_data.csv", index=False)
    print("Data loaded to output_data.csv")

# Run ETL
if __name__ == "__main__":
    data = extract()
    data = transform(data)
    load(data)
