import pandas as pd

data = {
    "CharacterName": ["Arwen", "Frodo", "Gimli", "Legolas"],
    "Terrain": ["Forest", "Mountain", "Swamp", "Village"],
    "Stamina": [100, 100, 100, 100]  # Assuming each character starts with 100 stamina
}
df = pd.DataFrame(data)

def stamina_adjust(terrain):

# Apply the stamina_adjustment function to (from?) the 'Terrain' column and set the data frame's stamina adjustment


df["Stamina Adjustment"] = df["Terrain"].apply(stamina_adjustment)

# Adjust the each character's Stamina column based on the Stamina Adjustment function (that was "saved in the previous step)


# print the results

print(df)