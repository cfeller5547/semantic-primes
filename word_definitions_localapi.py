import json

file_path = "C:/Users/Client/Desktop/Semantic Primes AI/semantic-primes/data/DA.json"

# Open the file
with open(file_path, "r") as file:
    # Load the JSON data from file
    data = json.load(file)

# Access elements in the JSON data
word = data["ABATE"]
synonyms = word["SYNONYMS"]
synonym1 = synonyms[1]
print(synonym1)
# print(data["ABATE"])
print(data["ABATE"]["SYNONYMS"])