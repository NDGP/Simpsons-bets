# game logic
import pandas as pd

relevant_characters = [
    "Abraham Jebediah Simpson",
    "Patty Bouvier",
    "Selma Bouvier",
    "Jacqueline Bouvier",
    "Mona Simpson",
    "Herbert Powell",
    "C. Montgomery Burns",
    "MR. Burns",
    "Waylon Smithers",
    "Nedward Flanders Jr.",
    "Maude Flanders",
    "Rod Flanders",
    "Todd Flanders",
    "Moe Szyslak",
    "Barney Gumble",
    "Seymour Skinner",
    "Edna Krabappel-Flanders",
    "Groundskeeper Willie",
    "Chief Clancy Wiggum",
    "Ralph Wiggum",
    "Eddie",
    "Lou",
    "Apu Nahasapeemapetilon",
    "Manjula Nahasapeemapetilon",
    "Milhouse Mussolini Van Houten",
    "Nelson Mandela Muntz",
    "Martin Prince",
    "Jimbo Jones",
    "Dolph Starbeam",
    "Kearney Zzyzwicz",
    "Sherri Mackleberry",
    "Terri Mackleberry",
    "Kent Brockman",
    "Reverend Timothy Lovejoy",
    "Mayor Joseph Quimby",
    "Lionel Hutz",
    "Blue-Haired Lawyer",
    "Jeff Albertson",
    "Dr. Julius Hibbert",
    "Dr. Nick Riviera",
    "Arnie Pye",
    "Troy McClure",
    "Gil Gunderson",
    "Hans Moleman",
    "Carl Carlson",
    "Lenny Leonard",
    "Sam",
    "Larry Dalrymple",
    "Disco Stu",
    "Otto Mann",
    "Cletus Delroy Spuckler",
    "Brandine Del Roy",
    "Captain Horatio McCallister",
    "Sideshow Bob",
    "Sideshow Mel",
    "Snake Jailbird",
    "Fat Tony",
    "Johnny Tightlips",
    "Louie",
    "Legs",
    "Patches",
    "Jub-Jub",
    "Lyle Lanley",
    "Hank Scorpio",
    "Frank Grimes",
    "Duffman",
    "Bumblebee Man",
    "The Rich Texan",
    "Professor John Frink",
    "Kang",
    "Kodos",
    "Superintendent Gary Chalmers",
    "Lunchlady Doris",
    "Janey Powell",
    "Üter Zörker",
    "Database",
    "Allison Taylor",
    "Wendell Borton",
    "Richard",
    "Lewis Clark",
    "Coach Krupt",
    "Agnes Skinner",
    "Helen Lovejoy",
    "Artie Ziff",
    "Cookie Kwan",
    "Declan Desmond",
    "Gabbo",
    "Krusty the Clown",
    "Squeaky-Voiced Teen",
    "Judge Roy Snyder",
    "Judge Constance Harm",
    "Drederick Tatum",
    "Rainier Wolfcastle",
    "Birch Barlow",
    "Princess Kashmir",
    "Don Vittorio DiMaggio",
    "Lucius Sweet",
    "Crazy Cat Lady",
    "Old Jewish Man",
    "Mrs. Muntz",
    "Dewey Largo",
    "Bleeding Gums Murphy",
    "Herman",
    "Akira",
    "Mrs. Hoover",
    "Gloria",
    "Luann Van Houten",
    "Dubya Spuckler",
    "Birthday Spuckler",
    "Whitney Spuckler"
]



game_state = {
    "players": {},
    "season": 1,
    "episode": 1,
    "round": 0,
}

#season logic
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

# Player management
def add_player(player_name):
    game_state["players"][player_name] = {
        "id": len(game_state["players"]) + 1,
        "score": 0,
        "wins": 0,
        "character_choices": {}
    }
    print(f"{player_name} added")

def remove_player(player_name):
    if player_name in game_state["players"]:
        del game_state["players"][player_name]
        print(f"{player_name} removed")
    else:
        print(f"{player_name} not found")



#season management
ep_count = len(df_filtered_episode_ids_in_season)

def set_season(season_number):
    if season_number < 1 or season_number > 12:
        print("Invalid season number. Please choose between 1 and 12.")
    else:
        game_state["season"] = season_number
        print(f"Season set to {season_number}")

def set_episode(episode_number):
    if episode_number < 1 or episode_number > ep_count:
        print(f"Invalid episode number. Please choose between 1 and {ep_count}.")
    else:
        game_state["episode"] = episode_number
        print(f"Episode set to {episode_number}")

def deselect_season():
    game_state["season"] = None
    game_state["episode"] = None
    game_state["players"] = {player: {"id": game_state["players"][player]["id"], "score": 0, "character_choices": {}} for player in game_state["players"]}
    print("Season deselected")
def deselect_episode():
    game_state["episode"] = None
    print("Episode deselected")

#caricter management
def select_character(player_name, character_name):
    if player_name not in game_state["players"]:
        print(f"{player_name} not found")
        return
    
    if character_name not in relevant_characters:
        print(f"{character_name} is not a relevant character for this season")
        return
    
    character_info = df_character_episode_counts[df_character_episode_counts['raw_character_text'] == character_name]
    
    if character_info.empty:
        print(f"No episode count found for {character_name}")
        return
    
    rarity_score = character_info['rarity_score'].values[0]
    
    game_state["players"][player_name]["character_choices"][character_name] = {
        "picked": True,
        "character_id": None,  # This can be filled in with actual character ID if needed
        "rarity_score": rarity_score
    }
    
    print(f"{player_name} selected {character_name} with rarity score {rarity_score}")

def deselect_character(player_name, character_name):
    if player_name not in game_state["players"]:
        print(f"{player_name} not found")
        return

    if character_name not in game_state["players"][player_name]["character_choices"]:
        print(f"{character_name} is not selected by {player_name}")
        return

    del game_state["players"][player_name]["character_choices"][character_name]
    print(f"{player_name} deselected {character_name}")

#game play
def start_round():
    game_state["round"] += 1
    print(f"Round {game_state['round']} started")

def end_round():
    print(f"Round {game_state['round']} ended")
    # Here you can add logic to calculate scores based on selected characters and update game_state["players"][player_name]["score"] accordingly
    for player, data in game_state["players"].items():
        for character, info in data["character_choices"].items():
            # Example scoring logic based on rarity
            game_state["players"][player]["score"] += info["rarity_score"]

    print("Scores updated:")
    tie = len(set(data["score"] for data in game_state["players"].values())) == 1
    if tie:
        print("It's a tie!")
        return
    for player, data in game_state["players"].items():
        print(f"{player}: {data['score']}")
    winner = max(game_state["players"], key=lambda p: game_state["players"][p]["score"])
    print(f"Winner: {winner}")
    game_state["players"][winner]["wins"] += 1
    for player, data in game_state["players"].items():
        data["score"] = 0

    print("Scores reset.")


add_player("Alice")
add_player("Bob")
select_character("Alice", "Apu Nahasapeemapetilon")
select_character("Bob", "Moe Szyslak")  
set_season(3)
set_episode(5)
start_round()
end_round()
