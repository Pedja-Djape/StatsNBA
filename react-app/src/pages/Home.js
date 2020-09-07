import React, { Component } from 'react';
import './pages.css'


class Home extends Component {
  
    render() {

      return (
        <div>

          <div className="d-flex justify-content-center"><p>This is where our main page will be.</p></div>

          <div className="card-deck">
            <div className="card box-shadow-hover pointer">
              <img className="card-img-top" src={require('../images/SPSC.jpg')} alt='spscImg'></img>
              <div className="card-body">
                <h4 className="card-title">How efficient is your favourite player?</h4>
                <p className="card-text" style={{fontSize: 'medium'}}>Get individual and league-relative shot charts for over 200+ active players!</p>
                <a href="#/SPSC" className="btn btn-dark stretched-link d-flex justify-content-center" 
                onMouseOver={(e) => {e.target.style.background = 'green'; }}
                
                onMouseLeave={(e) => e.target.style.background = '#343a40'} >
                  Get your predictions now!</a>
              </div>
            </div>

            <div className="card box-shadow-hover pointer">
              <img className="card-img-top" src={require('../images/TPSC.png')} alt='tpscImg'></img>
              <div className="card-body">
                <h4 className="card-title">Who will win?</h4>
                <p className="card-text"> Some description  </p>
                <a href="#/TPSC" className="btn btn-dark stretched-link d-flex justify-content-center" style={{transition: "margin-right 4s"}}
                onMouseOver={(e) => e.target.style.background = 'green'} onMouseLeave={(e) => e.target.style.background = '#343a40'} >
                  Get your predictions now!</a>
              </div>
            </div>

            <div className="card box-shadow-hover pointer">
              <img className="card-img-top" src={require('../images/gamePrediction.jpg')} alt='gpImg'></img>
              <div className="card-body">
                <h4 className="card-title">Who will win?</h4>
                <p className="card-text"> ML DNN algo to predict games blah blah... </p>
                <a href="#/game-pred" className="btn btn-dark stretched-link d-flex justify-content-center" 
                onMouseOver={(e) => e.target.style.background = 'green'} onMouseLeave={(e) => e.target.style.background = '#343a40'} >
                  Get your predictions now!</a>
              </div>
            </div>


          </div>  
        </div>
      );
    }
  }

export default Home;