import React, { Component } from 'react';
import axios from 'axios';
import Dropdown from './Components/Dropdown'

const teams = [{name: 'ATL', id: 0}, {name: 'BOS', id: 1}, {name: 'CLE', id: 2}, {name: 'NOP', id: 3},
{name: 'CHI', id: 4}, {name: 'DAL', id: 5}, {name: 'DEN', id: 6}, {name: 'GSW', id: 7},
{name: 'HOU', id: 8}, {name: 'LAC', id: 9}, {name: 'LAL', id: 10}, {name: 'MIA', id: 11},
{name: 'MIL', id: 12}, {name: 'MIN', id: 13}, {name: 'BKN', id: 14}, {name: 'NYK', id: 15},
{name: 'ORL', id: 16}, {name: 'IND', id: 17}, {name: 'PHI', id: 18}, {name: 'PHX', id: 19},
{name: 'POR', id: 20}, {name: 'SAC', id: 21}, {name: 'SAS', id: 22}, {name: 'OKC', id: 23},
{name: 'TOR', id: 24}, {name: 'UTA', id: 25}, {name: 'MEM', id: 26}, {name: 'WAS', id: 27},
{name: 'DET', id: 28}, {name: 'CHA', id: 29}];

class GamePrediction extends Component {
  constructor(props){
    super(props);
    this.state = {
      teams: [null,null],
      info: {home: {full_name: ''},
             away: {full_name: ''}}
    };
    this.handleTeamSelection = this.handleTeamSelection.bind(this);
    this.getWinner = this.getWinner.bind(this)
  }
  
  handleTeamSelection(selectedTeam,id) {
    this.state.teams[id] = selectedTeam;
    this.setState({teams: this.state.teams})
    if ((this.state.teams[0] != null) && this.state.teams[0] === this.state.teams[1]){
      alert('You must select 2 different teams! Teams have been cleared!')
      this.state.teams[0] = null; this.state.teams[1] = null;
      this.setState({teams: this.state.teams})
      // window.location.reload(false)
    }
    console.log(this.state)
  } 

  getWinner() {
    if (this.state.teams[0] != null && this.state.teams[1] != null){
      console.log('Proceed')
      axios.get(`/api/team-info/${this.state.teams[0]}/${this.state.teams[1]}`).then((response) => {
        const homeInfo = response.data.home
        const awayInfo = response.data.away
        console.log(response.data)
        this.setState({info: {home: homeInfo, away: awayInfo} }) 
      }, (error) => {
          console.log(error);
        })       
      }
      
    
    else {
      alert('You must select and away team and a home team to proceed!')
    }
  }

  render() {
    return (
      <React.Fragment>
        <div className='container-fluid'>

          <div className='row'>
            <div className='col d-flex justify-content-center'>
              <Dropdown buttonID={0} page='#/game-pred' title="Select the Home Team!" options={teams} handleOpt={this.handleTeamSelection} /> 
              <Dropdown buttonID={1} page='#/game-pred' title="Select the Away Team!" options={teams} handleOpt={this.handleTeamSelection} /> 
            </div>
          </div>

          <div className='row' style={{marginTop: '30px'}}>
            <div className='col d-flex justify-content-center'>
              <p>You have selected the following Teams:</p> 
            </div>
          </div>

          <div className='row' style={{marginTop: '30px'}}>
            <div className='col d-flex justify-content-center'>
              <ol className="list-group-flush">
                {this.state.teams.map( (team) => 
                    <li>{team}</li>
                )}
              </ol>
            </div>
          </div>

          <div className='row' style={{marginTop: '30px'}}>
            <div className='col d-flex justify-content-center'>
            <h3> Home: {this.state.info.home.full_name} </h3>
            </div>
            <div className='col d-flex justify-content-center'>
              <h3>Away: {this.state.info.away.full_name}</h3>
            </div>
          </div>

          <div className='row' style={{marginTop: '30px'}}>
            <div className='col d-flex justify-content-center'>
              <button type="button" className="btn btn-dark btn-lg" onClick={this.getWinner}>Get Winner!</button>
            </div>
          </div>


        </div>
      </React.Fragment>


    )}
      

}








export default GamePrediction;
