import pandas as pd
from gameState import game_state, relevant_characters
from kaggle.api.kaggle_api_extended import KaggleApi    
api = KaggleApi()

df_episodes = pd.read_csv("data/episodes.csv")
df_characters = pd.read_csv("data/characters.csv")
df_scripts = pd.read_csv("data/script_lines.csv")

df_filtered_episode_ids_in_season = df_episodes[df_episodes['season'] == game_state['season']]['id'].values

df_scripts_in_season = df_scripts[df_scripts['episode_id'].isin(df_filtered_episode_ids_in_season)]


#list of characters in season and how many episodes they appear in
# Step 3: Count UNIQUE episodes per relevant character only
df_character_episode_counts = (
    df_scripts_in_season[
        df_scripts_in_season['raw_character_text'].isin(relevant_characters)
    ]
    .groupby('raw_character_text')['episode_id']
    .nunique()
    .reset_index(name='episode_count')
    .sort_values(by='episode_count', ascending=False)
)

def calculate_rarity(count):
    if count == 1:
        return 10
    elif 2 <= count <= 3:
        return 5
    elif 4 <= count <= 6:
        return 3
    else:  # >= 8
        return 1
    
df_character_episode_counts['rarity_score'] = df_character_episode_counts['episode_count'].apply(calculate_rarity)
print(df_character_episode_counts)