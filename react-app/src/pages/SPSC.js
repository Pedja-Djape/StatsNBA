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
        const image = 'data:image/jpeg;base64,' + response.data.shotChart
        console.log(image)
        this.setState({soloSC: image})
        }
      );
      alert('Adding player to database...');
      // window.location.reload(false);
    } else {
      axios.get(`/api/player-sc/${player_name}`).then((response) => {
        const image = 'data:image/jpeg;base64,' + response.data.shotChart
        console.log(image)
        this.setState({soloSC: image})
        }
      );
    }

  }


    render() {

      return (
        <div className="container-fluid">         

            <div className='row '>
              <div className='col-xl-12'>
                <div className='d-flex justify-content-center'>  
                  <Autosuggest options={this.state.players} getSubmit={this.getShotchart}/>
                </div>
              </div>
            </div>

            <div className='row d-flex justify-content-center' style={{marginTop: '30px'}}>
              <div className='col-xl-6'>
                <div className="d-flex justify-content-center">
                  <img src={this.state.soloSC} style={{maxWidth:"424.7", maxHeight:"370.6"}}/>
                </div>
              </div>
              <div className='col-xl-6'>
                <div className='d-flex justify-content-center'>
                  <img src = {this.state.leagueComp} style={{maxWidth:"424.7", maxHeight:"370.6"}}/>
                </div>

              </div>
            </div>

        </div>
        
      );
    }
  }

export default SPSC;