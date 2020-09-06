import React, { Component, useState,useEffect} from 'react';
import { Route, NavLink, HashRouter } from "react-router-dom";
import Home from './pages/Home'; import SPSC from './pages/SPSC'; import TPSC from './pages/TPSC'; import GamePrediction from './pages/GamePrediction';
import websiteHeader from './images/websiteHeader.jpg'


function App() {
  
    return ( 
        <HashRouter>
          {/* Header section */}
          <div className="jumbotron" style={{backgroundImage: `url(${websiteHeader})`,backgroundSize: 'auto 100%',}}></div>  
          <div className="lead d-flex justify-content-center">
            <p className="h2">
              Welcome to your favorite NBA Stats Page! 
              <small className="text-muted">  Created By: Pedja Muratovic</small>
            </p>
          </div>

          {/* Nav Bar Section */}
          <div className="justify-content-center">
            <nav className="navbar navbar-expand-sm bg-dark navbar-dark justify-content-center">
              <ul className="navbar-nav">
                <li className="nav-item"><NavLink className="nav-link" exact to="/">Home</NavLink> </li>
                <li className="nav-item"><NavLink className="nav-link" to="/SPSC">Single Player Shot Chart</NavLink> </li>
                <li className="nav-item"><NavLink className="nav-link" to="/TPSC">Two Player Shot Chart</NavLink> </li>
                <li className="nav-item"><NavLink className="nav-link" to="game-pred">Game Predictions</NavLink> </li>
              </ul>
            </nav>
            <br/>
          </div>
          <div className="content">
            <Route exact path="/" component={Home} />
            <Route path="/SPSC" component={SPSC} />
            <Route path="/TPSC" component={TPSC} />
            <Route path="/game-pred" component={GamePrediction} />
          </div>
          
        </HashRouter>

    );
  
}




export default App;
