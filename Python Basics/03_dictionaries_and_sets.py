# A dictionary in Python is a collection of key-value pairs.
# Each key is unique and is used to access its corresponding value. Dictionaries are mutable, unordered (as of Python 3.6+ they maintain insertion order), and are defined using curly braces {}.
character_stats = {
    "name": "Joker",
    "level": 75,
    "class": "Trickster",
    "pesona": "Arsene",
    "skills": ["Cleave", "Apt Pupil", "Counter"],  # skills are stored as a list
    "HP": 500,
    "SP": 500,
}

# Accessing values in a dictionary is done using the key. 
print(character_stats["name"])  # Output: Joker
# We can also use the get method to avoid KeyError if the key does not exist.
print(character_stats.get("name"))  # Output: Joker

# Add a new key-value pair to the dictionary.
character_stats["weapon"] = "Knife"

# Update an existing key-value pair.
character_stats["level"] = 80

# Some common dictionary methods:
print(character_stats.keys())  # Output: dict_keys(['name', 'level', 'class', 'pesona', 'skills', 'HP', 'SP', 'weapon'])
print(character_stats.values())  # Output: dict_values(['Joker', 80, 'Trickster', 'Arsene', ['Cleave', 'Apt Pupil', 'Counter'], 500, 500, 'Knife'])
print(character_stats.items())  # Output: dict_items([('name', 'Joker'), ('level', 80), ('class', 'Trickster'), ('pesona', 'Arsene'), ('skills', ['Cleave', 'Apt Pupil', 'Counter']), ('HP', 500), ('SP', 500), ('weapon', 'Knife')])

# To remove a key-value pair, use the del statement or pop method.
del character_stats["SP"]  # Removes the 'SP' key-value pair
character_stats.pop("HP")  # Removes the 'HP' key-value pair and returns its value

# Sets in Python are collections of unique elements. They are unordered and mutable, defined using curly braces {} or the set() constructor.
unique_skills = {"Cleave", "Apt Pupil", "Counter", "Cleave"}  # 'Cleave' will only appear once in the set
print(unique_skills)  # Output: {'Cleave', 'Apt Pupil', 'Counter'}

# Using common set methods:
unique_skills.add("Baton Pass")  # Adds a new skill to the set
unique_skills.remove("Cleave")  # Removes 'Cleave' from the set
print(unique_skills)  # Output: {'Apt Pupil', 'Counter', 'Baton Pass'}

# Check for membership in a set using the 'in' keyword.
if "Counter" in unique_skills:
    print("Counter skill is available.")  # Output: Counter skill is available.