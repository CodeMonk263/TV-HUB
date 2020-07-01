import "./App.css";
import React, { Component } from 'react';
import { Button , Card, ListGroup, Container, Row, Col } from 'react-bootstrap';
import history from "../history";
import axios from "axios";

class EpisodeScreen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            ep_id: this.props.location.state.id_ep,
            ep_title: this.props.location.state.title_ep,
            ep_href: this.props.location.state.href_ep,
            ep_season: this.props.location.state.season_ep,
            ep_num: this.props.location.state.episode,
            ep_data: [],
            placeholder: "None"
        };
    }

    GETRequest = async (url) => {
        const request = await axios.get(url);
        this.setState( { ep_href: request.data.href });
    }

    componentDidMount() {
        if (this.state.ep_href.length > 150) {
            this.GETRequest(`http://localhost:8000/api/episodes/${this.state.ep_id}/watch_episode/`);
        }
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
                        <h1 className="title-text"> {this.state.ep_title} - Season {this.state.ep_season} -  Episode {this.state.ep_num} </h1>
                    </Row>
                    <Row>
                        <Col></Col>
                    </Row>
                </Container>
                <Container fluid>
                    <Row className="row-grid">     
                        <Col className="col-grid">
                            {this.state.ep_href.length < 150 ? 
                                <video src={this.state.ep_href} controls></video> 
                                : <h2>Loading...</h2>  
                            }
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    };
}

export default EpisodeScreen;