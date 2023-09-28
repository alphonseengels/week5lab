import pandas as pd


player_data = {
    "PlayerName": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "XP Earned": [80, 150, 50, 600, 400, 750]
}
df = pd.DataFrame(player_data)

# Function to determine the number of health potions
def assign_potions(xp):
    if xp < 100:
        return 1
    elif 100 <= xp <= 500:
        return 3
    else:
        return 5

# Function to determine if the player gets a Golden Elixir
def assign_elixir(xp):
    return xp > 700

df["Health Potions"] = df["XP Earned"].apply(assign_potions)
df["Golden Elixir"] = df["XP Earned"].apply(assign_elixir)

print(df)


