import "./App.css";
import React, { Component } from "react";
import history from "../history"
import { Button , Card, Container, Row, Col, Alert, InputGroup, FormControl, Form } from "react-bootstrap";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      search_term: "",
      loaded: false,
      placeholder: "Loading",
    };
    this.textInput = React.createRef();
    this.onSubmit = this.onSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(value) {
    this.setState({search_term: value});
  }

  onSubmit(event) {
    this.POSTRequest("http://localhost:8000/api/shows/search_shows/")
    event.preventDefault();
  }

  GETRequest = async (url) => {
    const request = await axios.get(url);
    if (request.data === "Success") {
      this.GETRequest("http://localhost:8000/api/shows/");
    } else {
      this.setState( { data: request.data, loaded: true });
    }
  }

  POSTRequest = async (url) => {
    await axios.post(url,
    {
      "search": this.state.search_term
    },
    {
    headers: {
        'Content-Type': 'application/json'
    }
    })
    .then(res => {
        this.GETRequest("http://localhost:8000/api/shows/")
    })
    .catch(err => console.log(err))
  }

  componentDidMount() {
    this.GETRequest("http://localhost:8000/api/shows/get_shows/");
    console.log(this.state.data);
  };

  goToShow = (video) => {
    history.push('/show', { id_show: video.id, title_show: video.title, href_show: video.href });
    window.location.assign('/show');
  };

  render() {
    return (
      <div className="black-bg" >
        <Container fluid>
        <Row>
        <Col xs={6} md={4}></Col>  
        <Col xs={6} md={4}>
        <h1 className="page-title">Latest TV Shows</h1>
        </Col>
        <Col xs={6} md={4}></Col> 
        </Row>
        <Row>
        <Col xs={6} md={4}></Col>  
        <Col xs={6} md={4}>
          <form onSubmit={this.onSubmit}>
            <label>
              Search:
              <input type="text" onChange={(e)=>this.handleChange(e.target.value)} />
            </label>
            <input type="submit" value="Submit" />
          </form>
        </Col>
        <Col xs={6} md={4}></Col> 
        </Row>
        </Container>
        <Container fluid>
          <Row className="row-grid">     
              {this.state.data.length > 0 ?
              this.state.data.map(show => {
              return (
                <Col className="col-grid" key={show.id}>
                  <Card style={{ width: '18rem' }}>
                    <Card.Img variant="top" src={show.thumbnail_src} />
                    <Card.Body className="black-bg" >
                      <Card.Title>
                        <h3 className="title-text">{show.title}</h3>
                      </Card.Title>
                      <Row>
                      <Col>
                      <Button variant="primary" className="button" onClick={() => this.goToShow(show)} >Watch</Button>
                      </Col>
                      </Row>
                    </Card.Body>
                  </Card>
                </Col>
              );
            }) : <h2>Loading...</h2>}
        </Row>
        </Container>
      </div>
    );
  }
}

export default App;

