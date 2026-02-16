from gameState import game_state, add_player, remove_player, set_season, set_episode, deselect_season, deselect_episode, select_character, start_round, end_round
from fastapi import FastAPI

app = FastAPI()
# Endpoint to create a new game
@app.post("/CreateGame")
def create_game():
    print("Game created successfully")
    return {"message": "Game created successfully"}

# Endpoint to get the current game state
@app.get("/GameState")
def get_game_state():
    print("Current game state:")
    return game_state

# Endpoint to add a player
@app.post("/AddPlayer")
def add_player_endpoint(player_name: str):
    add_player(player_name)
    return {"message": f"Player {player_name} added successfully"}

# Endpoint to remove a player
@app.post("/RemovePlayer")
def remove_player_endpoint(player_name: str):
    remove_player(player_name)
    return {"message": f"Player {player_name} removed successfully"}

# Endpoint to set the season
@app.post("/SetSeason")
def set_season_endpoint(season_number: int):
    set_season(season_number)
    return {"message": f"Season set to {season_number}"}

# Endpoint Remove the season
@app.post("/DeselectSeason")
def deselect_season_endpoint():
    deselect_season()
    return {"message": "Season deselected"}

# Endpoint to set the episode
@app.post("/SetEpisode")
def set_episode_endpoint(episode_number: int):
    set_episode(episode_number)
    return {"message": f"Episode set to {episode_number}"}

# Endpoint Remove the episode
@app.post("/DeselectEpisode")
def deselect_episode_endpoint():
    deselect_episode()
    return {"message": "Episode deselected"}

# Endpoint to select a character for a player
@app.post("/SelectCharacter")
def select_character_endpoint(player_name: str, character_name: str):
    select_character(player_name, character_name)
    return {"message": f"Player {player_name} selected character {character_name}"}

#endpoint remove a character for a player
@app.post("/DeselectCharacter")
def deselect_character_endpoint(player_name: str, character_name: str):
    deselect_character(player_name, character_name)
    return {"message": f"Player {player_name} deselected character {character_name}"}

#start round
@app.post("/StartRound")
def start_round_endpoint():
    start_round()
    return {"message": "Round started"}

#results/ reset round
@app.get("/Results")
def get_results():
    return {"message": "Results retrieved successfully"}
