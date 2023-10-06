import pandas as pd

data = {
    "CharacterName": ["Arwen", "Frodo", "Gimli", "Legolas"],
    "Terrain": ["Forest", "Mountain", "Swamp", "Village"],
    "Stamina": [100, 100, 100, 100]  # Assuming each character starts with 100 stamina
}

df = pd.DataFrame(data)

def stamina_adjustment(terrain):
    if terrain == 'Forest':
        return 10
    elif terrain == 'Mountain':
        return -20
    elif terrain == 'Swamp':
        return -30
    else:
        return 15

# Apply the stamina_adjustment function to (from?) the 'Terrain' column and set the data frame's stamina adjustment
df["Stamina Adjustment"] = df["Terrain"].apply(stamina_adjustment)

# Adjust the each character's Stamina column based on the Stamina Adjustment function (that was "saved in the previous step)
df["Stamina"] = df["Stamina Adjustment"] + df["Stamina"]

# print the results
print(df)
