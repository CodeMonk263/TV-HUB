
import React, { Component } from "react";
import { Router, Switch, Route } from "react-router-dom";

import App from "./components/App";
import VidScreen from "./components/VidScreen";
import SeasonScreen from "./components/SeasonScreen";
import EpisodeScreen from "./components/EpisodeScreen";
import history from './history';

export default class Routes extends Component {

    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route path="/" exact component={App} />
                    <Route path="/show" exact component={VidScreen} />
                    <Route path="/season" exact component={SeasonScreen} />
                    <Route path="/episode" exact component={EpisodeScreen} />
                </Switch>
            </Router>
        )
    }
}