import React, { Component } from 'react';

class Dropdown extends Component {
    constructor(props) {
      super(props);
      this.state = {
        headerTitle: this.props.title,
        options: this.props.options,
        buttonID: this.props.buttonID,
        link: this.props.page
  
      };
    }
  
    render() {
      return (
        <div className="btn-group w-100 d-flex">
          <button type="button" className="btn-dark w-100 dropdown-toggle" data-toggle="dropdown">
            {this.state.headerTitle}
          </button>
          <ul className="dropdown-menu pre-scrollable w-100" role="menu">
            {this.state.options.map((opt) => {
              return (
                <li>
                  <a href={this.state.link} className="dropdown-item d-flex justify-content-center" onClick={() => {
                    this.props.handleOpt(opt.name,this.state.buttonID);
                    this.setState({headerTitle: opt.name});
                  }}>{opt.name}</a>
                </li>
              );
            })}
          </ul>
  
        </div>
      );
    }
  }
export default Dropdown