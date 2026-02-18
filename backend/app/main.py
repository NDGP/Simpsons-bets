from app.gameState import game_state, add_player, remove_player, set_season, set_episode, deselect_season, deselect_episode, select_character, start_round, end_round
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlayerRequest(BaseModel):
    player_name: str

class SeasonRequest(BaseModel):
    season_number: int

class EpisodeRequest(BaseModel):
    episode_number: int

class CharacterRequest(BaseModel):
    player_name: str
    character_name: str

# Endpoint to create a new game
@app.post("/create-game")
def create_game():
    print("Game created successfully")
    return {"message": "Game created successfully"}

# Endpoint to get the current game state
@app.get("/game-state")
def get_game_state():
    print("Current game state:")
    return game_state

# Endpoint to add a player  
@app.post("/add-player")
def add_player_endpoint(request: PlayerRequest):
    add_player(request.player_name)
    return {"message": f"Player {request.player_name} added successfully"}

# Endpoint to remove a player
@app.post("/remove-player")
def remove_player_endpoint(request: PlayerRequest):
    remove_player(request.player_name)
    return {"message": f"Player {request.player_name} removed successfully"}

# Endpoint to set the season
@app.post("/set-season")
def set_season_endpoint(request: SeasonRequest):
    set_season(request.season_number)
    return {"message": f"Season set to {request.season_number}"}

# Endpoint Remove the season
@app.post("/deselect-season")
def deselect_season_endpoint():
    deselect_season()
    return {"message": "Season deselected"}

# Endpoint to set the episode
@app.post("/set-episode")
def set_episode_endpoint(request: EpisodeRequest):
    set_episode(request.episode_number)
    return {"message": f"Episode set to {request.episode_number}"}

# Endpoint Remove the episode
@app.post("/deselect-episode")
def deselect_episode_endpoint():
    deselect_episode()
    return {"message": "Episode deselected"}

# Endpoint to select a character for a player
@app.post("/select-character")
def select_character_endpoint(request: CharacterRequest):
    select_character(request.player_name, request.character_name)
    return {"message": f"Player {request.player_name} selected character {request.character_name}"}

#endpoint remove a character for a player
@app.post("/deselect-character")
def deselect_character_endpoint(request: CharacterRequest):
    deselect_character(request.player_name, request.character_name)
    return {"message": f"Player {request.player_name} deselected character {request.character_name}"}

#start round
@app.post("/start-round")
def start_round_endpoint():
    start_round()
    return {"message": "Round started"}

#results/ reset round
@app.get("/results")
def get_results():
    return {"message": "Results retrieved successfully"}


