import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/Login';
import Home from './pages/Home';
import Header from "./components/header";  // Import the Login component
import './App.css';
import Search from "./pages/Search";
import Suggest from "./pages/Suggest";
function App() {
    return (
        <Router>
                <Header/>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path = "/search" element={<Search />} /> {/* Updated route to use Search */}
                    <Route path = "/suggest" element={<Suggest />} /> {/* Updated route to use Suggest */}
                </Routes>
        </Router>

    );
}

export default App;



//**<Router> {/* Wrap the app in a Router */}
//                         <Routes>
//                             <Route path="/" element={<Header />} /> {/* Route for the home page */}
//                             <Route path="/login" element={<Login />} /> {/* Route for the login page */}
//                             {/* Add more routes as needed */}
//                         </Routes>
//                     </Router>