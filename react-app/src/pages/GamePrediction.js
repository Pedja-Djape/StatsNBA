import React, { Component } from 'react';


class Dropdown extends Component {
  constructor(props) {
    super(props);
  
    this.state = {
      isOpen: false,
      headerTitle: this.props.title,
      teams: [{name: 'ATL', id: 0}, {name: 'BOS', id: 1}, {name: 'CLE', id: 2}, {name: 'NOP', id: 3},
      {name: 'CHI', id: 4}, {name: 'DAL', id: 5}, {name: 'DEN', id: 6}, {name: 'GSW', id: 7},
      {name: 'HOU', id: 8}, {name: 'LAC', id: 9}, {name: 'LAL', id: 10}, {name: 'MIA', id: 11},
      {name: 'MIL', id: 12}, {name: 'MIN', id: 13}, {name: 'BKN', id: 14}, {name: 'NYK', id: 15},
      {name: 'ORL', id: 16}, {name: 'IND', id: 17}, {name: 'PHI', id: 18}, {name: 'PHX', id: 19},
      {name: 'POR', id: 20}, {name: 'SAC', id: 21}, {name: 'SAS', id: 22}, {name: 'OKC', id: 23},
      {name: 'TOR', id: 24}, {name: 'UTA', id: 25}, {name: 'MEM', id: 26}, {name: 'WAS', id: 27},
      {name: 'DET', id: 28}, {name: 'CHA', id: 29}],
    };
    this.handleClick = this.handleClick.bind(this)
  }
  handleClick(teamID) {
      // this.setState({headerTitle: 'clicked'})
      // this.setState({
      //   headerTitle: this.state.teams[id]
      // });
      console.log(this.state.teams[teamID].name);
  }
  // getTeamName(team){
  //   return (
  //     <li><a href="#/game-pred" className="dropdown-item d-flex justify-content-center" onClick={() => this.handleClick}>{team.name}</a></li>
  //     );
  // }

  render() {
    return (
      <div className="btn-group w-100 d-flex">
        <button type="button" className="btn-success w-100 dropdown-toggle" data-toggle="dropdown">
          {this.state.headerTitle}
        </button>
        <ul className="dropdown-menu pre-scrollable w-100" role="menu">
          {this.state.teams.map((team) => {
            return (
              <li>
                <a href="#/game-pred" className="dropdown-item d-flex justify-content-center" onClick={() => this.handleClick(team.id)}>{team.name}</a>
              </li>
            );
          })}
        </ul>

      </div>
    );
  }
}

class GamePrediction extends Component {
  render() {
    const teams = [{name: 'ATL', id: 0}, {name: 'BOS', id: 1}, {name: 'CLE', id: 2}, {name: 'NOP', id: 3},
                   {name: 'CHI', id: 4}, {name: 'DAL', id: 5}, {name: 'DEN', id: 6}, {name: 'GSW', id: 7},
                   {name: 'HOU', id: 8}, {name: 'LAC', id: 9}, {name: 'LAL', id: 10}, {name: 'MIA', id: 11},
                   {name: 'MIL', id: 12}, {name: 'MIN', id: 13}, {name: 'BKN', id: 14}, {name: 'NYK', id: 15},
                   {name: 'ORL', id: 16}, {name: 'IND', id: 17}, {name: 'PHI', id: 18}, {name: 'PHX', id: 19},
                   {name: 'POR', id: 20}, {name: 'SAC', id: 21}, {name: 'SAS', id: 22}, {name: 'OKC', id: 23},
                   {name: 'TOR', id: 24}, {name: 'UTA', id: 25}, {name: 'MEM', id: 26}, {name: 'WAS', id: 27},
                   {name: 'DET', id: 28}, {name: 'CHA', id: 29}];
    
    
    return (
      <div className="button-group w-100 d-flex">
        <Dropdown title="Team 1" teams={teams}/>
        {/* <Dropdown title="Team 2" teams={teams}/> */}
      </div>
    );
  }
}







export default GamePrediction;