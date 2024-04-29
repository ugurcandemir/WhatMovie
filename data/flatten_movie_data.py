# In this script we fetch a random set of movies based on pupularity to be used later on.

import json
import json
import pandas as pd


with open("data/movie_info.json" , "r" , encoding= 'utf-8') as f :
    movie_info_data = json.load(f)

def flatten_json(json_data, prefix=''):
    """
    Flatten a nested JSON into a pandas DataFrame by adding underscores
    after each step of going deep.
    
    Args:
        json_data (dict): Nested JSON data.
        prefix (str): Prefix to be added to column names.
        
    Returns:
        pd.DataFrame: Flattened DataFrame.
    """
    flattened_data = {}

    for key, value in json_data.items():
        new_key = prefix + '_' + key if prefix else key

        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, new_key))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    flattened_data.update(flatten_json(item, f"{new_key}_{i+1}"))
                else:
                    flattened_data[f"{new_key}_{i+1}"] = item
        elif isinstance(value, str):  # Add this condition to handle string values
            flattened_data[new_key] = value
        else:
            flattened_data[new_key] = value

    return flattened_data


# Convert each item in movie_info_data to a DataFrame
dfs = []
for item in movie_info_data:
    flattened_data = flatten_json(item)
    df = pd.DataFrame([flattened_data])
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Display the final DataFrame
print(final_df)

# Save the final DataFrame as a CSV file
final_df.to_csv("data/final_movie_data.csv", index=False)

print("final_movie_data.csv saved successfully.")