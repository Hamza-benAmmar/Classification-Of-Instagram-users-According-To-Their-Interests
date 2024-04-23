import pandas as pd

# Load your CSV dataset
df = pd.read_csv('datasetPfa.csv')  # Correct function for CSV files

# Print the first few rows to check the format
print(df.head())

# Initialize a dictionary to keep track of each user's interests
user_interests = {}

# Iterate over each column in the DataFrame
for interest in df.columns:
    # Convert all data to string type, replacing NaN with an empty string
    users = df[interest].fillna('').astype(str)

    # Clean up line breaks and split usernames assuming they are separated by commas
    users = users.apply(lambda x: x.replace('\r\n', ',').split(','))

    for user_list in users:
        for user in user_list:
            user = user.strip()  # Remove any surrounding whitespace
            if user:  # Ensure user is not empty
                if user in user_interests:
                    user_interests[user].append(interest)
                else:
                    user_interests[user] = [interest]

# Convert the dictionary to a DataFrame
interests_df = pd.DataFrame(list(user_interests.items()), columns=['Username', 'Interests'])
interests_df['Interests'] = interests_df['Interests'].apply(lambda x: ', '.join(x))  # Convert list to comma-separated string

# Save to a new CSV file
interests_df.to_csv('output_user_interests.csv', index=False)

