import React, { useState } from "react";
import "../styles/Search.css";

const Search = () => {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    const [error, setError] = useState("");

    const handleSearch = async () => {
        try {
            const response = await fetch(`/api/art/search?query=${query}`);
            if (!response.ok) {
                throw new Error("No results found.");
            }
            const data = await response.json();
            setResults(data);
            setError("");
        } catch (err) {
            setResults([]);
            setError(err.message);
        }
    };

    return (
        <div className="search-container">
            <h1>Search Art Pieces</h1>
            <div className="search-bar">
                <input
                    type="text"
                    placeholder="Search for the artist, name of the piece, or time period..."
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                />
                <button onClick={handleSearch}>Search</button>
            </div>
            {error && <p className="error">{error}</p>}
            <div className="results-container">
                {results.length > 0 && (
                    <div className="images-container">
                        {results.map((item) => (
                            <div key={item.id} className="image-item">
                                <img src={item.Image} alt={item.Title} className="image" />
                                <p>{item.Title}</p>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Search;
