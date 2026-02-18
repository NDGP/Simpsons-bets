import {useState} from "react";
import { setSeason } from "../services/api";

export default function SeasonPicker({ onSeasonSelected }) {
    const [season, setSeasonNumber] = useState("");
 
    const handleSelect = async () => {
        await setSeason(season);

        onSeasonSelected(season);  
        setSeasonNumber("");
    }

    return (
        <div>
            <h2>Select Season</h2>
            <input
                value={season}
                onChange={(e) => setSeasonNumber(e.target.value)}
                placeholder="Enter season number"
            />
            <button onClick={handleSelect}>Select Season</button>
        </div>
    );
}
