import requests
import json

# Word
my_word = "watch"

# Get Info
req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{my_word}")

# Print full requested data for the word
print(req.text)

# Convert to JSON
data = req.json()

# Access the first item in the list, since it only contains one item
word_data = data[0]

# Access the "meanings" list
meanings = word_data["meanings"]

# Access the first item in the "meanings" list
first_meaning = meanings[0]

# Access the "definitions" list within the first meaning
definitions = first_meaning["definitions"]

# Access the first item in the "definitions" list
first_definition = definitions[1]

# Access the "synonyms" list within the first definition
synonyms = first_definition["synonyms"]

# Print the list of synonyms
print(synonyms)