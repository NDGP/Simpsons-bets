const API_BASE = "http://127.0.0.1:8000";

export const createGame = async () => {
  return fetch(`${API_BASE}/create-game`, {
    method: "POST",
  });
};

export const getGameState = async () => {
  const res = await fetch(`${API_BASE}/game-state`);
  return res.json();
};

export const addPlayer = async (playerName) => {
  return fetch(`${API_BASE}/add-player`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ player_name: playerName }),
  });
};

export const removePlayer = async (playerName) => {
    return fetch(`${API_BASE}/remove-player`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ player_name: playerName }),
    });
};

export const setSeason = async (seasonNumber) => {
  return fetch(`${API_BASE}/set-season`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ season_number: seasonNumber }),
  });
};

export const selectCharacter = async (playerName, characterName) => {
  return fetch(`${API_BASE}/select-character`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      player_name: playerName,
      character_name: characterName,
    }),
  });
};