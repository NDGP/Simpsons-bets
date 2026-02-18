import { useState } from "react";
import { addPlayer, getGameState } from "../services/api";

// Component for adding players to the game
export default function PlayerSetup({ onPlayerAdded }) {
  const [name, setName] = useState("");

  const handleAdd = async () => {
    await addPlayer(name);

    const updatedState = await getGameState();

    onPlayerAdded(updatedState);  // send state back to Game

    setName(""); // clear input
  };
  

  return (
    <div>
      <h2>Add Player</h2>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter player name"
      />
      <button onClick={handleAdd}>Add Player</button>
    </div>
  );
}