import requests

# Word
my_word = "apple"

# Get Info
req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{my_word}")

# Print result
print(req.text)