import React, { Component } from 'react';
import DropDown from './Components/Dropdown';
import lbjmelo from '../images/lbjmelo.gif';
import axios from 'axios';

const playerOptions = [{name: 'James Harden'}, {name: 'Damian Lillard'}, {name: 'Devin Booker'}, {name: 'Giannis Antetokounmpo'},
 {name: 'Trae Young'}, {name: 'Luka Doncic'}, {name: 'Bradley Beal'},{name: 'LeBron James'}, {name: 'Donovan Mitchell'},
 {name: 'Anthony Davis'}, {name: 'CJ McCollum'}, {name: 'Russell Westbrook'}, {name: 'Jayson Tatum'},{name: 'Kawhi Leonard'},
 {name: 'Zach LaVine'}, {name: 'DeMar DeRozan'}, {name: 'Brandon Ingram'}, {name: 'Nikola Jokic'}, {name: 'Tobias Harris'},
 {name: 'Buddy Hield'}, {name: 'Pascal Siakam'}, {name: 'Collin Sexton'}, {name: 'Shai Gilgeous-Alexander'}];

class TPSC extends Component {
  constructor(props){
    super(props);
    this.state = {
      image: lbjmelo,
      players: [null,null],
      grammar: ["'s","'s"],
      player1Stats: {
        shotZoneBasic: Array(18).fill('---'),
        shotZoneArea: Array(18).fill('---'),
        shotZoneRange: Array(18).fill('---'),
        fgPct: Array(18).fill('---')
      },
      player2Stats: {
        shotZoneBasic: Array(18).fill('---'),
        shotZoneArea: Array(18).fill('---'),
        shotZoneRange: Array(18).fill('---'),
        fgPct: Array(18).fill('---')
      }
    };
    this.handlePlayerSelection = this.handlePlayerSelection.bind(this)
    this.getComparison = this.getComparison.bind(this)
  }
  componentDidMount() {
    if (this.state.players[0] != null && this.state.players[0][-1] === 's'){
      this.setState({grammar: ["'",this.state.grammar[1]]})
    }
    if (this.state.players[1] != null && this.state.players[1][-1] === 's'){
      this.setState({grammar: [this.state.grammar[1],"'"]})
    }
  }
  handlePlayerSelection(selectedPlayer,id) {
    this.state.players[id] = selectedPlayer;
    this.setState({players: this.state.players})
    console.log(this.state.players)
    if ((this.state.players[0] != null) && this.state.players[0] === this.state.players[1]){
      alert('You must select 2 different players! Players have been cleared!')
      this.state.players[0] = null; this.state.players[1] = null;
      this.setState({players: this.state.players})
      // window.location.reload(false)

    }
  }

  getComparison() {
    // console.log('Button working...')
    axios.get(`/api/getCompSc/${this.state.players[0]}/${this.state.players[1]}`).then( (response) => {
      const shotChart = 'data:image/jpeg;base64,' + response.data.shotChart;
      this.setState({image: shotChart})
    }, (error) => {
      console.log(error)
    })
    axios.get(`/api/player-shooting-stats/${this.state.players[0]}`).then((response) => {
      this.setState({
        player1Stats: {
          shotZoneBasic: response.data.pdf[0],
          shotZoneArea: response.data.pdf[1],
          shotZoneRange: response.data.pdf[2],
          fgPct: response.data.pdf[3]
        }
      })
    }, (error) => {
      console.log(error)
    })
    axios.get(`/api/player-shooting-stats/${this.state.players[1]}`).then((response) => {
      this.setState({
        player2Stats: {
          shotZoneBasic: response.data.pdf[0],
          shotZoneArea: response.data.pdf[1],
          shotZoneRange: response.data.pdf[2],
          fgPct: response.data.pdf[3]
        }
      })
    }, (error) => {
      console.log(error)
    })

  }

  getTableRow(type,idx){
    if (type === 'player1') {
      return (
        <tr>
          <td >{this.state.player1Stats.shotZoneBasic[idx]}</td><td >{this.state.player1Stats.shotZoneArea[idx]}</td>
          <td >{this.state.player1Stats.shotZoneRange[idx]}</td><td >{this.state.player1Stats.fgPct[idx]}</td>
        </tr>  
      );
    }
    else if (type === 'player2') {
      return (
        <tr>
          <td >{this.state.player2Stats.shotZoneBasic[idx]}</td><td >{this.state.player2Stats.shotZoneArea[idx]}</td>
          <td >{this.state.player2Stats.shotZoneRange[idx]}</td><td >{this.state.player2Stats.fgPct[idx]}</td>
        </tr>  
      );
    }
  }



    render() {
      return (
        <React.Fragment>
          <div class='container-fluid'>
            <div class='row'>
              <div class='col d-flex justify-content-center'>
                <div className="button-group w-100 d-flex">
                  <DropDown buttonID={0} page='#/TPSC' title='Select the first player!' options={playerOptions} handleOpt={this.handlePlayerSelection}/>
                  <DropDown buttonID={1} page='#/TPSC' title='Select the second player!'options={playerOptions} handleOpt={this.handlePlayerSelection}/>
                </div>
              </div>
            </div>

            <div class='row'>
              <div class='col d-flex justify-content-center'>
                <p>You've selected the following 2 players:</p>
              </div>
            </div>
            <div class='row'>
              <div class='col d-flex justify-content-center'>
                <ol className="list-group-flush">
                  {this.state.players.map( (player) => 
                    <li>{player}</li>
                  )}
                </ol>
              </div>
            </div>

            <div class='row'>
              <div className='col d-flex justify-content-center'>
                <button type='button' className='button btn-outline-dark btn-lg' onClick={this.getComparison}>Compare!</button>
              </div>
            </div>

            <div class='row'>
              <div className='col d-flex justify-content-center' style={{marginTop: '25px'}}>
                <img src={this.state.image}/>
              </div>
            </div>
            
            <div className='row' style={{marginTop: '30px'}}>
              <div className='col d-flex justify-content-center'>
                  <h3>{this.state.players[0]}{this.state.grammar[0]} Career Averages</h3>
              </div>
              <div className='col d-flex justify-content-center'>
              <h3>{this.state.players[1]}{this.state.grammar[1]} Career Averages</h3>
              </div>
            </div>

            <div className='row' style={{marginTop: '30px'}}>
              <div className='col-6 d-flex justify-content-center'>
                <table class='table'>
                  <thead className='thead-dark'>
                    <tr>
                      <th>Shot Zone Basic</th>
                      <th>Shot Zone Area</th>
                      <th>Shot Zone Range</th>
                      <th>FG %</th>
                    </tr>
                  </thead>
                  <tbody>
                    {this.getTableRow('player1',0)}
                    {this.getTableRow('player1',1)}
                    {this.getTableRow('player1',2)}
                    {this.getTableRow('player1',3)}
                    {this.getTableRow('player1',4)}
                    {this.getTableRow('player1',5)}
                    {this.getTableRow('player1',6)}
                    {this.getTableRow('player1',7)}
                    {this.getTableRow('player1',8)}
                    {this.getTableRow('player1',9)}
                    {this.getTableRow('player1',10)}
                    {this.getTableRow('player1',11)}
                    {this.getTableRow('player1',12)}
                    {this.getTableRow('player1',13)}
                    {this.getTableRow('player1',14)}
                    {this.getTableRow('player1',15)}
                    {this.getTableRow('player1',16)}
                    {this.getTableRow('player1',17)}
                  </tbody>
                </table>
              </div>
              <div className='col-6 d-flex justify-content-center'>
                <table className='table'>
                  <thead className='thead-dark'>
                    <tr>
                      <th>Shot Zone Basic</th>
                      <th>Shot Zone Area</th>
                      <th>Shot Zone Range</th>
                      <th>FG %</th>
                    </tr>
                  </thead>
                  <tbody>
                    {this.getTableRow('player2',0)}
                    {this.getTableRow('player2',1)}
                    {this.getTableRow('player2',2)}
                    {this.getTableRow('player2',3)}
                    {this.getTableRow('player2',4)}
                    {this.getTableRow('player2',5)}
                    {this.getTableRow('player2',6)}
                    {this.getTableRow('player2',7)}
                    {this.getTableRow('player2',8)}
                    {this.getTableRow('player2',9)}
                    {this.getTableRow('player2',10)}
                    {this.getTableRow('player2',11)}
                    {this.getTableRow('player2',12)}
                    {this.getTableRow('player2',13)}
                    {this.getTableRow('player2',14)}
                    {this.getTableRow('player2',15)}
                    {this.getTableRow('player2',16)}
                    {this.getTableRow('player2',17)}
                  </tbody>
                </table>

              </div>
            </div>



          </div>
        </React.Fragment>
      );
    }
}

export default TPSC;