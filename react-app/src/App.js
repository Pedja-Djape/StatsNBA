import React, { Component } from 'react';
//import './App.css';
import { Route, NavLink, HashRouter } from "react-router-dom";
import Start from './pages/Start'; import SPSC from './pages/SPSC'; import TPSC from './pages/TPSC'; import GamePrediction from './pages/GamePrediction';



class App extends Component {
  render() {
    return (
      <HashRouter>
        <div>
          <div className="lead d-flex justify-content-center">
            <h1>Welcome to my NBA STATS SPA</h1>
          </div>
          <div className="d-flex justify-content-center">
            <ul className="header">
              <li><NavLink exact to="/">Start</NavLink> </li>
              <li><NavLink to="/SPSC">Single Player Shot Chart</NavLink> </li>
              <li><NavLink to="/TPSC">Two Player Shot Chart</NavLink> </li>
              <li><NavLink to="game-pred">Game Predictions</NavLink> </li>
            </ul>
          </div>
          <div className="content">
            <Route exact path="/" component={Start} />
            <Route path="/SPSC" component={SPSC} />
            <Route path="/TPSC" component={TPSC} />
            <Route path="/game-pred" component={GamePrediction} />
          </div>
        </div>
      </HashRouter>  
    );
  }
}

//{
  /* <div>
  <h1>Is anyone here?</h1>
  <enter>
    <div class='form'>
      <form action="http://localhost:5000/result" method="GET">
        Player Name: <input type="text" name='player' />
        <input type="submit" value="Submit Player" />
      </form>
    </div>

  </enter>
</div> *///}


export default App;
