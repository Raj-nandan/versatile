import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
// import logo from '../images/logo.png'

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
       <h2>Bright Hands</h2>
        </Link>
        <div className="navbar-menu">
          <Link to="/" className="navbar-item">Home</Link>
          <Link to="/translate" className="navbar-item">Translate</Link>
          <Link to="/learn" className="navbar-item">Learn</Link>
          <Link to="/board" className="navbar-item">WhiteBoard</Link>
        </div>
        <Link to="/convert" className="navbar-item">Converter</Link>
      </div>
    </nav>
  );
}

export default Navbar;