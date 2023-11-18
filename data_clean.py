import pandas as pd

# Read the CSV file
df = pd.read_csv('sales_data.csv')

# Replace 'N/A' with 0
df = df.replace('N/A', 0)

# Function to remove 'm' and convert to float
def convert_sales(value):
    if isinstance(value, str):
        return float(value.replace('m', '')) if 'm' in value else float(value)
    return value

# Apply this function to all sales columns
for col in ['Total Sales', 'NA Sales', 'PAL Sales', 'Japan Sales', 'Other Sales']:
    df[col] = df[col].apply(convert_sales)

# Now, create a dictionary for each unique genre
genre_data = {}
for genre in df['Genre'].unique():
    genre_group = df[df['Genre'] == genre]
    
    # Initialize the genre object with empty lists
    genre_object = {
        "Console": [],
        "Total Sales": [],
        "NA Sales": [],
        "PAL Sales": [],
        "Japan Sales": [],
        "Other Sales": []
    }
    
    # Loop through each row in the genre group to fill the lists
    for _, row in genre_group.iterrows():
        genre_object["Console"].append(row["Console"])
        genre_object["Total Sales"].append(row["Total Sales"])
        genre_object["NA Sales"].append(row["NA Sales"])
        genre_object["PAL Sales"].append(row["PAL Sales"])
        genre_object["Japan Sales"].append(row["Japan Sales"])
        genre_object["Other Sales"].append(row["Other Sales"])
    
    # Assign the object to the genre key
    genre_data[genre] = genre_object


# Loop through each genre in the genre_data
for genre, data in genre_data.items():
    # Loop through each key in the data dictionary
    for key, values in data.items():
        # Replace 'nan' with 0.0 in the list of values
        data[key] = [0.0 if pd.isna(value) else value for value in values]



# Now you have a dictionary of genres, each containing its own dictionary of sales data
# Here's how you can access the data for a specific genre, like "Party"
# party_data = genre_data.get("Role-Playing", {})
# print(party_data)

# Initialize a new dictionary to hold the totals
genre_totals = {}

# Loop through each genre in the original data
for genre, data in genre_data.items():
    # Initialize a new dictionary to hold the totals for this genre
    totals = {}
    
    # Loop through each key in the data dictionary
    for key, values in data.items():
        # Sum the values for this key, ensuring to convert all non-numeric to 0.0
        if key != "Console":
            totals[key] = sum([float(value) if not pd.isna(value) else 0.0 for value in values])
    
    # Assign the totals dictionary to the current genre in the new genre_totals dictionary
    genre_totals[genre] = totals


genre = []
for key in genre_totals:
    genre.append(key)
genre.pop

# party_data = genre_totals.get("Role-Playing", {})
# print(party_data)

na_sales = 0
pal_sales = 0
japan_sales = 0
other_sales = 0
for i in range(len(genre)):
    data = genre_totals.get(genre[i], {})
    
    na_sales += data["NA Sales"]
    pal_sales += data["PAL Sales"]
    japan_sales += data["Japan Sales"]
    other_sales += data["Other Sales"]

    # print(genre[i], data, "\n")


print(na_sales)
print(pal_sales)
print(japan_sales)
print(other_sales)