// src/pages/Search.js
import React, { useState } from 'react';
import '../styles/Search.css';

const Search = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);

    // Sample data (mimicking items or images that can be searched)
    const items = [
        { id: 1, name: 'Apple', image: '/images/apple.jpg' },
        { id: 2, name: 'Banana', image: '/images/banana.jpg' },
        { id: 3, name: 'Orange', image: '/images/orange.jpg' },
        { id: 4, name: 'Mango', image: '/images/mango.jpg' },
        { id: 5, name: 'Pineapple', image: '/images/pineapple.jpg' },
        { id: 6, name: 'Strawberry', image: '/images/strawberry.jpg' },
        { id: 7, name: 'Grapes', image: '/images/grapes.jpg' },
        { id: 8, name: 'Peach', image: '/images/peach.jpg' },
        { id: 9, name: 'Cherry', image: '/images/cherry.jpg' },
    ];

    const handleSearch = () => {
        const filteredResults = items.filter(item =>
            item.name.toLowerCase().includes(query.toLowerCase())
        );
        setResults(filteredResults);
    };

    return (
        <div className="search-container">
            <h1></h1>

            {/* Search Input */}
            <div className="search-bar">
                <input
                    type="text"
                    placeholder="Search for the artist, name of the piece, or time period  ..."
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                />
                <button onClick={handleSearch}>Search</button>
            </div>

            {/* Display Results */}
            <div className="results-container">
                {results.length === 0 ? (
                    <p>We found no matches.</p>
                ) : (
                    <div className="images-container">
                        {results.map(item => (
                            <div key={item.id} className="image-item">
                                <img src={item.image} alt={item.name} className="image" />
                                <p>{item.name}</p>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Search;
