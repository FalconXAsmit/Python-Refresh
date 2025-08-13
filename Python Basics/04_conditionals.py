# Conditional statements in Python
# ------------------------------------------------------------Basic weakness check for shadows------------------------------------------------------------------
# 'if' is used to run code ONLY when a certain condition is True.
# 'else' is the fallback. Its code runs only if the 'if' condition was False.
enemy_weakness = "Fire"
print("A shadow appears!")
if enemy_weakness == "Fire":
    print("The shadow is weak to fire! Use Agidyne!")
else:
    print("The shadow is not weak to fire. Use physical attacks.")

# But fights aren't like that shadows can have other weaknesses like ice, electric, wind, light, curse or even physical attacks and bosses have none so now lets make a better system.
# ---------------------------------------------------------A more complex weakness check for shadows-------------------------------------------------------------
# 'elif' stands for "else if". It lets you check for more conditions
# if the first 'if' was False. You can have as many 'elif's as you need.
# The final 'else' runs if NONE of the 'if' or 'elif' conditions were True.
enemy_weakness = "Curse"
if enemy_weakness == "Fire":
    print("Weak to Fire! Cast Agidyne!")
elif enemy_weakness == "Ice":
    print("Weak to Ice! Cast Bufudyne!")
elif enemy_weakness == "Elec":
    print("Weak to Elec! Cast Ziodyne!")
elif enemy_weakness == "Wind":
    print("Weak to Wind! Cast Garudyne!")
elif enemy_weakness == "Light":
    print("Weak to Light! Cast Hamaon!")
elif enemy_weakness == "Curse":
    print("Weak to Curse! Cast Mudo!")
elif enemy_weakness == "Physical":
    print("Weak to Physical! Use a Physical or Meele attack!")
else:
    # This runs if NONE of the above conditions were true
    print("No elemental weakness detected. Time for almighty attack.")

# ---------------------------------------------------------The pythonic way for checking party member------------------------------------------------------------
# In this example, we check if a character is in the party list.
# If they are, we print a message saying they are in the party.
party = ["Joker", "Ryuji", "Ann", "Makoto"]
characher_to_check = "Akechi"
# We can use the 'in' keyword to check if a character is in the party list.
# This is a more pythonic way to check membership in a list.
if characher_to_check in party:
    # This f"" is called a f-string, it allows to embed expressions inside string, using curly braces `{}`.
    print(f"{characher_to_check} is in the party.") 
else:
    print(f"{characher_to_check} is on standby.")
