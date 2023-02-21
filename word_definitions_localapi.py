import os
import json

# Creates a list of dictionary files
def load_data_list(directory_path):
    data = []
    # Loop through the files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            # Build the full path to the file
            file_path = os.path.join(directory_path, filename)
            # Open the file
            with open(file_path, "r") as file:
                # Load the JSON data from file
                data.append(json.load(file))

    return data

def load_data_dict(directory_path):
    data = {}
    # Loop through the files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            # Build the full path to the file
            file_path = os.path.join(directory_path, filename)
            # Open the file
            with open(file_path, "r") as file:
                # Load the JSON data from file
                json_data = json.load(file)
                # Update the data dictionary with the loaded data
                data.update(json_data)

    return data


# Finds a word in a list of dictionaries and returns its info
def find_key(data, key):
    for dictionary in data:
        if key in dictionary:
            return dictionary[key]
            # return dictionary

# Extracts a specific property of a word
def get_property(word_info, property):
    word_property = word_info[property]
    return word_property

# Extracts the synonyms from the word info
def get_synonyms(word_info):
    synonyms = word_info["SYNONYMS"]
    return synonyms

def convert_to_dict(data):
    # Convert list to dictionary
    data_dict = {}
    for item in data:
        data_dict.update(item)

# Creates a list of a specific property of all words
def get_property_list(data, property):
    property_list = []
    for key in data.keys():
        meanings = data[key].get("MEANINGS", {})
        synonyms = meanings.get(property, [])
        property_list.extend(synonyms)
    return property_list

# Set the path to the directory containing the JSON files
directory_path = "semantic-primes/data"

# Load Data
data_list = load_data_list(directory_path)
data_dict = load_data_dict(directory_path)

# Choose Word
key = "SEE"

word_info = find_key(data_list, key)
word_synonyms = get_synonyms(word_info)
print(word_synonyms)