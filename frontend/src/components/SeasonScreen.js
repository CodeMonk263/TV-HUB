import "./App.css";
import React, { Component } from 'react';
import { Button , Card, ListGroup, Container, Row, Col } from 'react-bootstrap';
import history from "../history";
import axios from "axios";

class SeasonScreen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            season_id: this.props.location.state.id_season,
            season_title: this.props.location.state.title_season,
            season_href: this.props.location.state.href_season,
            season_num: this.props.location.state.season,
            season_ep: [],
            placeholder: "None"
        };
        this.GETRequest = this.GETRequest.bind(this);
    }

    goToEpisode = (ep) => {
        if (ep.href.length > 100) {
            history.push('/episode', { id_ep: ep.id, title_ep: ep.title, href_ep: ep.href, season_ep: ep.season, episode: ep.episode });
            window.location.assign('/episode');
        } else {
            window.location.assign(ep.href);
        }
    };

    GETRequest(url) {
        fetch(url)
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(data => {
          this.setState( { season_ep: data });
        });
    }

    POSTRequest = async (url) => {
        await axios.post(url, 
        {
            "title": this.state.season_title,
            "season": this.state.season_num,
            "href": this.state.season_href
        },
        {
        headers: {
            'Content-Type': 'application/json'
        }
        })
        .then(res => {
            this.GETRequest("http://localhost:8000/api/episodes/")
        })
        .catch(err => console.log(err))
    }

    componentDidMount() {
        this.POSTRequest("http://localhost:8000/api/episodes/get_episodes/");
    };

    render() {
        return (
            <div className="wrapper" >
                <Container fluid className="page-footer">
                    <br/>
                    <Row xs={2} md={4} lg={6}>
                        <Col >
                            <Button className="button" variant="secondary" onClick={event => history.goBack()}>Back</Button>
                        </Col>
                    </Row>
                    <br/>
                    <Row>
                        <h1 className="title-text"> {this.state.season_title} - Season {this.state.season_num} </h1>
                    </Row>
                    <Row>
                        <Col></Col>
                    </Row>
                </Container>
                <Container fluid>
                    <Row className="row-grid">
                    {(this.state.season_ep.length > 0) ?  
                        this.state.season_ep.map(ep => {
                        return (
                            <Col className="col-grid" key={ep.id}>
                            <Card style={{ width: '18rem' }}>
                                <Card.Body className="black-bg" >
                                <Card.Title>
                                    <h3 className="title-text">Episode {ep.episode} </h3>
                                    <Button className="button" variant="secondary" onClick={() => {this.goToEpisode(ep)}}>WATCH</Button>
                                </Card.Title>
                                </Card.Body>
                            </Card>
                        </Col> )}) : <h2>Loading...</h2>  }
                    </Row>
                </Container>
            </div>
        );
    };
}

export default SeasonScreen;