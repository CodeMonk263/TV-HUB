import "./App.css";
import React, { Component } from 'react';
import { Button , Card, ListGroup, Container, Row, Col, Grid } from 'react-bootstrap';
import history from "../history";
import axios from "axios";

class VidScreen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            show_id: this.props.location.state.id_show,
            show_title: this.props.location.state.title_show,
            show_href: this.props.location.state.href_show,
            show_seasons: [],
            placeholder: "None"
        };
        this.GETRequest = this.GETRequest.bind(this);
    }

    goToSeason = (season) => {
        history.push('/season', { id_season: season.id, title_season: season.title, href_season: season.href, season: season.season });
        window.location.assign('/season');
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
          this.setState( { show_seasons: data });
        });
    }

    POSTRequest = async (url) => {
        await axios.post(url, 
        {
            "title": this.state.show_title,
            "href": this.state.show_href
        },
        {
        headers: {
            'Content-Type': 'application/json'
        }
        })
        .then(res => {
            this.GETRequest("http://localhost:8000/api/seasons/")
        })
        .catch(err => console.log(err))
    }

    componentDidMount() {
        this.POSTRequest("http://localhost:8000/api/seasons/get_seasons/");
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
                        <h1 className="title-text"> {this.state.show_title} </h1>
                    </Row>
                    <Row>
                        <Col></Col>
                    </Row>
                </Container>
                <Container fluid>
                    <Row className="row-grid">     
                        {(this.state.show_seasons.length > 0) ?
                        this.state.show_seasons.map(season => {
                        return (
                            <Col className="col-grid" key={season.id}>
                            <Card style={{ width: '18rem' }}>
                                <Card.Body className="black-bg" >
                                <Card.Title>
                                    <h3 onClick={() => {this.goToSeason(season)}} className="title-text">Season {season.season}</h3>
                                </Card.Title>
                                </Card.Body>
                            </Card>
                            </Col> )}
                        ) : <h2>Loading...</h2>  }
                    </Row>
                </Container>
            </div>
        );
    };
}

export default VidScreen;