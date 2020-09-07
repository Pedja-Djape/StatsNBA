import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './SPSC.css'
import axios from 'axios';
import shotGif1 from '../images/shotGif1.gif';
import shotGif2 from '../images/shotGif2.gif';


class Autosuggest extends Component {
  constructor(props){
    super(props);
    this.state = {
      activeOption: 0,
      filteredList: [],
      showOpts: false,
      userInput: '',
    };
    this.onChange = this.onChange.bind(this);
    this.onClick = this.onClick.bind(this)
    this.onKeyDown = this.onKeyDown.bind(this);
    // this.getSubmit = this.getSubmit.bind(this);
  }

  static propTypes = {
    options: PropTypes.instanceOf(Array).isRequired,
  };

  onChange(e) {
    const {options} = this.props;
    const userInput = e.currentTarget.value;
    const filteredList = options.filter( (options) => 
      options.toLowerCase().indexOf(userInput.toLowerCase()) > -1
    );
    this.setState({
      activeOption: 0,filteredList, showOpts: true, userInput: e.currentTarget.value 
    })
  }

  onClick(e) {
    this.setState({activeOption: 0, filteredList: [], showOpts: false, userInput: e.currentTarget.innerText,selectedPlayer: e.currentTarget.innerText});
  }

  onKeyDown(e) {
    const {activeOption, filteredList} = this.state;
    if (e.keyCode === 13) {
      this.setState({activeOption: 0, showOpts: false, userInput: filteredList[activeOption]});
    } 
    else if (e.keyCode === 38){
      if (activeOption === 0) {
        return;
      }
    this.setState({activeOption: activeOption - 1});
    }
    else if (e.keyCode === 40){
      if (activeOption === filteredList.length - 1) {
        return;
      }
      this.setState({activeOption: activeOption + 1});
    }

  };




  render() {
    let optList;
    if (this.state.showOpts && this.state.userInput){
      if (this.state.filteredList.length) {
        optList = (
          <div className="list-group " style={{maxHeight: '210px',overflowY: 'auto'}}>
            {this.state.filteredList.map((opt,idx) => {
              return (
                <a href="#/SPSC" className="list-group-item list-group-item-action d-flex justify-content-center" 
                style={{height: '30px',padding: '5px 15px'}} onClick={(e) => this.onClick(e)}>{opt}</a>
              );
            })}
          </div>
        );
      }
      else {
        optList = (
          <div className="no-options">
            <em>No Options!</em>
          </div>
        );
      }
    }
    return (
      <React.Fragment>

        <div id='wrapper'>
          <div className="d-flex justify-content-center">
              <input type="text" onChange={(e) => this.onChange(e)} onKeyDown={(e) => this.onKeyDown(e)} value={this.state.userInput} className="form-control" placeholder="Enter Player Name"/>
              <button type="button" className="btn btn-dark" onClick= {() => {
                this.props.getSubmit(this.state.userInput);
              }}>
                Submit!
              </button>
          </div>
            {optList}

        </div>

      </React.Fragment>
    );
  }
}


class SPSC extends Component {
  constructor(props) {
    super(props);
    this.state = {
      soloSC: shotGif1,
      leagueComp: shotGif2,
      submitClicked: false,
      players: [],
      leagueStats: {
        shotZoneBasic: Array(18).fill('---'),
        shotZoneArea: Array(18).fill('---'),
        shotZoneRange: Array(18).fill('---'),
        fgPct: Array(18).fill('---')
      }, 
      playerStats: {
        shotZoneBasic: Array(18).fill('---'),
        shotZoneArea: Array(18).fill('---'),
        shotZoneRange: Array(18).fill('---'),
        fgPct: Array(18).fill('---')
      },
    }
    this.getShotchart = this.getShotchart.bind(this)
  }
  
  componentDidMount() {
    axios.get('/api/players').then( (response) => {
      var players = response.data.players
      this.setState({players:players})
    })
    
  }

  getShotchart(player_name) {
    if ((this.state.players).includes(player_name) === false){
      axios.get(`/api/player-sc/${player_name}`).then((response) => {
        const soloSC = 'data:image/jpeg;base64,' + response.data.soloSC
        const playerLeagueSC = 'data:image/jpeg;base64,' + response.data.playerLeagueSC
        // console.log(image)
        this.setState({soloSC: soloSC,leagueComp: playerLeagueSC})
        }
      );
      alert('Adding player to database...');
      // window.location.reload(false);
    } else {
      axios.get(`/api/player-sc/${player_name}`).then((response) => {
        const soloSC = 'data:image/jpeg;base64,' + response.data.soloSC
        const playerLeagueSC = 'data:image/jpeg;base64,' + response.data.playerLeagueSC
        this.setState({soloSC: soloSC,leagueComp: playerLeagueSC,
          leagueStats: {
            shotZoneBasic: response.data.ldf[0],
            shotZoneArea: response.data.ldf[1],
            shotZoneRange: response.data.ldf[2],
            fgPct: response.data.ldf[3]
          },
          playerStats: {
            shotZoneBasic: response.data.pdf[0],
            shotZoneArea: response.data.pdf[1],
            shotZoneRange: response.data.pdf[2],
            fgPct: response.data.pdf[3]
            }
            })
        console.log(response.data.pdf)
        }
      );
    }
  }

    getTableRow(type,idx){
      let t;
      if (type === 'player') {
        return (
          <tr>
            <td >{this.state.playerStats.shotZoneBasic[idx]}</td><td >{this.state.playerStats.shotZoneArea[idx]}</td>
            <td >{this.state.playerStats.shotZoneRange[idx]}</td><td >{this.state.playerStats.fgPct[idx]}</td>
          </tr>  
        );
      }
      else if (type === 'league') {
        return (
          <tr>
            <td >{this.state.leagueStats.shotZoneBasic[idx]}</td><td >{this.state.leagueStats.shotZoneArea[idx]}</td>
            <td >{this.state.leagueStats.shotZoneRange[idx]}</td><td >{this.state.leagueStats.fgPct[idx]}</td>
          </tr>  
        );
      }
    }

    render() {


      return (
        <div className="container-fluid">         

            <div className='row '>
              <div className='col d-flex justify-content-center'>
                  <Autosuggest options={this.state.players} getSubmit={this.getShotchart}/>
              </div>
            </div>

            <div className='row' style={{marginTop: '30px'}}>
              <div className='col d-flex justify-content-center'>
                <img src={this.state.soloSC} />
              </div>
              <div className='col d-flex justify-content-center'>
                <img src = {this.state.leagueComp}/>
              </div>
            </div>

            <div className='row' style={{marginTop: '30px'}}>
              <div className='col d-flex justify-content-center'>
                <h3>Player Career Averages</h3>
              </div>
              <div className='col d-flex justify-content-center'>
                <h3>Current League Averages</h3>
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
                    {this.getTableRow('player',0)}
                    {this.getTableRow('player',1)}
                    {this.getTableRow('player',2)}
                    {this.getTableRow('player',3)}
                    {this.getTableRow('player',4)}
                    {this.getTableRow('player',5)}
                    {this.getTableRow('player',6)}
                    {this.getTableRow('player',7)}
                    {this.getTableRow('player',8)}
                    {this.getTableRow('player',9)}
                    {this.getTableRow('player',10)}
                    {this.getTableRow('player',11)}
                    {this.getTableRow('player',12)}
                    {this.getTableRow('player',13)}
                    {this.getTableRow('player',14)}
                    {this.getTableRow('player',15)}
                    {this.getTableRow('player',16)}
                    {this.getTableRow('player',17)}
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
                    {this.getTableRow('league',0)}
                    {this.getTableRow('league',1)}
                    {this.getTableRow('league',2)}
                    {this.getTableRow('league',3)}
                    {this.getTableRow('league',4)}
                    {this.getTableRow('league',5)}
                    {this.getTableRow('league',6)}
                    {this.getTableRow('league',7)}
                    {this.getTableRow('league',8)}
                    {this.getTableRow('league',9)}
                    {this.getTableRow('league',10)}
                    {this.getTableRow('league',11)}
                    {this.getTableRow('league',12)}
                    {this.getTableRow('league',13)}
                    {this.getTableRow('league',14)}
                    {this.getTableRow('league',15)}
                    {this.getTableRow('league',16)}
                    {this.getTableRow('league',17)}
                  </tbody>
                </table>

              </div>
            </div>
        </div>
        
      );
    }
  }

export default SPSC;