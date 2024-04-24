import csv
import json

# Define mappings between subinterests and main interests
subinterests_to_maininterests = {
    'social media': 'Business and Industry',
    'Health care': 'Business and Industry',
    'Business': 'Business and Industry',
    'movies': 'Entertainment',
    'live events': 'Entertainment',
    'Games': 'Entertainment',
    'music': 'Entertainment',
    'reading': 'Entertainment',
    'tv and series': 'Entertainment',
    'family': 'family and relationships',
    'parenting': 'family and relationships',
    'dating and mariage': 'family and relationships',
    'bodybuilding': 'fitness and wellness',
    'Physical exercise': 'fitness and wellness',
    'yoga': 'fitness and wellness',
    'running': 'fitness and wellness',
    'beverages': 'food and drink',
    'alcoholic beverages': 'food and drink',
    'cooking and cuisine': 'food and drink',
    'food and restaurants': 'food and drink',
    'art and music': 'hobbies and activities',
    'current event homes and garden': 'hobbies and activities',
    'pets': 'hobbies and activities',
    'political and social issues': 'hobbies and activities',
    'travel': 'hobbies and activities',
    'vehicles': 'hobbies and activities',
    'beauty': 'shopping and fashion',
    'clothing': 'shopping and fashion',
    'fashion accessories': 'shopping and fashion',
    'shopping': 'shopping and fashion',
    'toys': 'shopping and fashion',
    'american football': 'sports',
    'football/soccer': 'sports',
    'baseball': 'sports',
    'basketball': 'sports',
    'golf': 'sports',
    'marathon': 'sports',
    'Auto racing': 'sports',
    'skiing': 'sports',
    'swimming': 'sports',
    'tennis': 'sports',
    'volleyball': 'sports',
    'handball': 'sports',
    'camping': 'Outdoors',
    'fishing': 'Outdoors',
    'horseback riding': 'Outdoors',
    'hiking': 'Outdoors',
    'computers': 'Technology',
    'consumer electronics': 'Technology'
}

# Function to rearrange the CSV data into the desired JSON format
def rearrange_csv_to_json(input_csv_file, output_json_file):
    user_interests_dict = {}

    # Open the CSV file and read its contents
    with open(input_csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['Username'].strip()
            sub_interests = [interest.strip() for interest in row['Interests'].split(',')]
            user_interests = {}
            for sub_interest in sub_interests:
                main_interest = subinterests_to_maininterests.get(sub_interest)
                if main_interest:
                    if main_interest in user_interests:
                        user_interests[main_interest].append(sub_interest)
                    else:
                        user_interests[main_interest] = [sub_interest]
            user_interests_dict[username] = user_interests

    # Write the rearranged data to a JSON file
    with open(output_json_file, 'w') as jsonfile:
        json.dump(user_interests_dict, jsonfile, indent=4)

# Call the function with your input and output file paths
rearrange_csv_to_json('output_user_interests.csv', 'output_interests.json')


