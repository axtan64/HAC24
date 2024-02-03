import './App.css';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';

import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  return ( 
    <div className="App">
      <button>Button 1</button>
      <button>Button 2</button>
      <button>Button 3</button>
    </div>
  )
}

export default App;
