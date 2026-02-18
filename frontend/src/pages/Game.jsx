import { useState, useEffect } from "react";
import PlayerSetup from "../components/PlayerSetup";
import SeasonPicker from "../components/SeasonPicker";
import { getGameState, removePlayer } from "../services/api";

export default function Game() {
  const [gameState, setGameState] = useState(null);

  useEffect(() => {
    const loadGame = async () => {
      const state = await getGameState();
      setGameState(state);
    };
    loadGame();
  }, []);

  // Function to remove player directly from Game.jsx
  const handleRemovePlayer = async (playerName) => {
    await removePlayer(playerName);

    const updatedState = await getGameState();
    setGameState(updatedState);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "sans-serif" }}>
      <h1>Simpsons Game</h1>

      {/* Player Setup Component */}
      <PlayerSetup onPlayerAdded={setGameState} />

      {/* Show current players */}
      {gameState &&
        gameState.players &&
        gameState.season &&
        Object.keys(gameState.players).length > 0 && (
          <div>
            <div style={{ marginTop: "20px" }}>
              <h2>Current Players:</h2>
              <ul>
                {Object.keys(gameState.players).map((player) => (
                  <li
                    key={player}
                    style={{ display: "flex", alignItems: "center" }}
                  >
                    {player}
                    <button
                      onClick={() => handleRemovePlayer(player)}
                      style={{
                        marginLeft: "10px",
                        background: "red",
                        color: "white",
                        border: "none",
                        borderRadius: "50%",
                        width: "20px",
                        height: "20px",
                        cursor: "pointer",
                      }}
                    >
                      X
                    </button>
                  </li>
                ))}
              </ul>
            </div>
            <div style={{ marginTop: "20px" }}>
              <h2>Selected Season: {gameState.season}</h2>
            </div>
          </div>
        )}
    </div>
  );
} 